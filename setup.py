"""A setuptools based setup module.
See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

from setuptools.command.install import install
from setuptools import setup, find_packages
from codecs import open
from os import path
from os.path import expanduser
import os,json

here = path.abspath(path.dirname(__file__))
home = expanduser("~")

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

class TwtApiDetails(install):
   def run(self):
        print("Creating Data Directories...")
        check_data_dir_exists()
        createCreds()
        install.run(self)

def check_data_dir_exists():
    try:
        original_umask = os.umask(0)
        os.makedirs(home+'/.twweet-cli/data')
    except OSError:
        print("Cannot create data dir the installation cannot continue..")
        exit()
    finally:
        os.umask(original_umask)

def createCreds():
    ck = input('Enter your Consumer Key: ').strip()
    cs = input('Enter your Consumer Secret: ').strip()
    at = input('Enter your Access Token: ').strip()
    ats = input('Enter your Access Token Secret: ').strip()
    jsondata= {"consumer_key": ck,
    "consumer_secret": cs,
    "access_token": at,
    "access_token_secret": ats}
    with open(home+"/.twweet-cli/data/creds.json", "w") as outfile:
        json.dump(jsondata, outfile)
    os.chmod(home+"/.twweet-cli/data/creds.json")

setup(
    name='twweet_cli',
    version='1.0.0',

    description='Tweet right from your cli without even opening your browser.',
    long_description=long_description,

    url='https://github.com/CruiseDevice/twweet-cli/',

    author='Akash Chavan',
    author_email='achavan1211@gmail.com',

    license='MIT',

    classifiers=[
        'Development Status :: 5 - Production/Stable',

        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 3.6',
    ],

    cmdclass={
        'install': TwtApiDetails,
    },


    keywords='twitter tweet cli',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    install_requires=[
         'tweepy',
         'pyyaml'
     ],

     py_modules=["twweet_cli"],
     entry_points={
        'console_scripts': [
            'twweet-cli = twweet_cli:main',
        ],
     }
)
