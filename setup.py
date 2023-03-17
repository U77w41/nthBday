"""setup"""
import pathlib
import os
import codecs
from setuptools import setup, find_packages

HERE = pathlib.Path(__file__).parent.resolve()

# Get the long description from the README file
long_description = (HERE / 'README.md').read_text(encoding='utf-8')
__version__ = '0.2.7'
__maintainer__ = 'Ujjwal Chowdhury'


# Setting up
setup(
    name='nthBday',
    version=__version__,
    description='An open-source python package to find business days of a month.',
    author=__maintainer__,
    author_email='<u77w41@gmail.com>',
    url='https://github.com/U77w41/nthBday',
    license='MIT',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=find_packages(),
    install_requires=['pandas','datetime'],
    tests_require=['pytest'],
    keywords= ['python', 'date', 'Business Day', 'Working Day', 'Holiday', 'calender']
)

#################################################################################################################
# python3 setup.py sdist bdist_wheel
# twine upload dist/*


