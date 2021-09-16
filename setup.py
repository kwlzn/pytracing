#!/usr/bin/env python2.7

from setuptools import setup

setup(
    name="pytracing",
    version="0.4",
    description="a python trace profiler that outputs to chrome trace-viewer format (about://tracing).",
    author="Kris Wilson",
    author_email="kwilson@twitter.com",
    extras_require={"test": ["flake8==3.9.2", "pre-commit"]},
    url="https://www.github.com/kwlzn/pytracing",
    packages=["pytracing"],
)
