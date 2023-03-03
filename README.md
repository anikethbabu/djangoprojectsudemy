# djangoprojectsudemy

### Templates
In django uses the MVT archeticture. M stands for model, V stands for views, and T stand for Templates. In the base directory for the product you can create templates folder and then create folders specifying which app it comes from. In settings.py make sure to go to templates variable and in the DIRS list add directorys which your templates are stored. In views create a function that returns the function render with the parameters request and the html template path. In urls add the URL and import the views function and add that into the path function in URL patterns list.

### Template_Tags
The django can render on the UI using DTL(Django template library). In the template if you write {{variable}} in the html file it will replace it with a the views variable. {% tagName %} specifies the specific template tag. {% x extends y %} extends one template to another. {% if condition %} can be used for if statements in the template. To pass data to a html template pass a variable in the render function in views.py.

### Static Files
To set up static files create a static files directory right under your project directory. Then in find the static variable and under that create a STATICFILES_DIRS variable and in the list add the directory for the static files. To load static files and use them in a template at the beginning of the file put the {% static %} tag. To load the specific file directory use {% static 'path to file' %} when provided the path provide it like you are already in the static directory.

### Database
The first step in setting up a database in django is to go to settings.py and go to the database variable and make apporiate connection based on the database. More info here : https://docs.djangoproject.com/en/4.1/ref/databases/. <br>
Then create models in the models.py file. The models are the tables in the database. The models are created by creating a class and inheriting from the models.Model class. Then create the fields for the model. The fields are the columns in the table. The fields are created by creating a variable and setting it equal to the field type. <br>
After you have updated the models.py file to create the migrations for the models run command : 
```
python manage.py makemigrations
```
To migrate the models to the database run: 
```
python manage.py migrate
```
### Django Orm
The django orm can be used to query the database. To query the database use the model name and then the field name. To get all the objects in the database use the model name and then the all() function. There are many other functions that can be used to query the database. A link to the documentation is here : https://docs.djangoproject.com/en/4.1/topics/db/queries/. <br>
Django orm has some various process to filter gt(greater than), gte(greater than or equal to), lt(less than), lte(less than or equal to), contains(contains the string), startswith(starts with the string), endswith(ends with the string), in(contains the value), and range(contains the range of values). <br>
Using values_list,values, or only function you can get the values of multiple fields in a database. Only by default also provides the id field. 
Using aggregate Function you can get the aggregate values of the fields. Aggregate functions are count, max, min, avg, and sum. <br>