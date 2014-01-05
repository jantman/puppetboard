from setuptools import setup
from sys import version_info

VERSION = "0.0.2"

pyver_requires = ['Flask==0.10.1',
                  'Flask-WTF==0.8.4',
                  'Jinja2==2.7',
                  'MarkupSafe==0.18',
                  'WTForms==1.0.4',
                  'itsdangerous==0.22',
                  'pypuppetdb==0.0.5',
                  'requests==1.2.3'
]

with open('requirements.txt') as file:
    for line in file.readlines():
        pyver_requires.append(line.strip())

with open('README.rst') as file:
    long_description = file.read()

classifiers = [
    'Development Status :: 3 - Alpha',
    'Environment :: Web Environment',
    'Framework :: Flask',
    'License :: OSI Approved :: Apache Software License'
]

setup(
    name='puppetboard',
    version=VERSION,
    author='Daniele Sluijters',
    author_email='github@daenney.net',
    packages=['puppetboard'],
    url='https://github.com/nedap/puppetboard',
    license='Apache 2.0',
    description='Web frontend for PuppetDB',
    long_description=long_description,
    install_requires=pyver_requires,
    keywords="puppet puppetdb puppetboard",
    classifiers=classifiers
)
