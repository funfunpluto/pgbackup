from setuptools import setup, find_packages

with open('README.rst', encoding='UTF-8') as f:
    readme = f.read()

setup(
    name='pgbackup',
    version='0.0.1',
    description='psql database back locally or to aws s3',
    long_descript=readme,
    author='funfunpluto',
    author_email='funfunpluto@gmail.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=[
    ]

)
