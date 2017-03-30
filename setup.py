from setuptools import find_packages, setup


install_requires = [
    'django==1.10.6',
    'wagtail==1.9'
]

test_require = [
    'flake8==3.0.4',
    'isort==4.2.5',
    'pytest==2.9.2',
    'pytest-cov==2.3.1',
    'pytest-django==2.9.1',
    'tox==2.3.1'
]

setup(
    name='application',
    version='0.1.0',
    description='My application short description.',
    author='Rob Moorman',
    author_email='rob@moori.nl',
    install_requires=install_requires,
    extras_require={
        'test': test_require
    },
    scripts=[
        'manage.py'
    ],
    package_dir={'': 'src'},
    packages=find_packages('src'),
    include_package_data=True,
    classifier=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Operating System :: Unix',
        'Programming Language :: Python',
    ],
)
