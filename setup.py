from setuptools import find_packages,setup
from typing import List

def get_requirements(file_path:str)->List[str]:
    '''
    This function will return the list of requirements
    '''
    Hyphen_E_Dot='-e .'
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        # Whenever the above will read the lines \n is automaticall added so we need to remove it 
        requirements=[req.replace("\n","") for req in requirements]

        if Hyphen_E_Dot in requirements:
            requirements.remove(Hyphen_E_Dot)

    return requirements

setup(
    name="MLProject",
    version='0.0.1',
    author='Sahil Jindal',
    author_email='Sahiljindal450@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')

)