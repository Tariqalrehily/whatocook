import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo

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



if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT', 3000)),
        debug=True)
