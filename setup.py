import setuptools
from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()
    
REQUIREMENTS = [i.strip() for i in open("requirements.txt").readlines()]

setuptools.setup(
    name="latentshift",
    version="0.0.4",
    author="Joseph Paul Cohen",
    author_email="joseph@josephpcohen.com",
    description="A method to generate counterfactuals",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ieee8023/latentshift",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=REQUIREMENTS,
    packages=find_packages(),
)
