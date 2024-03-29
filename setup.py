from pathlib import Path

from setuptools import find_packages, setup

import asu

long_description = Path("README.md").read_text()

setup(
    name="asu-cli",
    version=asu.__version__,
    description="aws s3 cli utils",
    url="https://github.com/tekumara/asu",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={"console_scripts": ["asu = asu.cli:main"]},
    python_requires=">=3.7",
    packages=find_packages(exclude=["tests"]),
    include_package_data=True,
    install_requires=["boto3==1.17.62", "typer==0.3.2", "rich==10.1.0"],
    extras_require={
        "dev": [
            "black==21.4b2",
            "boto3-stubs[s3]==1.17.62.0",
            "isort==5.8.0",
            "flake8==3.9.1",
            "flake8-annotations==2.6.2",
            "flake8-colors==0.1.9",
            "pre-commit==2.13.0",
            "pytest==6.2.3",
            "twine==3.4.1",
        ]
    },
)
