from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e.'

def get_requirements(file_path:str)->List[str]:
    '''
    This function will return the  list of requirement
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        [req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements

setup(
    name="MLproject01",
    version='0.0.1',
    author="Praveen",
    author_email="arulpraveen3456@gmail.com",
    package=find_packages(),
    install_requires=get_requirements('requirements.txt')
)