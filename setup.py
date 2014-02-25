#!/usr/bin/env python
import os
from numpy.distutils.core import setup
from hooks import get_cmdclass, get_version

# force sdist to copy files
delattr(os, 'link')

VERSION = '3.1'

name = 'qubic'
long_description = open('README.rst').read()
keywords = 'scientific computing'
platforms = 'MacOS X,Linux,Solaris,Unix,Windows'

setup(name=name,
      version=get_version(name, VERSION),
      description='Simulation and map-making tools for the QUBIC experiment.',
      long_description=long_description,
      url='',
      author='Pierre Chanial',
      author_email='pierre.chanial@apc.univ-paris7.fr',
      install_requires=['progressbar',
                        'pysimulators>=0.7.1',
                        'healpy>=0.6.1',
                        'pyYAML'],
      packages=['qubic'],
      package_data={'qubic': ['calfiles/*fits', 'data/*']},
      platforms=platforms.split(','),
      keywords=keywords.split(','),
      cmdclass=get_cmdclass(),
      license='CeCILL-B',
      classifiers=[
          'Programming Language :: Python',
          'Programming Language :: Python :: 2 :: Only',
          'Development Status :: 4 - Beta',
          'Intended Audience :: Science/Research',
          'Operating System :: OS Independent',
          'Topic :: Scientific/Engineering',
          'Topic :: Scientific/Engineering :: Astronomy'])
