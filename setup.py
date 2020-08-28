from setuptools import setup
setup(
    name = 'IVY',
    version = '1.0.0.1',
    packages = ['IVY'],
    entry_points = {
        'console_scripts': [
            'IVY = IVY.__main__:main'
        ]
    })
