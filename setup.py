from setuptools import setup, find_packages

setup(
    name='nb_nix_kernels',
    version='1.0.0',
    url='https://github.com/costrouc/nb_nix_kernels',
    author='Chris Ostrouchov',
    author_email='chris.ostrouchov@gmail.com',
    description='Nix Kernels Embeded in notebooks',
    packages=['nb_nix_kernels'],
    install_requires=['jupyter_client'],
)
