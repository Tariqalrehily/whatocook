import os
from flask import Flask, render_template, redirect, request, url_for, request
from flask_pymongo import PyMongo
from bson.objectid import ObjectId


app = Flask(__name__)
app.config["MONGO_DBNAME"] = "whatocook"
app.config["MONGO_URI"] = "mongodb+srv://root:Tar1010@projectdb-ddwj9.mongodb.net/whatocook?retryWrites=true&w=majority"

mongo = PyMongo(app)

@app.route('/')
@app.route('/get_recipes')
def get_recipes():
    return render_template("recipes.html", recipes=mongo.db.recipes.find())


@app.route('/add_recipe')
def add_recipe():
    return render_template('addrecipe.html', cuisines=mongo.db.cuisines.find())

# insert recipe route, insert as dictionary, so it can easily be understood by Mongo
@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    recipes =  mongo.db.recipes
    recipes.insert_one(request.form.to_dict())
    return redirect(url_for('get_recipes'))


@app.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):
    the_recipe =  mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    cuisines_types =  mongo.db.cuisines.find()
    return render_template('editrecipe.html', recipe=the_recipe, cuisines=cuisines_types)


@app.route('/update_recipe/<recipe_id>', methods=["POST"])
def update_recipe(recipe_id):
    recipes = mongo.db.recipes
    recipes.update( {'_id': ObjectId(recipe_id)},
    {
        'recipe_cuisine':request.form.get('recipe_cuisine'),
        'recipe_food_type':request.form.get('recipe_food_type'),
        'recipe_name':request.form.get('recipe_name'),
        'ingredients': request.form.get('ingredients'),
        'preparation_steps': request.form.get('preparation_steps'),
        'required_tools':request.form.get('required_tools')
    })
    return redirect(url_for('get_recipes'))


@app.route('/delete_recipe/<recipe_id>')
def delete_recipe(recipe_id):
    mongo.db.recipes.remove({'_id': ObjectId(recipe_id)})
    return redirect(url_for('get_recipes'))

# ----------------- cuisine  -----------------

@app.route('/get_cuisines')
def get_cuisines():
    return render_template('cuisines.html', cuisines=mongo.db.cuisines.find())


@app.route('/delete_cuisine/<cuisine_id>')
def delete_cuisine(cuisine_id):
    mongo.db.cuisines.remove({'_id': ObjectId(cuisine_id)})
    return redirect(url_for('get_cuisines'))


@app.route('/edit_cuisine/<cuisine_id>')
def edit_cuisine(cuisine_id):
    return render_template('editcuisine.html',
    cuisine=mongo.db.cuisines.find_one({'_id': ObjectId(cuisine_id)}))


@app.route('/update_cuisine<cuisine_id>', methods=['POST'])
def update_cuisine(cuisine_id):
    mongo.db.cuisines.update(
        {'_id': ObjectId(cuisine_id)},
        {'cuisine_name': request.form.get('cuisine_name')})
    return redirect(url_for('get_cuisines'))


@app.route('/insert_cuisine', methods=['POST'])
def insert_cuisine():
    cuisine_doc = {'cuisine_name': request.form.get('cuisine_name')}
    mongo.db.cuisines.insert_one(cuisine_doc)
    return redirect(url_for('get_cuisines'))


@app.route('/add_cuisine')
def add_cuisine():
    return render_template('addcuisine.html')
    
@app.route('/search_by_cuisine')
def search_by_cuisine():
    return render_template("searchbycuisine.html", cuisines=mongo.db.cuisines.find())

@app.route('/recipes_by_cuisine', methods=["POST"])
def recipes_by_cuisine():
    recipe = mongo.db.recipes.find()
    search = request.form.get('recipes_by_cuisine')
    search_cuisine = mongo.db.recipes.find({"recipe_cuisine": {"name":search}})
    return render_template("recipesbycuisine.html", recipe=recipe, search_cuisine=search_cuisine)

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT', 3000)),
            debug=True)