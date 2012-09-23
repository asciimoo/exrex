from setuptools import setup, find_packages

setup(
    name = 'exrex',
    version = '0.6.0',
    author = 'Adam Tauber',
    author_email = 'asciimoo@gmail.com',
    description = ('Exrex is a tool and python module that generates all - or random - matching strings to a given regular expression.'),
    license = 'AGPLv3+',
    keywords = "regexp generators string generation",
    url = 'https://github.com/asciimoo/exrex',
    scripts = ['exrex.py'],
    py_modules = ['exrex'],
    packages = find_packages(),
    install_requires = [],
    download_url = 'https://github.com/asciimoo/exrex/tarball/master',
    classifiers = [
        "Development Status :: 4 - Beta",
        "Topic :: Utilities",
        'Environment :: Console',
        'License :: OSI Approved :: GNU Affero General Public License v3'
    ],
)
