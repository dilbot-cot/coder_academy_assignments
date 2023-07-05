#!/bin/bash

# create a virtual environment
python3 -m venv venv

# activate the virtual environment
source venv/bin/activate

# install dependencies
pip install -r requirements.txt #NOTE: there are no requirements for this app, however to ensure consistent code this has been left in.

# navigate to the directory of your script, assuming the script is not in the same directory as this bash script.
# replace 'directory_path' with the path to your script
cd src

# run the main script
python3 main.py

# deactivate the virtual environment
deactivate