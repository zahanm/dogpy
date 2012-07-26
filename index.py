
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
  """
  Send back output to Dog, exiting the python code
  """
  json.dump(out, sys.stdout)
  sys.exit(0)

def error(err):
  """
  Exit, and send back an error to Dog
  """
  json.dump({ "error": err }, sys.stdout)
  sys.exit(1)

def run():
  """
  Run the Python code that was called from Dog
  """
  global argv, kwargs
  if len(sys.argv) != 1:
    error("Improper calling convention")
  try:
    inp = json.load(sys.stdin)
  except ValueError:
    error("Invalid JSON passed to external code")
  name = inp["name"]
  if inp["name"] not in doggyfns:
    error("The external function name invoked does not exist")
  argv = inp["argv"]
  kwargs = inp["kwargs"]
  if type(argv) != list or type(kwargs) != dict:
    error("The arguments were formatted incorrectly")
  try:
    doggyfns[name](*argv, **kwargs)
  except TypeError:
    error("The external function received incorrect arguments")

import functools

doggyfns = {}

def extfunc(fn):
  """
  A decorator marking a function as suitable for use with (Dog)[http://dog-lang.org]
  """
  @functools.wraps(fn)
  def wrapper(*args, **kwargs):
    return output( fn(*args, **kwargs) )
  doggyfns[ wrapper.__name__ ] = wrapper
  return wrapper
