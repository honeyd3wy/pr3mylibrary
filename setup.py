from setuptools import setup, find_packages

setup(
    name ='pr3mylibrary',
    version = '1.0.0',
    description = 'my library for project',
    author = 'honeyd3wy',
    author_email = None,
    packages = find_packages(),
    install_requires=[ ],
    url = 'https://github.com/honeyd3wy/pr3mylibrary.git',
    py_modules = ['data_handling', 'get_myplaylist_api', 'model'],
    zip_safe = False
)