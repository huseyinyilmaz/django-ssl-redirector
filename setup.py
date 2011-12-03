from setuptools import setup
from setuptools import find_packages

VERSION = '0.1.b1'
DESCRIPTION = """\
A simple django application that manages http/https statuses of different views.
"""

setup(
    name='django-sslredirector',
    version=VERSION,
    description=DESCRIPTION,
    url='https://bitbucket.org/yilmazhuseyin/django-sslredirector',
    author='Huseyin Yilmaz',
    author_email='me@yilmazhuseyin.com',
    packages=find_packages(),
    include_package_data=True,
    license='GPLv3',
    keywords='django ssl redirect https http',
    install_requires=[
        'Django>=1.3',
    ]
)
