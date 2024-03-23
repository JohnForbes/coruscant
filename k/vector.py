from typing import List
from f.obj.is_zeroish import f as is_zeroish

class Vector:
  def __init__(self, values: List): self._values = values
  is_zeroish = property(lambda self: all([is_zeroish(_) for _ in self.v]))
  v = values = property(lambda self: self._values)
  h = height = property(lambda self: len(self._values))
  t = type = property(lambda self: type(self._values[0]))
  
  def _get_unit_str(self):
    if self.type == type(0): return 'int'
    return 'blergh'

  u = unit = unit_str = property(lambda self: self._get_unit_str())
  w = width = property(lambda self: max([len(str(_)) for _ in self._values]))

  __eq__ = lambda left, right: left.values == right.values

f = lambda x: Vector(**x)

def t():
  from hak.pf import f as pf
  from hak.pxyz import f as pxyz
  def t_values():
    x = {'values': [0, 1, 2]}
    return pxyz(x, [0, 1, 2], f(x).values)
  if not t_values(): return pf('!t_values')

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

  def t_is_zeroish():
    def t_is_zeroish_0():
      x = {'values': [0, 0, 1]}
      return pxyz(x, 0, f(x).is_zeroish)
    if not t_is_zeroish_0(): return pf('!t_is_zeroish_0')
    def t_is_zeroish_1():
      x = {'values': [0, 0, None]}
      return pxyz(x, 1, f(x).is_zeroish)
    if not t_is_zeroish_1(): return pf('!t_is_zeroish_1')
    return 1
  if not t_is_zeroish(): return pf('!t_is_zeroish')

  def t_eq():
    t_eq_0 = lambda: f({'values': [0, 10, 100]}) != f({'values': [0, 10, 101]})
    if not t_eq_0(): return pf('!t_eq_0')
    t_eq_1 = lambda: f({'values': [0, 10, 100]}) == f({'values': [0, 10, 100]})
    if not t_eq_1(): return pf('!t_eq_1')
    return 1
  if not t_eq(): return pf('!t_eq')
  return 1
