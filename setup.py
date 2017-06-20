#!/usr/bin/env python

from distutils.core import setup

setup(name='XGraphic',
      version='0.1',
      description='Switching between nvidia and bumblebee',
      author='Eray AYDIN',
      author_email='eray@labkod.com',
      url='https://www.github.com/erayaydin/xgraphic',
      packages=['xgraphic'],
      package_dir={'xgraphic': 'xgraphic'},
      package_data={'xgraphic': ['stubs/*']},
     )
