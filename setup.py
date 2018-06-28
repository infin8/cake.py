from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='cake',
      version=version,
      description="API for getcake",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='',
      author='n8',
      author_email='yo.its.n8@gmail.com',
      url='https://github.com/infin8/cake.py.git',
      license='MIT',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=True,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
