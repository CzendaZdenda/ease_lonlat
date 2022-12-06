import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ease_lonlat",
    version="0.0.3.5",
    author="Zdenek Ruzicka",
    author_email="tramtara@seznam.cz",
    description="To convert between LON, LAT coordinates and EASE(2) grid ROW, COL.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/CzendaZdenda/ease_lonlat",
    project_urls={
        "Bug Tracker": "https://github.com/CzendaZdenda/ease_lonlat/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: GIS"
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
    install_requires=['pyproj'],
    extras_require={
        "testing":  ['pytest', 'numpy']}
)