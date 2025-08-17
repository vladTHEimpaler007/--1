from setuptools import find_packages, setup
from typing import List

hyphen_e_dot= '-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return a list of strings -- Requirements
    '''
    requirements =[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        [req.replace("\n","") for req in requirements]

        if hyphen_e_dot in requirements:
            requirements.remove(hyphen_e_dot)

    return requirements



setup(
    name='mlproject',
    version = '0.0.1',
    author = 'Sayantan',
    author_email='gsayantan2408@gmail.com',
    packages=find_packages(),
    install_requires=['pandas','numpy','seaborn']
)