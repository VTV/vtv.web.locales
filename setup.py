# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
import os

version = '1.0'
long_description = open("README.txt").read() + "\n" + \
                   open(os.path.join("docs", "INSTALL.txt")).read() + "\n" + \
                   open(os.path.join("docs", "CREDITS.txt")).read() + "\n" + \
                   open(os.path.join("docs", "HISTORY.txt")).read()

setup(name='vtv.web.locales',
      version=version,
      description="Localizaciones para sitio web de Venezolana de Televisión.",
      long_description=long_description,
      classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Framework :: Plone",
        "Framework :: Plone :: 4.2",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Office/Business :: News/Diary",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='l10n i18n locale translation',
      author='Héctor Velarde',
      author_email='hector.velarde@gmail.com',
      url='https://github.com/VTV/vtv.web.locales',
      license='GPLv2',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['vtv', 'vtv.web'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
        'setuptools',
        ],
      )
