from datetime import datetime
from hak.file.load import f as load_file
from hak.file.save import f as save_file
from hak.strings.filepaths.py.get import f as list_py_files
from os.path import exists
import numpy as np

def _f(lines, comment_lines, non_comment_lines):
  from hak.classes.block import Block as B
  l = B(['Total lines:', 'Comment lines:', 'Code lines:', 'Progress:'])
  progress = len(non_comment_lines)/len(lines)*100
  w = max([len(str(_)) for _ in [
    *[len(__) for __ in [lines, comment_lines, non_comment_lines]],
    int(progress),
    '2026-06-27 01:32:22'
  ]])
  r = B([
    f'{len(lines):>{w}}',
    f'{len(comment_lines):>{w}}',
    f'{len(non_comment_lines):>{w}}',
    f'{progress:>{w+3}.2f} %'
  ])
  from hak.strings.block.hstack import f as hstack
  _ = str(hstack([l, r])).replace('|', ' ')
  print(_)

def f():
  lines = []
  for pyfile in list_py_files(root='.', filepaths=[]):
    lines += load_file(pyfile).split('\n')

  comment_lines = [l for l in lines if l.strip().startswith('#')]
  non_comment_lines = [l for l in lines if not l.strip().startswith('#')]

  _f(lines, comment_lines, non_comment_lines)

  with open('progress.txt', 'a') as _file:
    _file.write(f'{datetime.now().timestamp()},{len(comment_lines)}\n')

  data = np.loadtxt("progress.txt", delimiter=",")
  try:
    print(data.shape[1])
    X, Y = data[:, 0], data[:, 1]
  except IndexError:
    X, Y = np.array([[1711104765.093206], [1000]])
    save_file('./expected_completion.txt', f'2100-01-01 12:00:00.00')

  m, b = np.polyfit(X, Y, deg=1)
  from hak.number.float.epsilon import ε
  expected_completion = -b/(m+ε)
  expected_completion_dt = datetime.fromtimestamp(expected_completion)

  δ = None
  if exists('./expected_completion.txt'):
    try:
      previous_expected_completion = datetime.strptime(
        load_file('./expected_completion.txt').strip(),
        "%Y-%m-%d %H:%M:%S.%f"
      )
    except ValueError:
      previous_expected_completion = datetime.strptime(
        "1970-01-01 10:00:00.00",
        "%Y-%m-%d %H:%M:%S.%f"
      )
    δ = expected_completion_dt - previous_expected_completion
    print(f'E[ω](t-1):     {previous_expected_completion}')

  save_file('./expected_completion.txt', f'{expected_completion_dt}')
  print(f'E[ω](t):       {expected_completion_dt}')
  if δ: print(f'δ:                         {δ}')

t = lambda: 1
