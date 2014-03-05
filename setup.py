from setuptools import setup

setup(
    name='assert_tools',
    url='http://mideo.github.io/assert_tools/',
    description='A Python Unit/Functional test library.',
    version='0.0.1',
    author='Mide Ojikutu',
    author_email='mide.ojikutu@gmail.com',
    packages=['assert_tools'],
    install_requires=['unittest2', 'requests', 'httplib2'],
    tests_require=["nose", 'mock', 'coverage', 'nosexcover'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 2 :: Only',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Unix',
        'Operating System :: POSIX',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Testing',
        'Natural Language :: English',
    ],
    keywords=[
        'testing', 'python', 'rest', 'unit testing', 'functional testing']
)
