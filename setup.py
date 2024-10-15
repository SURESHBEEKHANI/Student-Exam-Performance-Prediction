from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    '''
    This function will return the list of requirements
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements

setup(
    name="student-exam-performance-prediction",
    version="1.0.0",
    packages=find_packages(),
    # Package metadata
    author="Suresh Beekhani",
    author_email="sureshbeekhani26@gmail.com",
    description="A tool for predicting student exam performance based on various factors.",
    long_description="This package provides a comprehensive model for predicting student exam performance using data analysis and machine learning techniques.",
    long_description_content_type="text/markdown",
    url="https://github.com/SURESHBEEKHANI/Student-Exam-Performance-Prediction.git",
    # Read dependencies from requirements.txt
    install_requires=get_requirements('requirements.txt'),
    # License and classification
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3.12",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
