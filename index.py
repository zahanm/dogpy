
import sys
import json

def output(out):
  json.dump(out, sys.stdout)
  sys.exit(0)
