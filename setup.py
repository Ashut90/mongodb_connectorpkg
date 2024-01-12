# Method and liberary required to import 

from setuptools import setup, find_packages
from typing import List

HYPEN_E_DOT = ' -e .'

"""
iterating through the filepath to check the requirements that 
that we fetch are in correct format or not
commenting it since its not required in my case , but might be helpful. 
In case, if we use then we need to write one parameter in out setup.
I mentioned it as a comment in setup (downbelow check setup)
"""

'''def get_requirement(file_path : str)->List[str]:
    reuirements = []
    with open(file_path) as f:
        requirements = f.readlines()
        requirements = [req.replace("\n" , "")for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements'''

# Read the read.md file and long discription

with open('README.md', r , encoding='utf-8') as f:
    long_description = f.read()

#Version and rest of the details that I am Using to prepare the package
__version__ = "0.0.4"
REPO_NAME = "mongodb_connectorpkg"
PKG_NAME = "MongoDB-Connect"
AUTHOR_USER_NAME = "Ashut90"
AUTHOR_EMAIL = "ashutosh.formin@gmail.com"

# setup is holding thats required in building a project
setup(

    name= PKG_NAME,
    version= __version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="This is Python Package for connecting Database",
    long_description=long_description,
    long_description_content = "text/markdown",
    url = f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_url = {
        "Bug_Traccking": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues"
    },
    package_dir = {"":"src"},
    package = find_packages(where="src"),
    install_requires = get_requirement("./requirements_dev.txt") 
)
