import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)
app.config["MONGO_DBNAME"] = "whatocook"
app.config["MONGO_URI"] = "mongodb+srv://root:Tar1010@projectdb-ddwj9.mongodb.net/whatocook?retryWrites=true&w=majority"

mongo = PyMongo(app)

@app.route('/get_recipes')
def get_recipes():
    return render_template("recipes.html", recipes=mongo.db.recipes.find());

@app.route('/add_recipe')
def add_recipe():
    return render_template('addrecipe.html', add_recipe=mongo.db.cuisine.find());

# insert recipe route, insert as dictionary, so it can easily be understood by Mongo
@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    recipes = mongo.db.recipes
    recipes.insert_one(request.form.to_dict())
    return redirect(url_for('get_recipes'))

@app.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):
    the_recipe = mongo.db.recipes.find_one({"_id: ObjectId(recipe_id)"})
    all_cuisines = mongo.db.cuisine.find()
    return render_template('editrecipe.html', recipe=the_recipe, cuisine=all_cuisines)

@app.route('/update_recipe/<recipe_id>', methods=["POST"])
def update_recipe(recipe_id):
    recipe = mongo.db.recipes
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

@app.route('/get_cuisine')
def get_cuisine():
    return render_template('cuisine.html', cuisine=mongo.db.cuisine.find())

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT', 3000)),
        debug=True)
