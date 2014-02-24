from setuptools import setup

setup(
    name='assert_tools',
    description='A Python Unit/Functional test library.',
    version='0.0.1',
    author='Mide Ojikutu',
    author_email='mide.ojikutu@gmail.com',
    packages=['assert_tools'],
    install_requires=['mock', 'nose', 'unittest2', 'requests', 'httplib2'],
)
