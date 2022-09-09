# (289) 0x02. AirBnB clone - MySQL
Foundations > Higher-level programming > AirBnB clone

---

### Project author
Guillaume Salva

### Assignment dates
08-07-2020 to 08-14-2020

### Description
First of three projects building the second iteration of a website cloning the basic features of the [`airbnb.com` main page, circa 2014-2017](https://web.archive.org/web/20170206112507/https://www.airbnb.com/).

Review of Object Relational Mapping from [`holbertonschool-higher_level_programming`](https://github.com/allelomorph/holbertonschool-higher_level_programming/). Building a MySQL database as a second storage engine accessible from our back end Python console.

## General requirements

### Python
* Interpreter conditions:
  * Ubuntu 14.04 LTS
  * python3 (version 3.4.3)
* First line of executable scripts will be `#!/usr/bin/python3`
* Compliance with linter:
  * `pep8` (version 1.7.*) (now known as `pycodestyle`)
* Docstrings are expected to follow the [Google style guide](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html):
  * Per module (`python3 -c 'print(__import__("my_module").__doc__)'`)
  * Per class (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
  * Per function
    * both inside a class (`python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`)
    * and outside a class (`python3 -c 'print(__import__("my_module").my_function.__doc__)'`)
* Test scripts will typically not be in same directory as the task solutions, use `export PYTHONPATH='.'` before running test scripts from project directory to allow includes
* Unit tests will be required on some projects:
  * using the [unittest module](https://docs.python.org/3.4/library/unittest.html#module-unittest)
  * located in a `tests/` folder, with a file structure mimicing that of your project, but with a `test_` prefix added to all file/directory names
  * tests should be capable of being run with `python3 -m unittest discover tests`, or individually per file with `python3 -m unittest <test file>`

### SQL
* `.sql` file comments prefixed with `-- `
* SQL keywords should be capitalized
* Interpreter conditions:
  * Ubuntu 14.04 LTS
  * mysql Ver 14.14 Distrib 5.7.8-rc, for Linux (x86_64) using EditLine wrapper
  * SQLAlchemy version 1.2.5

### Use of MySQL
* `sudo apt install mysql-server` to install
* Interactive mode with `sudo mysql`, non-interactive with:
```bash
$ service mysql start
$ cat <script> | mysql -uroot -p
```
* Import a SQL dump:
```bash
$ echo "CREATE DATABASE <database>;" | mysql -uroot -p
$ curl <dump_file_uri> -s | mysql -uroot -p <database>
```

### Environmental Variables
* `HBNB_ENV`: running environment, can be `dev` or `test` (eventually `production`)
* `HBNB_MYSQL_USER`: the username of your MySQL
* `HBNB_MYSQL_PWD`: the password of your MySQL
* `HBNB_MYSQL_HOST`: the hostname of your MySQL
* `HBNB_MYSQL_DB`: the database name of your MySQL
* `HBNB_TYPE_STORAGE`: the type of storage used, can be `file` (using `FileStorage`) or `db` (using `DBStorage`)

---

## Mandatory Tasks

### :white_check_mark: 0. Fork me if you can!
In the industry, you will work on an existing codebase 90% of the time. Your first thoughts upon looking at it might include:
* “Who did this code?”
* “How does this work?”
* “Where are the unit tests?”
* “Where is this?”
* “Why did they do that like this?”
* “I don’t understand anything.”
* “… I will refactor everything…”

But the worst thing you could possibly do is to **redo everything**. Please don’t do that! **Note: the existing codebase might be perfect, or it might have errors. Don’t always trust the existing codebase!**

For this project you will fork this [codebase](https://github.com/justinmajetich/AirBnB_clone):
* update the repository name to `AirBnB_clone_v2`
* update the `README.md` with your information but **don’t delete the initial authors**

If you are the owner of this repository, please create a new repository named `AirBnB_clone_v2` with the same content of `AirBnB_clone`

### :white_large_square: 1. Bug free!
Do you remember the `unittest` module?

This codebase contains many test cases. Some are missing, but the ones included cover the basic functionality of the program.
```bash
~/AirBnB_v2$ python3 -m unittest discover tests 2>&1 /dev/null | tail -n 1
OK
~/AirBnB_v2$ 
```
All your unittests **must** pass without any errors at anytime in this project, **with each storage engine!** Same for the PEP8 linter.
```bash
~/AirBnB_v2$ HBNB_ENV=test HBNB_MYSQL_USER=hbnb_test HBNB_MYSQL_PWD=hbnb_test_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_test_db HBNB_TYPE_STORAGE=db python3 -m unittest discover tests 2>&1 /dev/null | tail -n 1
OK
~/AirBnB_v2$ 
```
Some tests won’t be relevant for some type of storage, please skip them by using the `skipIf` feature of the [Unittest module - 26.3.6 Skipping tests and expected failures](https://docs.python.org/3/library/unittest.html#skipping-tests-and-expected-failures). Of course, the number of tests must be higher than the current number of tests, so if you decide to skip a test, you should write a new test!

**How to test with MySQL?**

First, you create a specific database for it (next tasks). After, you have to remember what the purpose of an unittest?

**Assert a current state (objects/data/database), do an action, and validate this action changed (or not) the state of your objects/data/database**

For example, “you want to validate that the `create State name="California"` command in the console will add a new record in your table `states` in your database”, here steps for your unittest:
* get the number of current records in the table `states` (my using a `MySQLdb` for example - but not SQLAlchemy (remember, you want to test if it works, so it’s better to isolate from the system))
* execute the console command
* get (again) the number of current records in the table `states` (same method, with `MySQLdb`)
* if the difference is `+1` => test passed

### :white_large_square: 2. Console improvements
Update the `def do_create(self, arg):` function of your command interpreter (`console.py`) to allow for object creation with given parameters:

* Command syntax: `create <Class name> <param 1> <param 2> <param 3>...`
* Param syntax: `<key name>=<value>`
* Value syntax:
    * String: `"<value>"` => starts with a double quote
        * any double quote inside the value must be escaped with a backslash `\`
        * all underscores `_` must be replace by spaces ` `. Example: You want to set the string `My little house` to the attribute `name`, your command line must be `name="My_little_house"`
    * Float: `<unit>.<decimal>` => contains a dot .
    * Integer: `<number>` => default case
* If any parameter doesn’t fit with these requirements or can’t be recognized correctly by your program, it must be skipped

**Don’t forget to add tests for this new feature!**

Also, this new feature will be tested here only with `FileStorage` engine.

File(s): [`console.py`](./console.py) [`models/`](./models/) [`tests/`](./tests/)

### :white_check_mark: 3. MySQL setup development
Write a script that prepares a MySQL server for the project:
* A database `hbnb_dev_db`
* A new user `hbnb_dev` (in `localhost`)
* The password of `hbnb_dev` should be set to `hbnb_dev_pwd`
* `hbnb_dev` should have all privileges on the database `hbnb_dev_db` (and **only this database**)
* `hbnb_dev` should have `SELECT` privilege on the database `performance_schema` (and **only this database**)
* If the database `hbnb_dev_db` or the user `hbnb_dev` already exists, your script should not fail

File(s): [`setup_mysql_dev.sql`](./setup_mysql_dev.sql)

### :white_check_mark: 4. MySQL setup test
Write a script that prepares a MySQL server for the project:
* A database `hbnb_test_db`
* A new user `hbnb_test` (in `localhost`)
* The password of `hbnb_test` should be set to `hbnb_test_pwd`
* `hbnb_test` should have all privileges on the database `hbnb_test_db` (and **only this database**)
* `hbnb_test` should have `SELECT` privilege on the database `performance_schema` (and **only this database**)
* If the database `hbnb_test_db` or the user `hbnb_test` already exists, your script should not fail

File(s): [`setup_mysql_test.sql`](./setup_mysql_test.sql)

### :white_check_mark: 5. Delete object
Update `FileStorage`: (`models/engine/file_storage.py`)
* Add a new public instance method: `def delete(self, obj=None):` to delete `obj` from `__objects` if it’s inside - if `obj` is equal to `None`, the method should not do anything
* Update the prototype of `def all(self)` to `def all(self, cls=None)` - that returns the list of objects of one type of class. Example below with `State` - it’s an optional filtering

File(s): [`models/engine/file_storage.py`](./models/engine/file_storage.py)

### :white_large_square: 6. DBStorage - States and Cities
SQLAlchemy will be your best friend!

It’s time to change your storage engine and use `SQLAlchemy`

In the following steps, you will make multiple changes:
* the biggest one is the transition between `FileStorage` and `DBStorage`: In the industry, you will never find a system who can work with both in the same time - but you will find a lot of services who can manage multiple storage systems. (for example, logs service: in memory, in disk, in database, in ElasticSearch etc…) - The main concept behind is the **abstraction**: Make your code running without knowing how it’s stored.
* add attributes for SQLAlchemy: they will be class attributes, like previously, with a “weird” value. Don’t worry, these values are for description and mapping to the database. If you change one of these values, or add/remove one attribute of the a model, you will have to delete the database and recreate it in SQL. (Yes it’s not optimal, but for development purposes, it’s ok. In production, we will add “migration mechanism” - for the moment, don’t spend time on it.)

Please follow all these steps:

Update `BaseModel`: (`models/base_model.py`)
* Create `Base = declarative_base()` before the class definition of `BaseModel`
* **Note! `BaseModel` does not inherit from `Base`. All other classes will inherit from `BaseModel` to get common values (`id`, `created_at`, `updated_at`), where inheriting from Base will actually cause SQLAlchemy to attempt to map it to a table.**
* Add or replace in the class `BaseModel`:
    * class attribute `id`
        * represents a column containing a unique string (60 characters)
        * can’t be null
        * primary key
    * class attribute `created_at`
        * represents a column containing a datetime
        * can’t be null
        * default value is the current datetime (use `datetime.utcnow()`)
    * class attribute `updated_at`
        * represents a column containing a datetime
        * can’t be null
        * default value is the current datetime (use `datetime.utcnow()`)
* Move the `models.storage.new(self)` from `def __init__(self, *args, **kwargs):` to `def save(self):` and call it just before `models.storage.save()`
* In `def __init__(self, *args, **kwargs):`, manage `kwargs` to create instance attribute from this dictionary. Ex: `kwargs={ 'name': "California" }` => `self.name` = "California"` if it’s not already the case
* Update the `to_dict()` method of the class `BaseModel`:
    * remove the key `_sa_instance_state` from the dictionary returned by this method **only if this key exists**
* Add a new public instance method: `def delete(self):` to delete the current instance from the storage (`models.storage`) by calling the method `delete`

Update City: (`models/city.py`)
* `City` inherits from `BaseModel` and `Base` (respect the order)
* Add or replace in the class `City`:
    * class attribute `__tablename__` -
        * represents the table name, `cities`
    * class attribute `name`
        * represents a column containing a string (128 characters)
        * can’t be null
    * class attribute `state_id`
        * represents a column containing a string (60 characters)
        * can’t be null
        * is a foreign key to `states.id`

Update State: (`models/state.py`)
* `State` inherits from `BaseModel` and `Base` (respect the order)
* Add or replace in the class `State`:
    * class attribute `__tablename__`
        * represents the table name, `states`
    * class attribute `name`
        * represents a column containing a string (128 characters)
        * can’t be null
    * for `DBStorage`: class attribute `cities` must represent a relationship with the class `City`. If the `State` object is deleted, all linked `City` objects must be automatically deleted. Also, the reference from a `City` object to his `State` should be named `state`
    * for `FileStorage`: getter attribute `cities` that returns the list of `City` instances with `state_id` equals to the current `State.id` => It will be the `FileStorage` relationship between `State` and `City`

New engine DBStorage: (`models/engine/db_storage.py`)
* Private class attributes:
    * `__engine`: set to `None`
    * `__session`: set to `None`
* Public instance methods:
    * `__init__(self)`:
        * create the engine (`self.__engine`)
        * the engine must be linked to the MySQL database and user created before (`hbnb_dev` and `hbnb_dev_db`):
            * dialect: `mysql`
            * driver: `mysqldb`
        * all of the following values must be retrieved via environment variables:
            * MySQL user: `HBNB_MYSQL_USER`
            * MySQL password: `HBNB_MYSQL_PWD`
            * MySQL host: `HBNB_MYSQL_HOST` (here = `localhost`)
            * MySQL database: `HBNB_MYSQL_DB`
        * don’t forget the option `pool_pre_ping=True` when you call `create_engine`
        * drop all tables if the environment variable `HBNB_ENV` is equal to `test`
    * `all(self, cls=None)`:
        * query on the current database session (`self.__session`) all objects depending of the class name (argument `cls`)
        * if `cls=None`, query all types of objects (`User`, `State`, `City`, `Amenity`, `Place` and `Review`)
        * this method must return a dictionary: (like `FileStorage`)
            * key = `<class-name>.<object-id>`
            * value = object
    * `new(self, obj)`: add the object to the current database session (`self.__session`)
    * `save(self)`: commit all changes of the current database session (`self.__session`)
    * `delete(self, obj=None)`: delete from the current database session `obj` if not `None`
    * `reload(self)`:
        * create all tables in the database (feature of SQLAlchemy) (WARNING: all classes who inherit from `Base` must be imported before calling `Base.metadata.create_all(engine)`)
        * create the current database session (`self.__session`) from the engine (`self.__engine`) by using a [sessionmaker](https://docs.sqlalchemy.org/en/13/orm/session_api.html) - the option `expire_on_commit` must be set to `False`; and [scoped_session](https://docs.sqlalchemy.org/en/13/orm/contextual.html) - to make sure your Session is thread-safe

Update `__init__.py`: (`models/__init__.py`)
* Add a conditional depending of the value of the environment variable `HBNB_TYPE_STORAGE`:
    * If equal to `db`:
        * Import `DBStorage` class in this file
        * Create an instance of `DBStorage` and store it in the variable `storage` (the line `storage.reload()` should be executed after this instantiation)
    * Else:
        * Import `FileStorage` class in this file
        * Create an instance of `FileStorage` and store it in the variable `storage` (the line `storage.reload()` should be executed after this instantiation)
* This “switch” will allow you to change storage type directly by using an environment variable

File(s): [`models/base_model.py`](./models/base_model.py) [`models/city.py`](./models/city.py) [`models/state.py`](./models/state.py) [`models/engine/db_storage.py`](./models/engine/db_storage.py) [`models/__init__.py`](./models/__init__.py)

### :white_check_mark: 7. DBStorage - User
Update `User`: (`models/user.py`)
* `User` inherits from `BaseModel` and `Base` (respect the order)
* Add or replace in the class `User`:
    * class attribute `__tablename__`
        * represents the table name, `users`
    * class attribute `email`
        * represents a column containing a string (128 characters)
        * can’t be null
    * class attribute `password`
        * represents a column containing a string (128 characters)
        * can’t be null
    * class attribute `first_name`
        * represents a column containing a string (128 characters)
        * can be null
    * class attribute `last_name`
        * represents a column containing a string (128 characters)
        * can be null

File(s): [`models/user.py`](./models/user.py)

### :white_large_square: 8. DBStorage - Place
Update `Place`: (`models/place.py`)
* `Place` inherits from `BaseModel` and `Base` (respect the order)
* Add or replace in the class `Place`:
    * class attribute `__tablename__`
        * represents the table name, `places`
    * class attribute `city_id`
        * represents a column containing a string (60 characters)
        * can’t be null
        * is a foreign key to `cities.id`
    * class attribute `user_id`
        * represents a column containing a string (60 characters)
        * can’t be null
        * is a foreign key to `users.id`
    * class attribute `name`
        * represents a column containing a string (128 characters)
        * can’t be null
    * class attribute `description`
        * represents a column containing a string (1024 characters)
        * can be null
    * class attribute `number_rooms`
        * represents a column containing an integer
        * can’t be null
        * default value: 0
    * class attribute `number_bathrooms`
        * represents a column containing an integer
        * can’t be null
        * default value: 0
    * class attribute `max_guest`
        * represents a column containing an integer
        * can’t be null
        * default value: 0
    * class attribute `price_by_night`
        * represents a column containing an integer
        * can’t be null
        * default value: 0
    * class attribute `latitude`
        * represents a column containing a float
        * can be null
    * class attribute `longitude`
        * represents a column containing a float
        * can be null

Update `User`: (`models/user.py`)
* Add or replace in the class `User`:
    * class attribute `places` must represent a relationship with the class `Place`. If the `User` object is deleted, all linked `Place` objects must be automatically deleted. Also, the reference from a `Place` object to its `User` should be named `user`

Update City: (models/city.py)
* Add or replace in the class `City`:
    * class attribute `places` must represent a relationship with the class `Place`. If the `City` object is deleted, all linked `Place` objects must be automatically deleted. Also, the reference from a `Place` object to his `City` should be named `cities`

File(s): [`models/place.py`](./models/place.py) [`models/user.py`](./models/user.py) [`models/city.py`](./models/city.py)

### :white_check_mark: 9. DBStorage - Review
Update `Review`: (`models/review.py`)
* `Review` inherits from `BaseModel` and `Base` (respect the order)
* Add or replace in the class `Review`:
    * class attribute `__tablename__`
        * represents the table name, `reviews`
    * class attribute `text`
        * represents a column containing a string (1024 characters)
        * can’t be null
    * class attribute `place_id`
        * represents a column containing a string (60 characters)
        * can’t be null
        * is a foreign key to `places.id`
    * class attribute `user_id`
        * represents a column containing a string (60 characters)
        * can’t be null
        * is a foreign key to `users.id`

Update `User`: (`models/user.py`)
* Add or replace in the class `User`:
    * class attribute `reviews` must represent a relationship with the class `Review`. If the `User` object is deleted, all linked `Review` objects must be automatically deleted. Also, the reference from a `Review` object to its `User` should be named `user`

Update `Place`: (`models/place.py`)
* for `DBStorage`: class attribute `reviews` must represent a relationship with the class `Review`. If the `Place` object is deleted, all linked `Review` objects must be automatically deleted. Also, the reference from a `Review` object to its `Place` should be named `place`
* for `FileStorage`: getter attribute reviews that returns the list of `Review` instances with `place_id` equals to the current `Place.id` => It will be the `FileStorage` relationship between `Place` and `Review`

File(s): [`models/review.py`](./models/review.py) [`models/user.py`](./models/user.py) [`models/place.py`](./models/place.py)

### :white_check_mark: 10. DBStorage - Amenity... and BOOM!
Update `Amenity`: (`models/amenity.py`)
* `Amenity` inherits from `BaseModel` and `Base` (respect the order)
* Add or replace in the class `Amenity`:
    * class attribute `__tablename__`
        * represents the table name, `amenities`
    * class attribute `name`
        * represents a column containing a string (128 characters)
        * can’t be null
    * class attribute `place_amenities` must represent a relationship [Many-To-Many](https://docs.sqlalchemy.org/en/13/orm/basic_relationships.html) between the class `Place` and `Amenity`. Please see below more detail: `place_amenity` in the `Place` update

Update `Place`: (`models/place.py`)
* Add an instance of [SQLAlchemy Table](https://docs.sqlalchemy.org/en/13/core/metadata.html) called `place_amenity` for creating the relationship [Many-To-Many](https://docs.sqlalchemy.org/en/13/orm/basic_relationships.html) between `Place` and `Amenity`:
    * table name `place_amenity`
    * `metadata = Base.metadata`
    * 2 columns:
        * `place_id`, a string of 60 characters foreign key of `places.id`, primary key in the table and never null
        * `amenity_id`, a string of 60 characters foreign key of `amenities.id`, primary key in the table and never null
* Update `Place` class:
    * for `DBStorage`: class attribute `amenities` must represent a relationship with the class `Amenity` but also as `secondary` to `place_amenity` with option `viewonly=False` (`place_amenity` has been define previously)
    * for `FileStorage`:
        * Getter attribute `amenities` that returns the list of `Amenity` instances based on the attribute `amenity_ids` that contains all `Amenity.id` linked to the `Place`
        * Setter attribute `amenities` that handles `append` method for adding an `Amenity.id` to the attribute `amenity_ids`. This method should accept only `Amenity` object, otherwise, do nothing.

**What’s a Many-to-Many relationship?**

In our system, we don’t want to duplicate amenities (for example, having 10000 time the amenity `Wifi`), so they will be unique. But, at least 2 places can have the same amenity (like `Wifi` for example). We are in the case of:
* an amenity can be linked to multiple places
* a place can have multiple amenities

= Many-To-Many

To make this link working, we will create a third table called `place_amenity` that will create these links.

And you are good, you have a new engine!

File(s): [`models/amenity.py`](./models/amenity.py) [`models/place.py`](./models/place.py)

---

## Student team
* **Samuel Pomeroy** - [allelomorph](github.com/allelomorph)
* **Trevor Stevenson** - [Tr3v1n4t0r](github.com/Tr3v1n4t0r)
