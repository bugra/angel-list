import angel
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

packages = [
    'angel'
]

requires = []

with open('README.rst') as f:
    readme = f.read()

setup(
    name='angel',
    version=angel.__version__,
    description='Python API for Angellist',
    long_description=readme,
    author='Bugra Akyildiz',
    author_email='vbugra@gmail.com',
    url='https://github.com/bugra/angel-list',
    packages=packages,
    package_data={'': ['LICENSE', 'NOTICE'], 'angel': ['*.pem']},
    package_dir={'angel': 'angel'},
    include_package_data=True,
    install_requires=requires,
    license='MIT',
    zip_safe=False,
    classifiers=(
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',

    ),
)
