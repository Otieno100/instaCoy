### Project Description
This is a clone of the popular instagram app built using Python - Django.

Users can sign in to the application to start using.
Users can upload pictures to the application.
They can also See their profile with all their pictures.
Users can Like a picture and leave a comment on it.

#### Getting Started
To clone the repository, run:

Then navigating to the cloned directory:

cd instagram
Prerequisite
This Instagram Clone project requires a prerequisite understanding of the following:

Django Framework
Python3.9
Postgres
Python virtualenv
Setup and installation
Activate virtual environment
Activate virtual environment using python3.9 as default handler virtualenv -p /usr/bin/python3.9 genv && source genv/bin/activate

Install dependancies
Install dependancies that will create an environment for the app to run pip3 install -r requirements.txt

Create the Database
- psql
- CREATE DATABASE instagram;
.env file
Create .env file and paste paste the following filling where appropriate:

SECRET_KEY = '<Secret_key>'
DBNAME = 'instagram'
USER = '<Username>'
PASSWORD = '<password>'
DEBUG = True
Run initial Migration
python3 manage.py makemigrations instagram
python3 manage.py migrate
Run the app
python3 manage.py runserver
Open terminal on localhost:8000
Deployment
The application is deployed on Heroku and is live on this link:



Built With
Django 4.0.5 - Back end logic of the application.
Material Design Bootstrap - Used for overall design and responsive site
Pillow 9.1.1 - Used for image uploads.
Contributing
Please read CONTRIBUTING.md for details on our code of conduct, and the process for submitting pull requests to us.

Author
    Brian Otieno
License
MIT License

Copyright (c) 2022 Brian Otieno

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

About
Instagram clone using Django framework

instagram-ms.herokuapp.com/
Resources
 Readme
License
 MIT license
Stars
 0 stars
Watchers
 1 watching
Forks
 0 forks
Releases
No releases published
Packages
No packages published
Languages
HTML
61.1%
 
Python
37.4%
 
CSS
1.5%