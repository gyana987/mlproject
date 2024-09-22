from setuptools import setup, find_packages
from typing import List

HYPHEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    '''
    This function will return the list of requirements
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.strip() for req in requirements]  # Remove newline characters

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)  # Remove '-e .' if present

    return requirements


setup(
    name='mlproject',  # Name of your project
    version='0.1.0',  # Version of your project
    author='Gyanaranjan Nayak',  # Your name
    author_email='gyanaoffice2019@gmail.com',  # Your contact info
    description='A machine learning project for X',  # Short description of your project
    long_description=open('README.md').read(),  # Long description, typically from README file
    url='https://github.com/gyana987/mlproject',  # Project's homepage or repo link
    packages=find_packages(),  # Automatically find packages in the project
    install_requires=get_requirements('requirements.txt')  # Get dependencies from requirements.txt
)
