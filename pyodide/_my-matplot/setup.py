from setuptools import setup, find_packages

setup(
    name='my-matplot',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'matplotlib',
    ],
    description='A package to generate base64-encoded matplotlib images',
    author='Your Name',
    author_email='your.email@example.com',
)
