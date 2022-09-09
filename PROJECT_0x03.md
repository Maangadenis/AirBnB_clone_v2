# (288) 0x03. AirBnB clone - Deploy static
Foundations > Higher-level programming > AirBnB clone

---

### Project author
Guillaume Salva

### Assignment dates
08-17-2020 to 08-18-2020

### Description
Second of three projects building the second iteration of a website cloning the basic features of the [`airbnb.com` main page, circa 2014-2017](https://web.archive.org/web/20170206112507/https://www.airbnb.com/).

Revisiting Continuous Integration/Continuous Deployment and Nginx concepts from [`holberton-system_engineering-devops`](https://github.com/allelomorph/holberton-system_engineering-devops), plus an intrduction to the Python library Fabric. Deploying the static web content from [(268) 0x01. AirBnB clone - Web static](https://github.com/allelomorph/AirBnB_clone/blob/master/PROJECT_0x01.md) to a simple architecture of two web servers and one load balancer.

## General requirements

## General requirements

### bash
* Interpreter conditions:
  * Ubuntu 14.04 LTS
* First line of executable scripts will be `#!/bin/bash`
* Second line is a comment describing the script's purpose
* Compliance with linter:
  * Shellcheck version 0.3.3-1~ubuntu14.04.1 (via `apt-get`)

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

### Fabric Installation
```bash
$ pip3 uninstall Fabric
$ sudo apt-get install libffi-dev
$ sudo apt-get install libssl-dev
$ sudo apt-get install build-essential
$ sudo apt-get install python3.4-dev
$ sudo apt-get install libpython3-dev
$ pip3 install pyparsing
$ pip3 install appdirs
$ pip3 install setuptools==40.1.0
$ pip3 install cryptography==2.8
$ pip3 install bcrypt==3.1.7
$ pip3 install PyNaCl==1.3.0
$ pip3 install Fabric3==1.14.post1
```

---

## Mandatory Tasks

### :white_check_mark: 0. Prepare your web servers
Write a Bash script that sets up your web servers for the deployment of `web_static`. It must:
* Install Nginx if it not already installed
* Create the folder `/data/` if it doesn’t already exist
* Create the folder `/data/web_static/` if it doesn’t already exist
* Create the folder `/data/web_static/releases/` if it doesn’t already exist
* Create the folder `/data/web_static/shared/` if it doesn’t already exist
* Create the folder `/data/web_static/releases/test/` if it doesn’t already exist
* Create a fake HTML file `/data/web_static/releases/test/index.html` (with simple content, to test your Nginx configuration)
* Create a symbolic link `/data/web_static/current` linked to the `/data/web_static/releases/test/` folder. If the symbolic link already exists, it should be deleted and recreated every time the script is ran.
* Give ownership of the `/data/` folder to the `ubuntu` user AND group (you can assume this user and group exist). This should be recursive; everything inside should be created/owned by this user/group.
* Update the Nginx configuration to serve the content of `/data/web_static/current/` to `hbnb_static` (ex: https://mydomainname.tech/hbnb_static). Don’t forget to restart Nginx after updating the configuration:
  * Use `alias` inside your Nginx configuration
  * [Tip](https://stackoverflow.com/questions/10631933/nginx-static-file-serving-confusion-with-root-alias)

Your program should always exit successfully. **Don’t forget to run your script on both of your web servers.**

File(s): [`0-setup_web_static.sh`](./0-setup_web_static.sh)

### :white_check_mark: 1. Compress before sending
Write a Fabric script that generates a [.tgz](https://en.wikipedia.org/wiki/Tar_%28computing%29) archive from the contents of the `web_static` folder of your AirBnB Clone repo, using the function `do_pack`.
* Prototype: `def do_pack():`
* All files in the folder `web_static` must be added to the final archive
* All archives must be stored in the folder `versions` (your function should create this folder if it doesn’t exist)
* The name of the archive created must be `web_static_<year><month><day><hour><minute><second>.tgz`
* The function do_pack must return the archive path if the archive has been correctly generated. Otherwise, it should return `None`

File(s): [`1-pack_web_static.py`](./1-pack_web_static.py)

### :white_large_square: 2. Deploy archive!
Write a Fabric script (based on the file `1-pack_web_static.py`) that distributes an archive to your web servers, using the function `do_deploy`:
* Prototype: `def do_deploy(archive_path):`
* Returns `False` if the file at the path `archive_path` doesn’t exist
* The script should take the following steps:
    * Upload the archive to the `/tmp/` directory of the web server
    * Uncompress the archive to the folder `/data/web_static/releases/<archive filename without extension>` on the web server
    * Delete the archive from the web server
    * Delete the symbolic link `/data/web_static/current` from the web server
    * Create a new the symbolic link `/data/web_static/current` on the web server, linked to the new version of your code (`/data/web_static/releases/<archive filename without extension>`)
* All remote commands must be executed on your both web servers (using `env.hosts = ['<IP web-01>', 'IP web-02']` variable in your script)
* Returns `True` if all operations have been done correctly, otherwise returns `False`
* You must use this script to deploy it on your servers: `xx-web-01` and `xx-web-02`

In the following example, the SSH key and the username used for accessing to the server are passed in the command line. Of course, you could define them as Fabric environment variables (ex: `env.user =...`)

File(s): [`2-do_deploy_web_static.py`](./2-do_deploy_web_static.py)

### :white_check_mark: 3. Full deployment
Write a Fabric script (based on the file `2-do_deploy_web_static.py`) that creates and distributes an archive to your web servers, using the function `deploy`:
* Prototype: `def deploy():`
* The script should take the following steps:
    * Call the `do_pack()` function and store the path of the created archive
    * Return `False` if no archive has been created
    * Call the `do_deploy(archive_path)` function, using the new path of the new archive
    * Return the return value of `do_deploy`
* All remote commands must be executed on both of web your servers (using env.hosts = ['<IP web-01>', 'IP web-02'] variable in your script)
* You must use this script to deploy it on your servers: `xx-web-01` and `xx-web-02`

File(s): [`3-deploy_web_static.py`](./3-deploy_web_static.py)

## Advanced Tasks

### :white_check_mark: 4. Keep it clean!
Write a Fabric script (based on the file `3-deploy_web_static.py`) that deletes out-of-date archives, using the function `do_clean`:
* Prototype: `def do_clean(number=0):`
* `number` is the number of the archives, including the most recent, to keep.
    * If `number` is 0 or 1, keep only the most recent version of your archive.
    * if `number` is 2, keep the most recent, and second most recent versions of your archive.
    * etc.
* Your script should:
    * Delete all unnecessary archives (all archives minus the number to keep) in the `versions` folder
    * Delete all unnecessary archives (all archives minus the number to keep) in the `/data/web_static/releases` folder of both of your web servers
* All remote commands must be executed on both of your web servers (using the `env.hosts = ['<IP web-01>', 'IP web-02']` variable in your script)

File(s): [`100-clean_web_static.py`](./100-clean_web_static.py)

### :white_check_mark: 5. Puppet for setup
Redo [task 0](#white_check_mark-0-prepare-your-web-servers), this time using Puppet.

File(s): [`101-setup_web_static.pp`](./101-setup_web_static.pp)

---

## Student
* **Samuel Pomeroy** - [allelomorph](github.com/allelomorph)
