import os
import setuptools

here = os.path.abspath(os.path.dirname(__file__))


with open(os.path.join(here, "README.md"), "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pipenv-github-issue-5100",
    version="0.0.0",
    author="rubyisbeautiful",
    author_email="",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: Other/Proprietary License",
        "Operating System :: OS Independent",
    ],
    description="demo for issue 5100",
    include_package_data=True,
    install_requires=[],
    long_description=long_description,
    long_description_content_type="text/markdown",
    package_data={
        'pipenv-github-issue-5100': [],
    },
    package_dir={'': 'src'},
    packages=['pipenv-github-issue-5100'],
    url="https://github.com/pypa/pipenv/issues/5100",
    python_requires='>=3.6, <4',
)
