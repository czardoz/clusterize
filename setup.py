from setuptools import setup, Extension, find_packages

lcs = Extension('lcs', sources=['clusterize/lcs.c'])

setup(
    name='clusterize',
    version='0.1',
    description='Can be used to cluster HTTP requests into related groups',
    ext_modules=[lcs],
    install_requires=open('requirements.txt').readlines(),
    scripts=['bin/run'],
    packages=find_packages(),
    include_package_data=True,
)