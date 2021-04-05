import setuptools

VERSION = '0.1.2'

setuptools.setup(
    name='index-from-time',
    version=VERSION,
    description='Get an integer from between 0 and the passed argument based on the current time and day of the year.',
    url='https://github.com/mts7/index-from-time',
    author='Mike Rodarte',
    license='MIT License',
    packages=setuptools.find_packages(exclude=['*_test.', 'test_*.']),
    classifiers=[
        'License:: OSI Approved:: MIT License',
        'Operating System:: OS Independent',
        'Programming Language:: Python:: 3',
        'Programming Language:: Python:: 3.6',
        'Programming Language:: Python:: 3.7',
        'Programming Language:: Python:: 3.8',
        'Programming Language:: Python:: 3.9',
    ],
    python_requires='>=3.6',
)
