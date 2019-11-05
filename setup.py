from setuptools import setup, find_packages

PACKAGES = ["tim.utils." + p for p in find_packages("proj2md")]

setup(
    name="proj_to_md",
    version="0.0.0a",
    packages=PACKAGES,
    url="",
    license="",
    author="Tim Seed",
    author_email="",
    description="Dump a project structure to Markdown",
    scripts=["tim/utils/proj2md/bin/proj2md"],
    zip_safe=False,
)
