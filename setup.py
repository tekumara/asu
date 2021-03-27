from pathlib import Path

from setuptools import find_packages, setup

long_description = Path("README.md").read_text()

setup(
    name="asu",
    version="0.0.0",
    description="aws s3 utils",
    long_description=long_description,
    long_description_content_type="text/markdown",
    entry_points={"console_scripts": ["asu = asu.cli:main"]},
    python_requires=">=3.7",
    packages=find_packages(exclude=["tests"]),
    include_package_data=True,
    install_requires=["boto3==1.17.38.0", "typer==0.3.2", "rich==9.13.0"],
    extras_require={
        "dev": [
            "autopep8==1.5.4",
            "boto3-stubs[s3]==1.17.38.0",
            # pin importlib_metadata to avoid conflict, must be <2
            "importlib_metadata==1.7.0",
            "isort==5.6.4",
            "flake8==3.9.0",
            "flake8-annotations==2.6.1",
            "flake8-colors==0.1.9",
            "pre-commit==2.11.1",
            "pytest==6.1.2",
        ]
    },
)
