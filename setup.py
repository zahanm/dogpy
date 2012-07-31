
from distutils.core import setup

setup(
  name="dogpy",
  version="0.1.1",
  author="Zahan Malkani",
  author_email="z@zahanm.com",
  py_modules=[ "dogpy" ],
  url="https://github.com/zahanm/dogpy",
  description="Python library for the Dog programming language",
  long_description="""\
  Python Interface to Dog
  -----------------------

  Needs just two components for use:
  - The `@dogpy.extfunc` decorator for the function being targeted
  - And the `dogpy.run()` line in your main scripting line

  Needs Python 2.6 or greater (AFAIK)
  """,
  classifiers=[
    "Programming Language :: Python",
    "Programming Language :: Python :: 3",
    "Development Status :: 4 - Beta",
    "Environment :: Web Environment",
    "Operating System :: OS Independent",
    "Intended Audience :: Developers",
    "Intended Audience :: Education",
    "Intended Audience :: End Users/Desktop",
    "Intended Audience :: Other Audience",
    "Intended Audience :: Religion",
    "Intended Audience :: Science/Research",
    "License :: OSI Approved :: MIT License",
    "Topic :: Software Development :: Libraries"
  ]
)
