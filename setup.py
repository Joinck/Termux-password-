from setuptools import setup, find_packages

setup(
    name='my_termux_repo',
    version='0.1',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'set_password=my_script:set_password',
        ],
    },
)
