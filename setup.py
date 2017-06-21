#!/usr/bin/env python

from distutils.core import setup

setup(name='XGraphic',
      version='0.1.0',
      description='Switching between nvidia and bumblebee',
      author='Eray AYDIN',
      author_email='eray@labkod.com',
      url='https://www.github.com/erayaydin/xgraphic',
      packages=['xgraphic'],
      scripts=['bin/xgraphic'],
      license='LICENSE.txt',
      long_description=open('README.txt').read(),
      include_package_data=True
     )
