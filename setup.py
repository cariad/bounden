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
    "Programming Language :: Python :: 3.9",
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
        "rebelbase==1.0.0a6",
    ],
    license="MIT",
    long_description=long_description,
    long_description_content_type="text/markdown",
    name="bounden",
    packages=[
        "bounden",
        "bounden.coordinates",
        "bounden.points",
        "bounden.regions",
        "bounden.vectors",
        "bounden.volumes",
    ],
    package_data={
        "bounden": ["py.typed"],
        "bounden.coordinates": ["py.typed"],
        "bounden.points": ["py.typed"],
        "bounden.regions": ["py.typed"],
        "bounden.vectors": ["py.typed"],
        "bounden.volumes": ["py.typed"],
    },
    project_urls={
        "Documentation": "https://bounden.dev",
        "Funding": "https://github.com/sponsors/cariad",
        "Issues": "https://github.com/cariad/bounden/issues",
        "Source": "https://github.com/cariad/bounden",
    },
    python_requires=">=3.9",
    url="https://bounden.dev",
    version=curr_version,
)
