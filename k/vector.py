from typing import List
from f.obj.is_zeroish import f as is_zeroish

class Vector:
  def __init__(self, values: List): self._values = values
  all_are_zeroish = property(lambda self: all([is_zeroish(_) for _ in self.v]))
  v = values = property(lambda self: self._values)
  h = height = property(lambda self: len(self._values))
  t = type = property(lambda self: type(self._values[0]))
  
  def _get_unit_str(self):
    if self.type == type(0): return 'int'
    return 'blergh'

  u = unit = unit_str = property(lambda self: self._get_unit_str())
  w = width = property(lambda self: max([len(str(_)) for _ in self._values]))

f = lambda x: Vector(**x)

def t():
  from hak.pf import f as pf
  from hak.pxyz import f as pxyz
  def t_a():
    x = {'values': [0, 1, 2]}
    return pxyz(x, [0, 1, 2], f(x).values)
  if not t_a(): return pf('!t_a')

  def t_w():
    x = {'values': [0, 10, 100]}
    return pxyz(x, 3, f(x).w)
  if not t_w(): return pf('!t_w')

  def t_type():
    x = {'values': [0, 10, 100]}
    return pxyz(x, type(0), f(x).t)
  if not t_type(): return pf('!t_type')

  def t_unit():
    x = {'values': [0, 10, 100]}
    return pxyz(x, 'int', f(x).u)
  if not t_unit(): return pf('!t_unit')
  
  def t_h():
    x = {'values': [0, 10, 100, 1000]}
    return pxyz(x, 4, f(x).h)
  if not t_h(): return pf('!t_h')

  def t_all_are_zeroish():
    def t_all_are_zeroish_0():
      x = {'values': [0, 0, 1]}
      return pxyz(x, 0, f(x).all_are_zeroish)
    if not t_all_are_zeroish_0(): return pf('!t_all_are_zeroish_0')
    def t_all_are_zeroish_1():
      x = {'values': [0, 0, None]}
      return pxyz(x, 1, f(x).all_are_zeroish)
    if not t_all_are_zeroish_1(): return pf('!t_all_are_zeroish_1')
    return 1
  if not t_all_are_zeroish(): return pf('!t_all_are_zeroish')
  return 1
