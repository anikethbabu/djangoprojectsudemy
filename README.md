# djangoprojectsudemy

### Templates
In django uses the MVT archeticture. M stands for model, V stands for views, and T stand for Templates. In the base directory for the product you can create templates folder and then create folders specifying which app it comes from. In settings.py make sure to go to templates variable and in the DIRS list add directorys which your templates are stored. In views create a function that returns the function render with the parameters request and the html template path. In urls add the URL and import the views function and add that into the path function in URL patterns list.

### Template_Tags
The django can render on the UI using DTL(Django template library). In the template if you write {{variable}} in the html file it will replace it with a the views variable. {% tagName %} specifies the specific template tag. {% x extends y %} extends one template to another. {% if condition %} can be used for if statements in the template. To pass data to a html template pass a variable in the render function in views.py.

### Static Files
To set up static files create a static files directory right under your project directory. Then in find the static variable and under that create a STATICFILES_DIRS variable and in the list add the directory for the static files. To load static files and use them in a template at the beginning of the file put the {% static %} tag. To load the specific file directory use {% static 'path to file' %} when provided the path provide it like you are already in the static directory.