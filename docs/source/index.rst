.. dev-locate documentation master file, created by
   sphinx-quickstart on Thu Dec  8 08:11:39 2022.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to dev-locate's documentation!
======================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`


dev-locate is a platform where developers can sign up with their projects on display and hiring managers can make searches of developers based on location, year of experience, tech stack or any other search query.

Setting up a virtual environment
==================================

The following process describes how to set up a virtual environment before install the dependencies used for this projects
+ `python -m venv venv` to create a virtual environment
+ `venv\Scripts\activate` to activate the virtual environment

Install requirements
=====================

+ Django. `pip install django` version 4.1 was used for this project

+ django-environ for environment variables `pip install django-environ`

+ `pip install Pillow`  which is a library for image processing.
+ `pip install black` for standard code formatting

Alternatively you can install all the dependencies from the `requirements.txt` file by running this command on your terminal

`pip install -r requirements.txt`


Developer setup
=================

+ Create a `.env` file inside your `config` repository, then create a variable called `SECRET_KEY` inside the `.env` file

+ Generate your secret key by running the command below on your terminal

`python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'`

+ Copy the generated secret key and paste inside the `.env` file you created like this

`SECRET_KEY='Yourgeneratedsecretkeywithoutanyspace'`

Using dev-locate as an Engineer
================================

You need to SignUp as a User to be able to create a project but if you're in a haste to check out this application you can log in using `vee@gmail.com`

as your login email and `pycongh22` as your login password.

Creating a project
=====================
To create a project you must be logged in, once you're logged in you'll be redirected to your profile.

.. image:: /images/profile.png
   :scale: 50%

To create your first project visit `My project` tab and click the `create` button

.. image:: /images/public.png
   :scale: 50%


Once a project has been created you can choose to either make it public by checking `make public` or leave it private by not checking.

.. image:: /images/make.png
   :scale: 50%


A private project is only visible to you(the requested user)

To edit a Project(public or private) visit the necessary tab and click on the edit button to make an update

.. image:: /images/edit.jpg
   :scale: 50%

.. warning::
   Warning! Once a project has been deleted it cannot be recovered

To modify your profile settings click on `Account settings` tab and you should be able to do that from here

.. image:: /images/settings.png
   :scale: 50%


Using dev-locate as a Hiring manager
=====================================

As a hiring manager you do not need to create an account to signup you can make searches of developers
from the search bar by either searching by country, tech stack or username

.. image:: /images/index.png
   :scale: 50%


When you click on a project, you will be redirected to a more detailed page about the project, where you can
view the repo of the project or a live url

.. image:: /images/details.png
   :scale: 50%


To contact an Engineer click on `Checkout my profile` in the detailed page you will be redirected

to the profile of the engineer that created that project and also click on the `message` button

you need to create an account tho to send a message

.. image:: /images/profile_b.png
   :scale: 50%

