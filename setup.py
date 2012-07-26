
from distutils.core import setup

setup(
  name="Dogpy",
  version="0.1",
  author="Zahan Malkani",
  author_email="z@zahanm.com",
  py_modules=[ "dogpy" ],
  url="https://github.com/zahanm/dogpy",
  download_url="https://github.com/zahanm/dogpy/tarball/master",
  description="Python library for the Dog programming language",
  long_description="""\
  Python Interface to Dog
  -----------------------

  Needs just two components for use:
  - The `@dogpy.extfunc` decorator for the function being targeted
  - And the `dogpy.run()` line in your main scripting line

  Needs Python 2.6 or greater (AFAIK)
  """
)
