from subprocess import run as sprun
from f.string.to_cy import f as cy

def f():
  print(cy("Executing 'git status -s'"))
  return sprun(args=['git', 'status', '-s'], capture_output=True, cwd='.')

def t():
  """
    Not writing this test yet as it is a peripheral piece of code relative to
    the project: 'coruscant',
    it may be moved to an external library at a later date.
  """
  return 1
