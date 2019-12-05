import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)
app.config["MONGO_DBNAME"] = "what_to_cook"
app.config["MONGO_URI"] = "mongodb+srv://root:Anatar1010@myfirstcluster-ddwj9.mongodb.net/what_to_cook?retryWrites=true&w=majority"

mongo = PyMongo(app)

@app.route('/')
@app.route('/get_recipes')
def get_recipes():
    return render_template("recipes.html", recipes=mongo.db.recipes.find())

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT', 3000)),
        debug=True)
