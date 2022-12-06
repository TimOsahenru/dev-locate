# Welcome to dev-locate
A platform where developers can signup with their projects on display and hiring managers can make searches of developers based on location, year of experience, tech stack or any other search query.


# Install requirements
+ Django. `pip install django` version 4.1 was used for this project

+ django-environ for environment variables `pip install django-environ`

+ `pip install Pillow`  which is a library for image processing.
+ `pip install black` for standard code formatting

Alternatively you can install all the dependencies from the `requirements.txt` file by running this command on your terminal

`pip install -r requirements.txt`


# Developer setup
+ Create a `.env` file inside your `config` repository, then create a variable called `SECRET_KEY` inside the `.env` file

+ Generate your secret key by running the command below on your terminal

`python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'`

+ Copy the generated secret key and paste inside the `.env` file you created like this

`SECRET_KEY='Yourgeneratedsecretkeywithoutanyspace'`