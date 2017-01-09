from setuptools import setup, find_packages
import os

version = open('version.txt').read().strip()

setup(
    name='edw.logger',
    version=version,
    description="Zope logging package.",
    long_description=(
        open("README.txt").read() + "\n" +
        open(os.path.join("docs", "HISTORY.txt")).read()
    ),
    # Get more strings from
    # http://pypi.python.org/pypi?:action=list_classifiers
    classifiers=[
        "Programming Language :: Python",
        "Framework :: Zope2",
    ],
    keywords='edw logging package',
    author='David Batranu',
    author_email='david.batranu@eaudeweb.ro',
    url='https://github.com/eaudeweb/edw.logger',
    license='GPL',
    packages=find_packages(exclude=['ez_setup']),
    namespace_packages=['edw'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
    ],
    extras_require={
    },
    entry_points="""
      # -*- Entry points: -*-
      """,
)
