"""
Setup script for Perspective Table Column Configuration
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="perspective-table-config",
    version="1.0.0",
    author="Irfan22in",
    description="Dynamic column configuration builder for Ignition Perspective Table components",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Irfan22in/PerspectiveTableColumnConfiguration",
    packages=find_packages(exclude=["tests", "examples"]),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.6",
    keywords="ignition, perspective, table, column, configuration, scada, hmi",
    project_urls={
        "Bug Reports": "https://github.com/Irfan22in/PerspectiveTableColumnConfiguration/issues",
        "Source": "https://github.com/Irfan22in/PerspectiveTableColumnConfiguration",
    },
)
