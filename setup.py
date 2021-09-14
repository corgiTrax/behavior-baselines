import setuptools
from setuptools import find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="behavior_baselines",
    version="0.0.1",
    author="Stanford University",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/StanfordVL/behavior-baselines",
    project_urls={
        "Bug Tracker": "https://github.com/StanfordVL/behavior-baselines/issues",
    },
    packages=find_packages(),
    install_requires=[
        "stable-baselines3",
    ],
)
