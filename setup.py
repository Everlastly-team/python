from setuptools import setup, find_packages

setup(
    name='everlastly',
    version='1.0.5',
    description='Everlastly API wrapper',
    long_description='Wrapper for Everlastly API. Allows to create trusted timestamp for any data. Async version in async_everlastly module.',
    url='https://github.com/Everlastly-team/python',
    author='Emelyanenko Kirill',
    author_email='kirill@everlastly.com',
    license='MIT',

    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3'
    ],

    # What does your project relate to?
    keywords='everlastly blockchain notarization',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    install_requires=['requests'],
    
)
