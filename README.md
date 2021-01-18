# Flask test project

this project hosts a flask application wich main functionality is storing the first 150 users of github in a SQLite database, the data of the users is obtained from the github api, and listing them in the browser, the list of data is paginated, the user can navigate between pages and select the amount of entries to list per page.

the style of the page uses basic bootstrap css and to retrieve  data from the database the package Flask-SQLAlchemy was used to make things simpler and more readable

# Requirements

The project was developed using python 3 and virtual environments, the next list is the content of the requirements file for the most part the listed packages are dependencies of Flask.

	attrs==20.3.0
	certifi==2020.12.5
	chardet==4.0.0
	click==7.1.2
	Flask==1.1.2
	Flask-SQLAlchemy==2.4.4
	gunicorn==20.0.4
	idna==2.10
	iniconfig==1.1.1
	itsdangerous==1.1.0
	Jinja2==2.11.2
	MarkupSafe==1.1.1
	packaging==20.8
	pluggy==0.13.1
	py==1.10.0
	pyparsing==2.4.7
	pytest==6.2.1
	requests==2.25.1
	SQLAlchemy==1.3.22
	toml==0.10.2
	urllib3==1.26.2
	Werkzeug==1.0.1


# Running the code
the project has two main programs one is `seed.py`  and the other `server.py`

## Virutal enviroment
The code can be tested locally using virtual environments, to create one and install the dependencies use:

	virtualenv env
	source env/bin/activate
	pip3 install -r requirements.txt

## `seed.py`
This file is responsible of retrieving the users from github and storing them in the SQLite database called `users.db`and the program can be run as follows:

	python3 seed.py
	python3 seed.py 300
The argument of the program is an integer and it represents the number of users to retrieve from github, when no parameter is passed the default is 150.

## `server.py`

This file starts the Flask application, and receives the same arguments as `seed.py` the intention of this is to create and load the database before flask is runned, this is with the aim to make the testing of the application easier, but can be disabled with minor changes to the code.

The Flask application can be started as follows:

	python3 server
	python3 server 300
The argument of the program is an integer and it represents the number of users to retrieve from github, when no parameter is passed the default is 150.

## Project structure
```
/GHusers
		/seed.py
		/server.py
		/setup.py
		/app
			/__init__.py
			/views.py
			/models.py
			/static/
				/css/
					/main.css
			/templates/
				/base.html
				/index.html
		/requirements.txt
		/test_app.py
		/env
```
`seed.py`: This script stores the github users in the SQLite database.
`server.py`: Starts the Flask project.
`setup.py`: Configures the Flask project.
`__init__.py`: Instantiates the Flask app.
`views.py`: Stores the views of the project (in this case just the list of users and index).
`models.py`: Definitions the ORM representations of the database.
`main.css`: css of the project, in this case it's empty because everything uses bootstrap.
`base.html`: Base template for the html views.
`index.html`: Html view to list the pagination of the users.
`requirements.txt`: List of dependencies of the project.
`test_app.py`: Basic testing of the project.
`env/`: Python virtual environment folder.
