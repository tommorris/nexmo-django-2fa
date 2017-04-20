from setuptools import find_packages, setup

setup(
    name='nexmo_django_twofactor',
    version='0.0.1',
    description='Nexmo support for django-twofactor',
    # long_description=open('README.rst').read(),
    author='Tom Morris',
    author_email='tom@tommorris.org',
    url='https://github.com/tommorris/nexmo-django-twofactor',
    #download_url='https://pypi.python.org/pypi/nexmo-django-twofactor',
    license='MIT',
    packages=find_packages(exclude=('example', 'tests')),
    install_requires=[
        'nexmo',
        'django-two-factor-auth>=1.6.0',
        'Django>=1.8,!=1.9.*',
    ],
    extras_require={
        #'Call': ['nexmo'],
        'SMS': ['nexmo']
    },
    include_package_data=True,
)
