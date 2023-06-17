# Python Technology - RECAP (3 hrs)

## PIP - Package Installer for Python
- Install and uninstall libraries. Libraries are collections of functions and classes

- Internal libraries  - builtin libraries - os, math, sys, setuptools, random etc
- external libraries - installed libraries - virtualenv, pandas, numpy, scikitlearn, Flask, django
```sh
    pip install <packagename> #install a package
    pip help # info and assistance on pip
    pip search <packagename> # search the global repo - PyPi for the package
    pip uninstall <packagename> 
    pip freeze #list installed packages

    pip list -o # returns list of install packages that have newer versions
```
You can install multiple packages in one command by separating them with space 
` pip install pylint pytest numpy pandas`
to install a specific python package, use `pip install <packagename>==version`
e.g pip install numpy==1.23.0
numpy, pylint

### Requirements

To create project/environment requirements 

```
pip freeze > requirements.txt
```

To install from requirements.txt file 

```
     pip install -r requirements.txt
```

## Virtual Environment
- Create isolated libraries. Self contained python libraries for a project

- Data Cleanup _data analyst/engineering - pandas, numpy, SQL, flask, SNS
- Machine Learning _ Scikitlearn, matplotlib, pytouch, geolab
- Web application _ flask, websockets, requests, pyaudio


First, install `virtualenv` package `pip install virtualenv`

To create a virtualenv, 

```python
    python -m venv <environment_name> #env, venv
```
OR 
``` python
    virtualenv <environment_name>
```
To get out of a virtual envirionment, `deactivate`

To activate a virtual env:
For mac and linux
``` python
    source /path_to_env/<environment_name>/bin/activate
```

for windows

    <path_to_env>\<environment_name>\Scripts\activate


## Code Interpretation
The interpreter converts source code (.py files) into machine readable code (bytecode).
`.pyc` files 

To run a python file `python <filepath>/<filename>.py`

- CPython
- IronPython
- Jpython 

## Modules and Packages
In python, a python file is considered a module

### Order of Search for import
 1. The current directory
 2. PYTHONPATH => elements derived from system variable
 3. standard/inbuilt libraries
 4. external libraries

## Git
Guidelines:
- Always have a readme.md/ README.md file that explains the project
- Always have a gitignore file. It holds all the files/folders that wont be pushed to git. 
    e.g __pychahe__, virtual env, 

``` python 
# For first time 
git init
git remote add origin <url>

```

to add changes/file `git add <filename> or git add .` . means add all pending changes/files


U = untracked/ not added to git
M = modified


## PyPi