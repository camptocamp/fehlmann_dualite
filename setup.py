# coding=utf-8
import os
from setuptools import setup

VERSION = '0.1.0'
HERE = os.path.abspath(os.path.dirname(__file__))
INSTALL_REQUIRES = [pkg for pkg in open(os.path.join(HERE, 'requirements.txt')).read().splitlines()]
TEST_REQUIRES = [pkg for pkg in open(os.path.join(HERE, 'build_requirements.txt')).read().splitlines()]


def long_description():
    try:
        return open('README.md').read()
    except FileNotFoundError:
        return ""


setup(
    name='dualite_transnumerique',
    version=VERSION,
    description='La dualité transnumérique',
    long_description=long_description(),
    long_description_content_type='text/markdown',
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6"
    ],
    author='Camptocamp',
    author_email='info@camptocamp.com',
    url='http://n-interaction.ch',
    keywords='math',
    packages=['dualite_transnumerique'],
    include_package_data=True,
    zip_safe=False,
    install_requires=INSTALL_REQUIRES,
    tests_require=INSTALL_REQUIRES + TEST_REQUIRES,
    test_suite="dualite_transnumerique",
    entry_points={
        'console_scripts': [
            'dualite_transnumerique_shell = dualite_transnumerique.shell:main',
            'dualite_transnumerique = dualite_transnumerique.ui:main'
        ]
    },

)
