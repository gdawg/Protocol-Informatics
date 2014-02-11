import os
import platform
from setuptools import setup, find_packages
from setuptools.extension import Extension

setup(
    name = "PI",
    version = "0.01",
    url = "http://www.baselineresearch.net/PI",
    author_email = "mbeddoe@baselineresearch.net",
    description = "Protocol analysis toolkit using bioinformatics algorithms",
    packages = ["PI"],
    ext_modules=[Extension("PI.align", ['PI/align.pyx'])],
    scripts = ['protinfo'],
    install_requires=['pyrex'],
    requires = ['pure_pcapy','numpy','dot_parser','pydot']
)
