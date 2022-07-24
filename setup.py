from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
        long_description = "\n" + fh.read()

setup(name='tempmail-lol',
        version='2.9.1',
        description='A Python API for TempMail',
        author='Pyro Botz',
        author_email='cloudbotsedc@gmail.com',
        url='https://github.com/github-noob-arjun/TEMP-MAIL-API',
        packages=find_packages(),
        install_requires=['requests'],
        keywords=['python', 'video', 'api', 'tempmail'],
        classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        ]
        )
