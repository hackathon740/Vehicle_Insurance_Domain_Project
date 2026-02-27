from setuptools import setup, find_packages

setup(
    name="Vehicle_Insurance_project",
    version="0.0.1",
    author="Abhishek Chattaraj",
    author_email="abhishekchattaraj4@gmail.com",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
)
