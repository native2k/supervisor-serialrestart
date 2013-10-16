from setuptools import setup
from os import path


VERSION = (0, 1, 0)
__version__ = VERSION
__versionstr__ = '.'.join(map(str, VERSION))

long_description = ''
try:
    f = open(path.join(path.dirname(__file__), 'README.md'))
    long_description = f.read().strip()
    f.close()
except:
    pass


setup(
    name = 'supervisor-serialrestart',
    description = "Implemenents serialrestart command support for Supervisor.",
    url = "http://github.com/native2k/supervisor-serialrestart",
    long_description = long_description,
    version = __versionstr__,
    author = "Sven Richter",
    author_email = "native2k@gmail.com",
    license = "BSD",
    packages = ['supervisorserialrestart'],
    classifiers = [
        "Development Status :: 4 - Beta",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
    ],
    test_suite='test_supervisorserialrestart.run_tests.run_all',
)
