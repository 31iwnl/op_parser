from setuptools import setup, find_packages

setup(
    name='op_parser',
    version='0.1.0',
    description='Library for downloading and parsing OP and IAGA-2002 files',
    author='31',
    author_email='xhispeco2018@gmail.com',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'requests'
    ],
    python_requires='>=3.7',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
