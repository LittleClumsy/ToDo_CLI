from setuptools import setup, find_packages

setup(
    name='todo_cli',
    version='1.0.0',  # Initial version
    author='Brendon & Evan',
    author_email='Bengelbrecht2002@gmail.com',
    description='A basic Todo CLI program',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/LittleClumsy/ToDo_CLI',
    packages=find_packages(),
    install_requires=[
        #Dependencies from requirements.txt
    ],
    entry_points={
        'console_scripts': [
            'todo=todo:main',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
