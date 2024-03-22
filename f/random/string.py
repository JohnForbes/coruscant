from string import ascii_letters

def f(charset=ascii_letters, min_length=None, max_length=None):
  if max_length is None: max_length = 10
  if min_length is None: min_length = min(5, max_length)
  from random import randint
  from random import choice
  return ''.join([
    choice(charset) for _ in range(randint(min_length, max_length))
  ])

def t():
  x = {'charset': ascii_letters, 'min_length': 5, 'max_length': 10}
  z = f(**x)
  if len(z) < x['min_length']: return pf('len(z) < _min_length')
  if len(z) > x['max_length']: return pf('len(z) > _max_length')
  from hak.pf import f as pf
  for char in z:
    if char not in x['charset']:
      return pf(f"char: {char} not in charset: {x['charset']}")
  return 1
