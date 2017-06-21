#!/usr/bin/env python

from setuptools import setup

setup(name='XGraphic',
      version='0.1.3',
      description='Switching between nvidia and bumblebee',
      author='Eray AYDIN',
      author_email='eray@labkod.com',
      url='https://www.github.com/erayaydin/xgraphic',
      packages=['xgraphic'],
      entry_points={
          'console_scripts': [
              'xgraphic = xgraphic.__main__:main'
          ]
      },
      license='LICENSE.txt',
      long_description=open('README.txt').read(),
      include_package_data=True
     )
