
import sys
import json

"""
Expected input on stdin from Dog

{
  "argv": [ arg1, arg2 ]
  "kwargs": {
    "arg3_name": arg3
    "arg4_name": arg4
  },
  "name": "function_name"
}
"""

argv = []
kwargs = {}

def output(out):
  json.dump(out, sys.stdout)
  sys.exit(0)

import functools

dogpyfns = {}

def dogpyfunc(fn):
  """
  A decorator marking a function as suitable for use with (Dog)[http://dog-lang.org]
  """
  @functools.wraps(fn)
  def wrapper(*args, **kwargs):
    return fn(*args, **kwargs)

  dogpyfns[ wrapper.__name__ ] = wrapper
  return wrapper
