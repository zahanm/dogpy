
import dogpy

@dogpy.extfunc
def top_k(a, c=1):
  return a + 5 + c

if __name__ == '__main__':
  dogpy.run()
