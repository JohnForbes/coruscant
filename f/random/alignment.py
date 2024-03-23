from d.domains import alignment

def f():
  from random import choice
  return choice(list(alignment))

t = lambda: all([f() in alignment for _ in range(100)])
