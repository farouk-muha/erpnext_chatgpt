from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in sanad_chatgpt/__init__.py
from sanad_chatgpt import __version__ as version

setup(
	name="sanad_chatgpt",
	version=version,
	description="ERPNext ChatGPT API",
	author="Farouk Muharram",
	author_email="faroukm.dev@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
