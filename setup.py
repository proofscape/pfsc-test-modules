import setuptools
import pathlib

with open("README.md", "r") as fh:
    long_description = ''.join(fh.readlines()[1:])

p = pathlib.Path('pfsc_test_modules')
data_files = [str(q.relative_to(p)) for q in p.glob('repos/**/*.pfsc')]

setuptools.setup(
    name="pfsc_test_modules",
    version="0.22.9",
    description="Test modules for pfsc-server",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/proofscape/pfsc-test-modules",
    # https://github.com/pypa/setuptools/issues/3340#issuecomment-1146678086
    packages=setuptools.find_namespace_packages(exclude=['venv.*']),
    package_data={'': data_files},
    classifiers=[
        "License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
    ],
)
