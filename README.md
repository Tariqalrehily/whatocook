# whatocook

whatocook is a web application for cooking recipes. Is prefect for store and search for cooking recipes for daily meals. Users will have the ability to easy add 
a new recipes by filling recipes form inputs. After storing the recipe with whatocook web application, you can re-visit the app anytime to find that recipe and 
start cooking to enjoy a nice meal.

The application provide users with ability to update the recipes on later stage. Each recipe can be edited or deleted by navigate to the recipe and click edit 
button to start updating or delete button to delete the recipe from the database. Also, this application provide a search function that will allow users to 
search for a recipes. Currently, the whatocook provide search function for recipes by the recipe's cuisines and by the recipes' name. Should you as a user 
wishing to cook a French meal for dinner, you can select search for recipes by French cuisine, and a list for all available French cuisine recipes there to pick one.

Each recipe will have a list of information as follow:

* Recipe cuisine
* Recipe food Type
* Recipe name
* Ingredients
* Recipe steps
* Required Tools
* Recipe Image

whatocook application is built as part of code institute Milestone project.

Go to Live site [whatocook link](https://whatocook.herokuapp.com/)

# The UX
## The UX design
The app has two primary type of users: user who wish to store a new cooking recipe and a user who wish to search for a recipe.

[Wireframe mockups](https://github.com/Tariqalrehily/whatocook/blob/master/Wireframe_mockups.pdf)

### User adding a new recipe
* I want to be able to store a new recipe, as such I can navigate to the top right of the home page to find in the Nav bar a Add recipe link to link to a new page for 
adding a new recipe by filling a form inputs for the recipe and when I finish, I can hit the Add Recipe green button at the end on add recipe html page to add the recipe,
 and the user will be redirected to the home page.
* I want to enter the recipe information. The user can do so, by selecting a cuisine, enter a recipe name, enter recipe name, enter ingredients in text area, enter 
preparation steps, enter the recipe required tools in the text area, and enter recipes image URL. 
* When the user wish to modify a recipe, edit function added to help the user to edit and update the recipe. At the buttom of each recipe in the recipe list. 
Under the cover photo, the user will find a list of all recipes in whatocook app linked database, an Edit button added to  route the user to a new html page to edit 
the wishing recipe's input fields and hit the Edit Recipe blue button at the end of the html page and the user also will be redirected to the home page.
* For user convenient, a delete button also added in red color at the end of each recipes drop down, should the user wish to delete the recipe on later stage.

### User searching for a recipe
* I want to select a recipe name or cuisine to start my search about that recipes. A search link at the top right of the home page a  in the Nav bar provided to start searching.
 This link is linked to a new html page. The search page currently only has two search functions available, it's search by recipes name or cuisine. 
* I want my search results. When the user enter a recipe name or select a cusine, he/she can start the search by clicking on the search recipes blue button under. After, 
the user will be taking to a new html page menu which will be listing all recipes related to that search.
* I want to see the recipe to start cooking. The user can click on the wishing recipe block, to have all recipes information.

## Wireframe mockups
I used Sketch software for Wireframe mockups, as follow:

* First page:  Mobile and Tablet Screens.
* Second page: Landscape Tablet and Desktop Screens.

[Wireframe mockups](https://github.com/Tariqalrehily/whatocook/blob/master/Wireframe_mockups.pdf)

## Features

* The primary feature of this application, is to find, add, edit, and delete a cooking recipes. The home page has the following links:
Home page link in Home Nav bar and whatocook logo.
Search link to route to search page.
Add recipe link to route to add a new recipe.
Manage a recipe to Add, Edit, and delete a cuisine.
under the cover photo, recipes list disply.
Each recipe has drop down arrow should the user wish to disply recipe informatio.
Each recipe has two buttons: Delete in red color and Edit in blue color.

* The land page has 50% heights background, the background image to a cooker for cooking recipes feeling. On the centre of the background image, a paragraph gives the user a direct indicator of the application purpose.

* The app has 10 html pages to fill the user needs to search, add, edit, and delete a cooking recipes.

## Features Left To Implement
* More search options to search for recipes, for example search by recipe food type.
* User authentication to edit and delete recipes, only the user who added the recipe can edit and delete that recipe.
* Function for testing the backend code. 

## Technologies Used
* HTML5
* CSS3
* Materialize
* Javascript
* jQuery
* Python3
* Flask Framework.
* MongoDB the whatocook app data
* Jinja2 templating language.

## Testing

### Store (Add) a recipe
* I have tried and friends by using different devices and screens (see devices below) to add more than one recipe and it works and were added to the whatocook database collection recipes without any error.

### Edit a recipe
* I have tried and friends by using different devices and screens to edit a recipe by changing it recipes and re save it to the database, a friend point out the data was not retrieving from the database, which are: Ingredients,
Preparation Steps and Required Tools. This we resolved by adding recipes collection and field name: 
```
{{recipe.ingredients}}
{{recipe.preparation_steps}}
{{recipe.required_tools}}
```
In addtion of cuisine was return null value when the user dose not re select it, this was fixed by disbley the current cuisine by added selected to the current cuisine value.
Also, redirect to get_recipes was not working. Deitals below in the (Redirect after Adding Editing and Deleting).

### Delete a recipe
* I tried  and friends by using different devices and screens to delete a recipe from the database and delete a cuisine and it was deleted from the database collections with no error, but redirect to get_recipes was not working. 
Deitals below in the (Redirect after Adding Editing and Deleting).

### Search for recipe
* I have tried and friends by using different devices and screens (see devices below) to search for more than one recipe by it's cuisines or recipes name, search function did not display match list of recipes when search by cuisine.
Found mismatch in search_cuisine vs search_by_cuisine in recipebycuisine.html {% for recipe in search_cuisine %}. 
For user convenient, upper method was added when cuisine is added to match search input.
Also have added print() to print the search out come., which is been removed from the code later. Tested by search for all recipes as French cuisine, all recipes related to that cuisine was listed successfully. Aslo, by recipes name, and it was listed successfully.

### Redirect after Adding Editing and Deleting
* After were a recipe / cuisine added editied or deleted, the app was not redirect to get_recipe page, insted was showing error (the site can't be reached) - bug fixed: re-set host to 0.0.0.0 and remove PORT 3000 for redirects to work. 
Tested by Edit a recipe, and the app successfully redirected to get_recipe page (Main page).
```
if __name__ == '__main__':
    app.run(host='0.0.0.0',
            port=(os.environ.get('PORT')),
            debug=True)
```
### Full width background and about
Background was giving 100% width, and the text was centre by using flex box. By giving relative position to the background and absolute position to the text, text is responsive at the centre of the background image across all screen sizes. 
This was tested by testing it on different screen sizes.

### Devices Tested
* Galaxy s5
* iPhone 6/7/8
* iPhone 6/7/8 Plus
* iPhone X
* iPad
* Desktop MacBook Pro

* Browsers: Chrome, Safari, Firefox, and Microsoft Edge. Also, Chrome Dev Tools: I used Chrome Tools to run test my code and debugging it through out the coding and building the application. Also, try texting different screen sizes.

### Code validator
* HTML: I ran html code on w3 html validator:
1. Warning: Consider adding a lang attribute to the html start tag to declare the language of this document. Been modified accordingly.
2. Error: Bad value {{url_for('static',filename='css/style.css')}} for attribute href on element link: Illegal character in path segment: { is not allowed.
3. Warning: The type attribute is unnecessary for JavaScript resources.Been modified accordingly.

* CSS: I ran html code on w3 validator No Error Found.

* Javascript: I ran html code on codebeautify.org/jsvalidate No Error Found.

* Python3: Checked app.py code for [PEP8](http://pep8online.com) requirements. 

## Deployment

### To Github
1. Create a new repository on GitHub. To avoid errors, I did not initialize the new repository with README, license, or gitignore files. I added these files after my project has been pushed to GitHub.
2. Open Terminal on MacBook Pro.
3. Change the current working directory to my local project.
4. Initialize the local directory as a Git repository, by:
  ```
  git init
  ```
5. Added the files in my new local repository. This stages them for the first commit, by:
```
$ git add fileName
```
6. Commit the files that I have staged in my local repository, by:
```
$ git commit -m "First commit"
```
7. At the top of my GitHub repository's, I copy the remote repository URL.
8. In Terminal, added the URL for the remote repository where my local repository will be pushed, by:
```
$ git remote add origin remote https://github.com/Tariqalrehily/whatocook
```
9. Push the changes in my local repository to GitHub Master branch, by:
```
$ git push -u origin master
```

* After, I will do this to commit and push my projects changes and keep my GitHub repository up to date.

### From Github
* To run this one page app locally:
1. On GitHub, navigate to the main page of the repository.
2. Under the repository name, click Clone or download.
3. In the Clone with HTTPs section, click  to copy the clone URL for the repository.
4. Open Terminal.
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type git clone, and then paste the URL you copied in Step 2. URL (https://github.com/Tariqalrehily/whatocook)
7. Press Enter. Your local clone will be created.

### Deploy To Heroku
There are four things needed in order to push our code to Heroku.
1. Create a requirements.txt file, which contains a list of our dependencies.
2. Create a Procfile, which tells Heroku how to run our project. By adding web: python app.py to the file and including it in our deployment
3. Created a Heroku whatocook app.
4. Linked the local Git repository to Heroku to enable auto deployment. 
5. Choose bransh (master) and start depolying. [whatocook link](https://whatocook.herokuapp.com/)

## Credit
1. Center content (e.g full width text): from [W3.org](https://www.w3.org/Style/Examples/007/center.en.html)

## Media
1. Background image: from Pexels.com by [Pixabay](https://www.pexels.com/photo/blaze-blue-blur-bright-266896/)

## Acknowledgement
* To my mentor Anthony Ngene provided me guides and the Tutor team for their help and advises.

## Disclaimer
* The materials on this application is currently for educational and entertainment purposes only.  
