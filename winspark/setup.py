from setuptools import setup, find_packages

setup(
    name="winspark",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "pyspark",  # Add any dependencies here
    ],
    author="Your Name",
    description="Custom Spark utilities and helpers",
)

