from pathlib import Path

from setuptools import setup

from bounden import version

curr_version = version()

readme_path = Path(__file__).parent / "README.md"

with open(readme_path, encoding="utf-8") as f:
    long_description = f.read()

classifiers = [
    "License :: OSI Approved :: MIT License",
    "Natural Language :: English",
    "Operating System :: OS Independent",
    "Programming Language :: Python :: 3 :: Only",
    "Programming Language :: Python :: 3.10",
    "Programming Language :: Python :: 3.11",
    "Typing :: Typed",
]

if "a" in curr_version:
    classifiers.append("Development Status :: 3 - Alpha")
elif "b" in curr_version:
    classifiers.append("Development Status :: 4 - Beta")
else:
    classifiers.append("Development Status :: 5 - Production/Stable")

classifiers.sort()

setup(
    author="Cariad Eccleston",
    author_email="cariad@cariad.earth",
    classifiers=classifiers,
    description="Bounds and positions",
    include_package_data=True,
    install_requires=[
        "rebelbase==1.0.0a7",
        "vinculum==1.0.0b6",
    ],
    license="MIT",
    long_description=long_description,
    long_description_content_type="text/markdown",
    name="bounden",
    packages=[
        "bounden",
        "bounden.axes",
        "bounden.enums",
        "bounden.points",
        "bounden.resolution",
        "bounden.resolved",
    ],
    package_data={
        "bounden": ["py.typed"],
        "bounden.axes": ["py.typed"],
        "bounden.enums": ["py.typed"],
        "bounden.points": ["py.typed"],
        "bounden.resolution": ["py.typed"],
        "bounden.resolved": ["py.typed"],
    },
    project_urls={
        "Documentation": "https://bounden.dev",
        "Funding": "https://github.com/sponsors/cariad",
        "Issues": "https://github.com/cariad/bounden/issues",
        "Source": "https://github.com/cariad/bounden",
    },
    python_requires=">=3.10",
    url="https://bounden.dev",
    version=curr_version,
)
