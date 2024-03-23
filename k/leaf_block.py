from k.vector import Vector as V
from k.block import Block as B
from k.name import Name as N
from k.unit import Unit as U

class LeafBlock(B):
  def __init__(self, name: N, vector: V):
    if not isinstance(name, N): raise TypeError('\n'.join([
      'name must be of type Name',
      f'observed type: {type(name)}',
      f'observed value: {name}'
    ]))
    self._name = name

    if not isinstance(vector, V): raise TypeError('\n'.join([
      'vector must be of type str',
      f'observed type: {type(vector)}',
      f'observed value: {vector}'
    ]))
    self._vector = vector

    _lines = [
      name,
      self._vector.unit,
      *self._vector.values
    ]
    super().__init__(lines=_lines)
  
  _get_unit_str = lambda self: self._v.type

  def _get_width(self) -> int:
    w_v = self._vector.width
    w_n = self._name.width
    print(f'type(self._vector.unit): {type(self._vector.unit)}')
    raise NotImplementedError('!')
    w_u = self._vector.unit.width
    return max([w_v, w_n, w_u])

  t = type = property(lambda self: self._v.type)
  u = unit = unit_str = property(lambda self: U(self._v.unit_str))
  w = width = property(lambda self: self._get_width())

f = lambda x: LeafBlock(**x)

def t():
  from hak.pf import f as pf
  from hak.pxyz import f as pxyz
  def t_a():
    x = {'name': N('foo'), 'vector': V(['a', 'bb'])}
    y = B([
      'foo',
      '---',
      'str',
      '---',
      'a  ',
      'bb '
    ])
    z = f(x)
    return pxyz(x, y, z)
  if not t_a(): return pf('!t_a')

  # def __init__(self, name: str, vector: Vector):
  #   if not isinstance(name, str): raise TypeError('\n'.join([
  #     'name must be of type str',
  #     f'observed type: {type(name)}',
  #     f'observed value: {name}'
  #   ]))
  #   self._name = name

  #   if not isinstance(vector, Vector): raise TypeError('\n'.join([
  #     'vector must be of type str',
  #     f'observed type: {type(vector)}',
  #     f'observed value: {vector}'
  #   ]))
  #   self._vector = vector
  
  # _get_unit_str = lambda self: self._v.type

  # def _get_width(self) -> int:
  #   return max([self._vector.w, self._name.w, self._vector._unit.w])

  # t = type = property(lambda self: self._v.type)
  # u = unit = unit_str = property(lambda self: self._v.unit_str)
  # w = width = property(lambda self: self._get_width())
  # fix this t

  # test that width is an int
  # test that width is in [0, inf]
  # test that width is sensible given the data
  # t_type
  # t_unit
  # t_width
  return 1
