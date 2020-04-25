#!/usr/bin/env python

"""PyGame-AniSprite package installer.

Distributing:

  $ setup.py sdist bdist_wheel
  $ twine upload dist/pygame_anisprite-0.2.3.tar.gz dist/pygame_anisprite-0.2.3*.whl
  $ rm -rf dist

  You'll need the wheel, twine package for bdist_wheel. Don't forget
  to clear your dist when finished.

"""

import sys
from setuptools import setup
from distutils.version import StrictVersion


# Build the list of packages required according to Python version
# Pygame isn't on Pypi.
#install_requires = ['Pillow>=2, <4']  # NOTE: why this specific Pillow range?
#wheel installation fails when build with old Pillow, updating.
install_requires = ['Pillow>=7']  # NOTE: why this specific Pillow range?

# x.y.z
python_version = StrictVersion('.'.join(str(n) for n in sys.version_info[:3]))

# the `enum` package is a backport of Python 3.5 enum,
# we only want it in earlier versions of python
if python_version < StrictVersion('3.5'):
    install_requires.append('enum34')

exec(open('pygame_anisprite/__init__.py').read())
setup(name='pygame-anisprite',
      packages=['pygame_anisprite'],
      version=__version__,
      description='Animated sprites for PyGame!',
      setup_requires=['setuptools-markdown'],
      install_requires=install_requires,
      long_description_markdown_filename='README.md',
      author='Lily Mayfield',
      author_email='lily.m.mayfield@gmail.com',
      license='MIT',
      classifiers=['Development Status :: 3 - Alpha',
                   'Intended Audience :: Developers',
                   'Natural Language :: English',
                   'License :: OSI Approved :: MIT License',
                   'Programming Language :: Python :: 2.7',
                   'Programming Language :: Python :: 3.4',
                   'Topic :: Software Development :: Libraries :: pygame',
                  ],
      keywords=('games gaming sprites 2d pygame animation'),  # XXX: done wrong lol?
    )

