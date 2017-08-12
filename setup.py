from setuptools import setup, find_packages

readme = open('README.md','r')
README_TEXT = readme.read()
readme.close()

setup(
    name="bibcure",
    version="0.1",
    packages = find_packages(exclude=["build",]),
    scripts=["bibcure/bin/bibcure"],
    long_description = README_TEXT,
    install_requires=["bibtexparser", "future"],
    include_package_data=True,
    package_data={
        "data":["data/db_abbrev.json", "data/teste"]
    },
    license="GPLv3",
    description="Abbreviates journal names inside in a given bibtex file",
    author="Bruno Messias",
    author_email="messias.physics@gmail.com",
    download_url="https://github.com/devmessias/bibcure/archive/0.1.tar.gz",
    keywords=["bibtex", "abbreviate", "science","scientific-journals"],

    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Intended Audience :: Science/Research",
        "Programming Language :: Python",
        "Topic :: Text Processing :: Markup :: LaTeX",
    ],
    url="https://github.com/devmessias/bibcure"
)
