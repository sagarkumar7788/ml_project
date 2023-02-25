## This file is use for install all the internal and external package automatically.
from setuptools import setup,find_packages
from typing import List

#Declaring variables for setup functions
PROJECT_NAME = "housing-predictor"
VERSION = "0.0.2"
AUTHOR = "Sagar Kumar"
DESRCIPTION = "This is a first FSDS Nov batch Machine Learning Project"

REQUIREMENT_FILE_NAME = "requirements.txt"

HYPHEN_E_DOT = "-e ."


def get_requirements_list()->List[str]:
    """
    Description: This function is going to return list of requirement
    mention in requirements.txt file
    return This function is going to return a list which contain name
    of libraries mentioned in requirements.txt file
    """
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        requirement_list = requirement_file.readlines()
        requirement_list = [requirement_name.replace("\n", "") for requirement_name in requirement_list]
        if HYPHEN_E_DOT in requirement_list:
            requirement_list.remove(HYPHEN_E_DOT)
        return requirement_list



setup(
name=PROJECT_NAME,
version=VERSION,
author=AUTHOR,
description=DESRCIPTION,
packages= find_packages(), ## it will automatically find __init__ package we don`t need to locate with hard code
# install_requires = get_requirements_list()
install_requires = ['Flask', 'gunicorn', 'sklearn', 'pandas', 'numpy','-e .']
)


## folder name is package and file name is module
##if we are using " -e ."  it is mendatry ,there is a setip.py file will exist , 
