# Find Libraries Nearby

This is the application where it is possible to find libraries near the desired location (for example, user location).
Here you can create your own library which is automatically marked in the google map or simply search for already
existing libraries. The challenge was to work with google maps and create custom filter functions when searching for
libraries.

## Getting Started

Below you will find the instructions and requirements on how to install and run this project on your local machine.

### Installing

The first step is to clone the repository.
After that you can create a virtual environment, activate it and install the requirements.txt file:

```
python -m venv env
cd env/Scripts/activate.bat                 // for Windows users
source env/bin/activate                     // for OS X users
python -m pip install -r requirements.txt
```

After successful installation you can start the server:
```
python manage.py runserver
```

## Usage

The demo database is included in the project file.