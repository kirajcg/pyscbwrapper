from setuptools import setup, find_packages

from pathlib import Path

this_dir = Path(__file__).parent

with open(this_dir / "README.md", encoding="utf-8") as f:
    long_description = f.read()


setup(
    name='pyscbwrapper',
    version='0.1.1',
    description="Python wrapper for Statistics Sweden's API, which can be found at http://www.scb.se/en/api.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/kirajcg/pyscbwrapper',
    author='Kira Coder Gylling',
    author_email='kira.gylling@gmail.com',
    license='MIT',
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    packages=find_packages(),
    install_requires=[
        'requests>=2.21.0',
    ]
)
