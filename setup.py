from setuptools import (
    find_packages,
    setup,
)

setup(
    name='network-ping-pong',
    version='0.0.1',
    packages=find_packages(),
    install_requires=['Click', 'pygame'],
)
