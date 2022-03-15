# [AWWWARDS]()
#### Web clone for the awwards website
#### By **[Trevin Livele]**

## Description
This is a simple web clone of the awwwwards website. A user can create an account and sign into it. 
The site supports uploading projects, and following other users. 
users can view projects uploaded by other users in the home page of app and rate them.

## Set Up and Installations

### Prerequisites
1. Ubuntu Software
2. Python3.8
3. [Postgres](https://www.postgresql.org/download/)
4. [python virtualenv](https://gist.github.com/Geoyi/d9fab4f609e9f75941946be45000632b)

### Clone the Repo
Run the following command on the terminal:
`git clone git@github.com:trevin-livele/django_api_awwwards.git && cd Awwards`


### Activate virtual environment
Activate virtual environment using python3.8 as default handler
```bash
virtualenv -p /usr/bin/python3.8 venv && source venv/bin/activate
```

### Install dependancies
Install dependancies that will create an environment for the app to run
`pip3 install -r requirements.txt`

### Create the Database
```bash
psql
CREATE DATABASE awwwards;
```
### .env file
Create .env file and paste paste the following filling where appropriate:
```python
SECRET_KEY = '<Secret_key>'
DBNAME = 'awwwards'
USER = '<Username>'
PASSWORD = '<password>'
DEBUG = True

```
### Run initial Migration
```bash
python3.8 manage.py makemigrations
python3.8 manage.py migrate
```

### Run the app
```bash
python3.8 manage.py runserver
```
Open terminal on `localhost:8000`

## Known bugs
not know bugs at the moment
## Technologies used
    - Python 3.8.10
    - HTML
    - Bootstrap 
    - JavaScript
    - Heroku
    - Postgresql

## Support and contact details
Contact me on liveletrevin6@gmail.com for any comments, reviews or advice.

### License
Copyright (c) **Trevin Livele**

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
