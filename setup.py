from setuptools import setup

setup(
    name='assert_tools',
    description='A Python Unit/Functional test library.',
    version='0.0.1',
    author='Mide Ojikutu',
    author_email='mide.ojikutu@gmail.com',
    packages=['assert_tools'],
    install_requires=['unittest2', 'requests', 'httplib2'],
    tests_require=["nose", 'mock', 'coverage', 'nosexcover'],
    classifiers=[
        'Programming Language :: Python',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Unix',
        'Operating System :: POSIX',
        'Intended Audience :: Developers',
        'Intended Audience :: Software Testers',
        'Topic :: Selenium Server',
    ]
)
