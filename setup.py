try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
import sys

from codecs import open
from os import path

if sys.version < '3.5.1':
    print("Supports only Python >= 3.5.1")
    sys.exit(1)

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(name='spoj-summarizer',
      version='1.0.0',
      description='An easy to use python package to track your progress on spoj.',
      url='https://github.com/amulyagaur/SPOJ_SUMMARIZER',
      download_url = 'https://github.com/amulyagaur/SPOJ_SUMMARIZER/archive/1.0.0.tar.gz',
      entry_points={'console_scripts': ['richest = richest.__main__:main']},
      keywords=['spoj-summarizer', 'competitive-programming', 'summary', 'progress check','spoj'],
      author='Amulya Gaur',
      author_email='amulya@mnnit.ac.in',
      license='MIT',
      packages=['spoj-summarizer'],
      install_requires=[
          'requests','pandas'
      ],
      long_description=long_description,
      long_description_content_type='text/markdown')