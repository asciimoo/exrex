from setuptools import setup, find_packages

setup(
    name = 'exrex',
    version = '0.9.3',
    author = 'Adam Tauber',
    author_email = 'asciimoo@gmail.com',
    description = 'Irregular methods for regular expressions',
    license = 'AGPLv3+',
    keywords = "regexp generators string generation regex simplification",
    url = 'https://github.com/asciimoo/exrex',
    scripts = ['exrex.py'],
    py_modules = ['exrex'],
    packages = find_packages(),
    install_requires = [],
    download_url = 'https://github.com/asciimoo/exrex/tarball/master',
    entry_points={
        "console_scripts": ["exrex=exrex:__main__"]
    },
    classifiers = [
        "Development Status :: 4 - Beta",
        "Topic :: Utilities",
        'Environment :: Console',
        'License :: OSI Approved :: GNU Affero General Public License v3'
    ],
)
