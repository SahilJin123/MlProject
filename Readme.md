# End to End Ml Project

## Commands To Run the Project
### Create virtual Env 
1. Open Anaconda prompt 
2. Make the folder MLProject
3. Run command conda create -p venv python==3.8 -y

### Activate Virtual ENV
1. conda activate venv/

### Install all the requirements 
1. pip install -r requirements.txt

######
## Tutorial 1
### setup.py
##
The setup script is the centre of all activity in building, distributing, and installing modules using the Distutils. The main purpose of the setup script is to describe your module distribution to the Distutils, so that the various commands that operate on your modules do the right thing. As we saw in section A Simple Example above, the setup script consists mainly of a call to setup(), and most information supplied to the Distutils by the module developer is supplied as keyword arguments to setup().


setup.py is a Python script used for packaging and distributing Python modules or packages. The setup.py file contains various metadata about the package, such as the package name, version, author, description, dependencies, and other details required for the package installation and distribution.

### find_packages() in setup.py
##
The find_packages() function is a utility function from the setuptools module that recursively searches for all Python packages in the current directory and its subdirectories and returns a list of their names as strings. This function helps to automate the process of including all the packages in the package distribution without explicitly listing them in the setup.py file.



For example, if your package has the following directory structure:


my_package/
├── __init__.py
├── module1.py
├── module2.py
├── subpackage/
│   ├── __init__.py
│   └── submodule.py
└── tests/
    ├── __init__.py
    └── test_module1.py

Then, the find_packages() function will return the following list:

['my_package', 'my_package.subpackage', 'my_package.tests']

This list will be used by the packages argument to include all the packages in the package distribution.

### what is -e . ?
##
-e . :- This automatically triggers setip.py to build the packages.