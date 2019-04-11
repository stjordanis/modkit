from os.path import dirname, abspath, join
from setuptools import setup

HERE = dirname(abspath(__file__))
srcfile = join(HERE, 'modkit.py')
with open(srcfile) as f:
	verline = f.readline()
if not verline.startswith('VERSION'):
	raise ValueError('Cannot find version information.')
VERSION = verline[8:].strip('=\' \n')

author = "pwwang"
author_email = "pwwang@pwwang.com"
keywords = ["module", "loader", "dynamic"]

setup(
    name="modkit",
    version=VERSION,
    description="Python module management",
    author=author,
    author_email=author_email,
    maintainer=author,
    maintainer_email=author_email,
    keywords=keywords,
    url="https://github.com/pwwang/modkit",
    license="MIT",
    py_modules=["modkit"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.1",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Software Development :: Build Tools",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)