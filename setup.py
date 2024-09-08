from setuptools import setup, find_packages
from pathlib import Path
this_directory = Path(__file__).parent

long_description = (this_directory / "README.md").read_text()

setup(
name='itadvisor_client',
version='0.1.0',
author='David Romero',
author_email='dromero@dromero.dev',
description='A python client for the Schneider Electric application IT Advisor.',
readme = "README.md",
long_description=str(long_description),
long_description_content_type='text/markdown',
packages=find_packages(),
classifiers=[
'Programming Language :: Python :: 3',
'License :: OSI Approved :: MIT License',
'Operating System :: OS Independent',
],
python_requires='>=3.6',
)
