# djangoprojectsudemy

### Templates
In django uses the MVT archeticture. M stands for model, V stands for views, and T stand for Templates. In the base directory for the product you can create templates folder and then create folders specifying which app it comes from. In settings.py make sure to go to templates variable and in the DIRS list add directorys which your templates are stored. In views create a function that returns the function render with the parameters request and the html template path. In urls add the URL and import the views function and add that into the path function in URL patterns list.
