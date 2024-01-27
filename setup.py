from setuptools import setup, find_packages
from typing import List

with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()     
   

__version__ = "0.0.5"
REPO_NAME = "mongodbconnectorpkg"
PKG_NAME= "mymongoo-automate"
AUTHOR_USER_NAME = "Ashutosh94"
AUTHOR_EMAIL = "ash945512@gmail.com"

setup(
    name=PKG_NAME,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A python package for connecting with database.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    install_requires = ["pymongo","pymongo[srv]","dnspython","pandas","numpy","ensure","pytest"]
    )