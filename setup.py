import os
import sys
import multiprocessing
from setuptools import setup
from setuptools.command.test import test as TestCommand
from pip.req import parse_requirements
# generate by: pip3 freeze > requirements.txt
install_reqs = parse_requirements('./requirements.txt', session=False)
reqs = [str(ir.req) for ir in install_reqs]

# # explicitly config
# test_args = [
#     '--cov-report=term',
#     '--cov-report=html',
#     '--cov=a_folder',
#     'tests'
# ]


# class PyTest(TestCommand):
#     user_options = [('pytest-args=', 'a', "Arguments to pass to py.test")]

#     def initialize_options(self):
#         TestCommand.initialize_options(self)
#         self.pytest_args = test_args

#     def run_tests(self):
#         # import here, cause outside the eggs aren't loaded
#         import pytest
#         errno = pytest.main(self.pytest_args)
#         sys.exit(errno)


# Utility function to read the README file.
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


# the setup
setup(
    name='openai_gym',
    version='0.0.1',
    description='Working out at the OpenAI Gym',
    long_description=read('README.md'),
    keywords='openai gym',
    url='https://github.com/kengz/openai_gym',
    author='keng',
    author_email='kengzwl@gmail.com',
    license='MIT',
    packages=[],
    zip_safe=False,
    include_package_data=True,
    install_requires=reqs,
    dependency_links=[],
    extras_require={
        'dev': [],
        'docs': [],
        'testing': []
    },
    classifiers=[],
    tests_require=[],
    # test_suite='tests',
    # cmdclass={'test': PyTest}
)