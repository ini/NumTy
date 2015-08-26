from distutils.core import setup

setup(
    name='NumTy',
    version='1.0',
    author='Ini Oguntola',
    author_email='ioguntol@gmail.com',
    packages=['numty', 'numty.test'],
    scripts=[],
    url='http://github.com/ioguntol/numty',
    license='LICENSE.txt',
    description='A number theory library for Python 2.7.',
    long_description=open('README.txt').read(),
    install_requires=[
        "Django >= 1.1.1",
        "caldav == 0.1.4",
    ],
)
