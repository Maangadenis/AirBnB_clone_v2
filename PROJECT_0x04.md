# (289) 0x04. AirBnB clone - Web framework
Foundations > Higher-level programming > AirBnB clone

---

### Project author
Guillaume Salva

### Assignment dates
08-31-2020 to 09-03-2020

### Description
Third of three projects building the second iteration of a website cloning the basic features of the [`airbnb.com` main page, circa 2014-2017](https://web.archive.org/web/20170206112507/https://www.airbnb.com/).

Using the Python library Flask along with Jinja templates to create a web framework and application to dynamically display the contents of our storage engines.

### Provided File(s)
* [`7-states_list.sql`](./web_static/tests/7-states_list.sql) [`10-hbnb_filters.sql`](./web_static/tests/10-hbnb_filters.sql) [`100-hbnb.sql`](./web_static/tests/100-hbnb.sql)

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

### HTML / CSS
* Your code should be W3C compliant and validate with [W3C-Validator](https://github.com/holbertonschool/W3C-Validator)
* All your CSS files should be in `styles` folder
* All your images should be in `images` folder
* You are not allowed to use `!important` and `id` (`#...` in the CSS file)
* You are not allowed to use tags `img`, `embed` and `iframe`
* You are not allowed to use Javascript
* Example screenshots taken on Chrome 56
* No cross browsers
* You have to follow all requirements but some `margin`/`padding` are missing - you should try to fit as much as you can to screenshots

### Installing Flask
```bash
$ pip3 install Flask
```

---

## Mandatory Tasks

### :white_check_mark: 0. Hello Flask!
Write a script that starts a Flask web application:
* Your web application must be listening on `0.0.0.0`, port `5000`
* Routes:
    * `/`: display “Hello HBNB!”
* You must use the option `strict_slashes=False` in your route definition

File(s): [`web_flask/0-hello_route.py`](./web_flask/0-hello_route.py) [`web_flask/__init__.py`](./web_flask/__init__.py)

### :white_check_mark: 1. HBNB
Write a script that starts a Flask web application:
* Your web application must be listening on `0.0.0.0`, port `5000`
* Routes:
    * `/`: display `Hello HBNB!`
    * `/hbnb`: display `HBNB`
* You must use the option `strict_slashes=False` in your route definition

File(s): [`web_flask/1-hbnb_route.py`](./web_flask/1-hbnb_route.py)

### :white_check_mark: 2. C is fun!
Write a script that starts a Flask web application:
* Your web application must be listening on `0.0.0.0`, port `5000`
* Routes:
    * `/`: display `Hello HBNB!`
    * `/hbnb`: display `HBNB`
    * `/c/<text>`: display `C ` followed by the value of the text variable (replace underscore `_` symbols with a space )
* You must use the option `strict_slashes=False` in your route definition

File(s): [`web_flask/2-c_route.py`](./web_flask/2-c_route.py)

### :white_check_mark: 3. Python is cool!
Write a script that starts a Flask web application:
* Your web application must be listening on `0.0.0.0`, port `5000`
* Routes:
    * `/`: display `Hello HBNB!`
    * `/hbnb`: display `HBNB`
    * `/c/<text>`: display `C `, followed by the value of the text variable (replace underscore `_` symbols with a space )
    * `/python/(<text>)`: display `Python `, followed by the value of the text variable (replace underscore `_` symbols with a space )
        * The default value of text is `is cool`
* You must use the option `strict_slashes=False` in your route definition

File(s): [`web_flask/3-python_route.py`](./web_flask/3-python_route.py)

### :white_check_mark: 4. Is it a number?
Write a script that starts a Flask web application:
* Your web application must be listening on `0.0.0.0`, port `5000`
* Routes:
    * `/`: display `Hello HBNB!`
    * `/hbnb`: display `HBNB`
    * `/c/<text>`: display `C `, followed by the value of the text variable (replace underscore `_` symbols with a space )
    * `/python/(<text>)`: display `Python `, followed by the value of the text variable (replace underscore `_` symbols with a space )
        * The default value of text is `is cool`
    * `/number/<n>`: display `n is a number` only if `n` is an integer
* You must use the option `strict_slashes=False` in your route definition

File(s): [`web_flask/4-number_route.py`](./web_flask/4-number_route.py)

### :white_check_mark: 5. Number template
Write a script that starts a Flask web application:
* Your web application must be listening on `0.0.0.0`, port `5000`
* Routes:
    * `/`: display “Hello HBNB!`
    * `/hbnb`: display `HBNB`
    * `/c/<text>`: display `C `, followed by the value of the text variable (replace underscore `_` symbols with a space )
    * `/python/(<text>)`: display `Python `, followed by the value of the text variable (replace underscore `_` symbols with a space )
        * The default value of text is `is cool`
    * `/number/<n>`: display `n is a number` only if `n` is an integer
    * `/number_template/<n>`: display a HTML page only if `n` is an integer:
        * `H1` tag: `Number: n` inside the tag BODY
* You must use the option `strict_slashes=False` in your route definition

File(s): [`web_flask/5-number_template.py`](./web_flask/5-number_template.py)  [`web_flask/templates/5-number.html`](./web_flask/templates/5-number.html)

### :white_check_mark: 6. Odd or even?
Write a script that starts a Flask web application:
* Your web application must be listening on `0.0.0.0`, port `5000`
* Routes:
    * `/`: display `Hello HBNB!`
    * `/hbnb`: display `HBNB`
    * `/c/<text>`: display `C `, followed by the value of the text variable (replace underscore `_` symbols with a space )
    * `/python/(<text>)`: display `Python `, followed by the value of the text variable (replace underscore `_` symbols with `a space )
        * The default value of text is `is cool`
    * `/number/<n>`: display `n is a number` only if `n` is an integer
    * `/number_template/<n>`: display a HTML page only if `n` is an integer:
        * `H1` tag: `Number: n` inside the tag `BODY`
    * `/number_odd_or_even/<n>: display a HTML page only if n is an integer:
        * `H1` tag: `Number: n is even|odd` inside the tag `BODY`
* You must use the option `strict_slashes=False` in your route definition

File(s): [`web_flask/6-number_odd_or_even.py`](./web_flask/6-number_odd_or_even.py) [`web_flask/templates/6-number_odd_or_even.html`](./web_flask/templates/6-number_odd_or_even.html)

### :white_check_mark: 7. Improve engines
Before using Flask to display our HBNB data, you will need to update some part of our engine:

Update `FileStorage`: (`models/engine/file_storage.py`)
* Add a public method `def close(self):`: call `reload()` method for deserializing the JSON file to objects

Update `DBStorage`: (`models/engine/db_storage.py`)
* Add a public method `def close(self):`: call `remove()` method on the private session attribute (`self.__session`) [tips](https://docs.sqlalchemy.org/en/13/orm/contextual.html) or `close()` on the class `Session` [tips](https://docs.sqlalchemy.org/en/13/orm/session_api.html)

Update `State`: (`models/state.py`) - If it’s not already present
* If your storage engine is not `DBStorage`, add a public getter method `cities` to return the list of `City` objects from storage linked to the current `State`

File(s): [`models/engine/file_storage.py`](./models/engine/file_storage.py) [`models/engine/db_storage.py`](./models/engine/db_storage.py) [`models/state.py`](./models/state.py)

### :white_check_mark: 8. List of states
Write a script that starts a Flask web application:
* Your web application must be listening on `0.0.0.0`, port `5000`
* You must use `storage` for fetching data from the storage engine (`FileStorage` or `DBStorage`) => `from models import storage and storage.all(...)`
* After each request you must remove the current SQLAlchemy Session:
    * Declare a method to handle `@app.teardown_appcontext`
    * Call in this method `storage.close()`
* Routes:
    * `/states_list`: display a HTML page: (inside the tag `BODY`)
        * `H1` tag: `States`
        * `UL` tag: with the list of all `State` objects present in `DBStorage` sorted by name (A->Z) 
            * `LI` tag: description of one `State`: `<state.id>: <B><state.name></B>`
* Import this [`7-states_list.sql`](`./web_flask/tests/7-states_list.sql`) to have some data
* You must use the option `strict_slashes=False` in your route definition

**IMPORTANT**
* Make sure you have a running and valid `setup_mysql_dev.sql` in your `AirBnB_clone_v2` repository ([task](./PROJECT_0x02.md/#white-check-mark-3-mysql-setup-development))
* Make sure all tables are created when you run `echo "quit" | HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./console.py`

File(s): [`web_flask/7-states_list.py`](./web_flask/7-states_list.py)  [`web_flask/templates/7-states_list.html`](./web_flask/templates/7-states_list.html)

### :white_check_mark: 9. Cities by states
Write a script that starts a Flask web application:
* Your web application must be listening on `0.0.0.0`, port `5000`
* You must use `storage` for fetching data from the storage engine (`FileStorage` or `DBStorage`) => `from models import storage` and `storage.all(...)`
* To load all cities of a `State`:
    * If your storage engine is `DBStorage`, you must use `cities` relationship
    * Otherwise, use the public getter method `cities`
* After each request you must remove the current SQLAlchemy Session:
    * Declare a method to handle `@app.teardown_appcontext`
    * Call in this method `storage.close()`
* Routes:
    * `/cities_by_states`: display a HTML page: (inside the tag `BODY`)
        * `H1` tag: `States`
        * `UL` tag: with the list of all `State` objects present in `DBStorage` sorted by name (A->Z)
            * `LI` tag: description of one `State`: `<state.id>: <B><state.name></B>` + `UL` tag: with the list of `City` objects linked to the `State` sorted by `name` (A->Z)
                * `LI` tag: description of one `City`: <city.id>: <B><city.name></B>`
* Import this [`7-states_list.sql`](`./web_flask/tests/7-states_list.sql`) to have some data
* You must use the option `strict_slashes=False` in your route definition

**IMPORTANT**
* Make sure you have a running and valid `setup_mysql_dev.sql` in your `AirBnB_clone_v2` repository ([task](./PROJECT_0x02.md/#white-check-mark-3-mysql-setup-development))
* Make sure all tables are created when you run `echo "quit" | HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./console.py`

File(s): [`web_flask/8-cities_by_states.py`](./web_flask/8-cities_by_states.py) [`web_flask/templates/8-cities_by_states.html`](./web_flask/templates/8-cities_by_states.html)

### :white_check_mark: 10. States and State
Write a script that starts a Flask web application:
* Your web application must be listening on `0.0.0.0`, port `5000`
* You must use `storage` for fetching data from the storage engine (`FileStorage` or `DBStorage`) => `from models import storage` and `storage.all(...)`
* To load all cities of a `State`:
    * If your storage engine is `DBStorage`, you must use `cities` relationship
    * Otherwise, use the public getter method `cities`
* After each request you must remove the current SQLAlchemy Session:
    * Declare a method to handle `@app.teardown_appcontext`
    * Call in this method `storage.close()`
* Routes:
    * `/states`: display a HTML page: (inside the tag `BODY`)
        * `H1` tag: `States`
        * `UL` tag: with the list of all `State` objects present in `DBStorage` sorted by name (A->Z)
            * `LI` tag: description of one `State`: `<state.id>: <B><state.name></B>`
    * `/states/<id>`: display a HTML page: (inside the tag `BODY`)
        * If a `State` object is found with this `id`:
            * `H1` tag: `State:`
            * `H3` tag: `Cities:`
            * `UL` tag: with the list of `City` objects linked to the `State` sorted by `name` (A->Z)
                * `LI` tag: description of one `City`: `<city.id>: <B><city.name></B>`
        * Otherwise:
            * `H1` tag: `Not found!`
* You must use the option `strict_slashes=False` in your route definition
* Import this [`7-states_list.sql`](`./web_flask/tests/7-states_list.sql`) to have some data

**IMPORTANT**
* Make sure you have a running and valid `setup_mysql_dev.sql` in your `AirBnB_clone_v2` repository ([task](./PROJECT_0x02.md/#white-check-mark-3-mysql-setup-development))
* Make sure all tables are created when you run `echo "quit" | HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./console.py`

File(s): [`web_flask/9-states.py`](./web_flask/9-states.py) [`web_flask/templates/9-states.html`](./web_flask/templates/9-states.html)

### :white_large_square: 11. HBNB filters
Write a script that starts a Flask web application:
* Your web application must be listening on `0.0.0.0`, port `5000`
* You must use `storage` for fetching data from the storage engine (`FileStorage` or `DBStorage`) => `from models import storage` and `storage.all(...)`
* To load all cities of a `State`:
    * If your storage engine is `DBStorage`, you must use `cities` relationship
    * Otherwise, use the public getter method `cities`
* After each request you must remove the current SQLAlchemy Session:
    * Declare a method to handle `@app.teardown_appcontext`
    * Call in this method `storage.close()`
* Routes:
    * `/hbnb_filters`: display a HTML page like `6-index.html`, which was done during the project [0x01. AirBnB clone - Web static](https://github.com/allelomorph/AirBnB_clone/PROJECT_0x01.md)
        * Copy files `3-footer.css`, `3-header.css`, `4-common.css` and `6-filters.css` from `web_static/styles/` to the folder `web_flask/static/styles`
        * Copy files `icon.png` and `logo.png` from `web_static/images/` to the folder `web_flask/static/images`
        * Update `.popover` class in `6-filters.css` to allow scrolling in the popover and a max height of 300 pixels.
        * Use `6-index.html` content as source code for the template `10-hbnb_filters.html`:
            * Replace the content of the `H4` tag under each filter title (`H3` States and `H3` Amenities) by `&nbsp;`
        * `State`, `City` and `Amenity` objects must be loaded from `DBStorage` and sorted by name (A->Z)
* You must use the option `strict_slashes=False` in your route definition
* Import this [`10-hbnb_filters.sql`](./web_flask/tests/10-hbnb_filters.sql) to have some data

**IMPORTANT**
* Make sure you have a running and valid `setup_mysql_dev.sql` in your `AirBnB_clone_v2` repository ([task](./PROJECT_0x02.md/#white-check-mark-3-mysql-setup-development))
* Make sure all tables are created when you run `echo "quit" | HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./console.py`

File(s): [`web_flask/10-hbnb_filters.py`](./web_flask/10-hbnb_filters.py) [`web_flask/templates/10-hbnb_filters.html`](./web_flask/templates/10-hbnb_filters.html) [`web_flask/static/`](./web_flask/static/)

## Advanced Tasks

### :white_large_square: 12. HBNB is alive!
Write a script that starts a Flask web application:
* Your web application must be listening on `0.0.0.0`, port `5000`
* You must use `storage` for fetching data from the storage engine (`FileStorage` or `DBStorage`) => `from models import storage` and `storage.all(...)`
* To load all cities of a `State`:
    * If your storage engine is `DBStorage`, you must use `cities` relationship
    * Otherwise, use the public getter method `cities`
* After each request you must remove the current SQLAlchemy Session:
    * Declare a method to handle `@app.teardown_appcontext`
    * Call in this method `storage.close()`
* Routes:
    * `/hbnb`: display a HTML page like `8-index.html`, done during the [0x01. AirBnB clone - Web static](https://github.com/allelomorph/AirBnB_clone/PROJECT_0x01.md) project
        * Copy files `3-footer.css`, `3-header.css`, `4-common.css`, `6-filters.css` and `8-places.css` from `web_static/styles/` to the folder `web_flask/static/styles`
        * Copy all files from `web_static/images/` to the folder `web_flask/static/images`
        * Update `.popover` class in `6-filters.css` to enable scrolling in the popover and set max height to 300 pixels.
        * Update `8-places.css` to always have the price by night on the top right of each place element, and the name correctly aligned and visible
        * Use `8-index.html` content as source code for the template `100-hbnb.html`:
            * Replace the content of the `H4` tag under each filter title (`H3` States and `H3` Amenities) by `&nbsp;`
            * Make sure all HTML tags from objects are correctly used (example: `<BR />` must generate a new line)
        * `State`, `City`, `Amenity` and `Place` objects must be loaded from DBStorage and sorted by name (A->Z)
* You must use the option `strict_slashes=False` in your route definition
* Import this [`100-hbnb.sql`](./web__flask/tests/100-hbnb.sql) to have some data

**IMPORTANT**
* Make sure you have a running and valid `setup_mysql_dev.sql` in your AirBnB_clone_v2 repository ([task](./PROJECT_0x02.md/#white-check-mark-3-mysql-setup-development))
* Make sure all tables are created when you run `echo "quit" | HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./console.py`

File(s): [`web_flask/100-hbnb.py`](./web_flask/100-hbnb.py) [`web_flask/templates/100-hbnb.html`](./web_flask/templates/100-hbnb.html) [`web_flask/static/`](./web_flask/static/)

---

## Student
* **Samuel Pomeroy** - [allelomorph](github.com/allelomorph)
