from k.filepath_and_line_number import FilepathAndLineNumber as FL

def f(filepath_and_line_number: FL) -> None:
  if not isinstance(filepath_and_line_number, FL): raise TypeError
  from subprocess import run as sprun
  return sprun(args=['code', '-g', str(filepath_and_line_number)])

def t():
  """
    Not writing test as this involves assessing
    whether the file opens in VS Code successfully.
    This is a peripheral piece of code relative to the project: 'coruscant'.
    It may be moved to an external library at a later date
  """
  return 1
