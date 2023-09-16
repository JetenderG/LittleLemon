# LittleLemon

## Description

The application is the barebones for a working restaurant app.

Application can:

    1. serve static content
    2. able to do CRUD methods on both  Menu 
    3. Create a basic account 
    4. Able to view booking list 

    Note need to be authenticated to do the CRUD methods besides get for menu

## Setup the Application

1. First update the *DATABASES* object in the setting.py in your project folder to correspond to yours

2. Next make a virtual environment to test the application using python env

3. After that install all the dependencies using pip3 or pip install

4. Then run python manage.py makemigrations and python manage.py migrate

5. Lastly run the server using python manage.py runserver and the applicaton will then run

## Application Urls

Access the Django's panel

>http://127.0.0.1:8000/admin/
----

Homepage of restaurant

>http://127.0.0.1:8000/restaurant/
----

Booking for user (access is only for users with crendentials)

>'http://127.0.0.1:8000/restaurant/booking/tables/'
----

Can use CRUD method on specfic table based on id number. For example this url view table with the id of 1

>'http://127.0.0.1:8000/restaurant/booking/tables/1'
----

List of menu items
(able to add menu item through use of url or django panel)

>'http://127.0.0.1:8000/restaurant/menu/'
----

Looks up a menu item based on id. Below for example is using the id 1

>http://127.0.0.1:8000/restaurant/menu/1
----

Creating account requires a user name and password.

    Must make a post request to url with a password and username.
    This can be done from the Django's Browserable API or through a use of API client testing software like Insomia  

    http://localhost:8000/auth/users/   
----

You can get a tokin from making a post request using your username and password if already registered

    http://localhost:8000/token/login/   
----


You can look at more of djoser url on their site on 
    [https://djoser.readthedocs.io/en/latest/index.html]