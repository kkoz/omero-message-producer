import os
import sys

from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand

import version

# Hack to prevent stupid "TypeError: 'NoneType' object is not callable" error
# in multiprocessing/util.py _exit_function when running `python
# setup.py test` or `python setup.py flake8`.  See:
#  * http://www.eby-sarna.com/pipermail/peak/2010-May/003357.html)
#  * https://github.com/getsentry/raven-python/blob/master/setup.py
import multiprocessing
assert multiprocessing  # silence flake8


def get_requirements(suffix=''):
    with open('requirements%s.txt' % suffix) as f:
        rv = f.read().splitlines()
    return rv


def read(fname):
    """
    Utility function to read the README file.
    :rtype : String
    """
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(name='omero-message-producer',
      version=version.getVersion(),
      description='Omero RabbitMQ Message Producer',
      long_description=read('README.md'),
      classifiers=[],  # Get strings from
                       # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='',
      author='Glencoe Software, Inc.',
      author_email='kevin@glencoesoftware.com',
      url='https://github.com/kkoz/omero-message-producer',
      license='',
      packages=find_packages(),
      zip_safe=True,
      include_package_data=True,
      platforms='any',
      install_requires=get_requirements(),
      tests_require=get_requirements(''),
      entry_points={
          'console_scripts': [
              'send_message = message_producer.message_producer:send_message',
          ]
      }
      )
