from f.string.to_cy import f as cy
from subprocess import run as sprun

def f():
  print(cy("Executing 'git pull'"))
  pull_result = sprun(args=['git', 'pull'], capture_output=True, cwd='.')
  print(cy('pull_result.stdout.decode():')+f' {pull_result.stdout.decode()}')

def t():
  """
    Not writing this test yet as it is a peripheral piece of code relative to
    the project: 'coruscant',
    it may be moved to an external library at a later date.
  """
  return 1
