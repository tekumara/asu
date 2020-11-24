from pathlib import Path

from setuptools import find_packages, setup

long_description = Path("README.md").read_text()

setup(
    name="asu",
    version="0.0.0",
    description="aws s3 utils",
    long_description=long_description,
    long_description_content_type="text/markdown",
    entry_points={"console_scripts": ["asu = asu.main:main"]},
    python_requires=">=3.7",
    packages=find_packages(exclude=["tests"]),
    include_package_data=True,
    install_requires=["boto3==1.16.24","typer==0.3.2"],
    extras_require={
        "dev": [
            "autopep8==1.5.4",
            "boto3-stubs[ec2]==1.16.24.0",
            # pin importlib_metadata to avoid conflict, must be <2
            "importlib_metadata==1.7.0",
            "isort==5.6.4",
            "flake8==3.8.4",
            "flake8-annotations==2.4.1",
            "flake8-colors==0.1.6",
            "pre-commit==2.8.2",
            "pytest==6.1.2",
        ]
    },
)
