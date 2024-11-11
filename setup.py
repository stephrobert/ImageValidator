# setup.py
from setuptools import setup, find_packages

setup(
    name="image-validator",
    version="0.1.0",
    description="Validate images for cloud",
    author="Stéphane ROBERT",
    author_email="robert.stephane.28@gmail.com",
    url="https://github.com/stephrobert/imagevalidator",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "click",
        "guestfs",
        "pyyaml",
    ],
    entry_points={
        "console_scripts": [
            "image-validator=imagevalidator.main:main",  # Corrigez ici
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.10",
)
