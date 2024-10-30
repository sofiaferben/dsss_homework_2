from setuptools import setup, find_packages

setup(
    name='math_quiz',
    version='0.1',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'math_quiz=math_quiz.math_quiz:main', 
        ],
    },
    install_requires= [  ], #not for now
    author='sofiaferben',
    author_email='sofiaferarndezbenito@gmail.com',
    description='Homwework 2 for Data Science Survival Skills',
    license='Apache 2.0', 
    url='https://github.com/sofiaferben/dsss_homework_2',  )
