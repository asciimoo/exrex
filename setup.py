from setuptools import setup, find_packages

setup(
    name='exrex',
    version='0.10.1',
    author='Adam Tauber',
    author_email='asciimoo@gmail.com',
    description='Irregular methods for regular expressions',
    license='AGPLv3+',
    keywords="regexp generators string generation regex simplification",
    url='https://github.com/asciimoo/exrex',
    scripts=['exrex.py'],
    py_modules=['exrex'],
    packages=find_packages(),
    install_requires=[],
    download_url='https://github.com/asciimoo/exrex/tarball/master',
    entry_points={
        "console_scripts": ["exrex=exrex:__main__"]
    },
    classifiers=[
        # As from http://pypi.python.org/pypi?%3Aaction=list_classifiers
        "Development Status :: 4 - Beta",
        "Topic :: Utilities",
        'Environment :: Console',
        'License :: OSI Approved :: GNU Affero General Public License v3',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ]
)
