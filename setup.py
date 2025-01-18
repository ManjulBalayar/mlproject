from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirements(file_path:str)->List[str]:
    '''
    Function will return a list of requirements
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines() # Readlines read every line of our requirements.txt, but adds a \n after reading each line
        requirements = [req.replace("\n","") for req in requirements] # Here we replace all the \n in our list with empty space, essentially removing it

        if HYPEN_E_DOT in requirements: # Don't want it in my requirements
            requirements.remove(HYPEN_E_DOT)
            
    return requirements

setup(
    name='mlproject',
    version='0.0.1',
    author='Manjul',
    packages=find_packages(), # Automatically finds all the packages being used in the project
    install_requires=get_requirements('requirements.txt')
)

