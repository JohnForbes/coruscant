from k.alignment import Alignment as A
from k.block import Block as B
from k.name import Name as N
from k.vector import Vector as V

class LeafBlock(B):
  def __init__(self, name: N, vector: V, alignment: A):
    if not isinstance(alignment, A): raise TypeError('\n'.join([
      'alignment must be of type Alignment',
      f'observed type: {type(alignment)}',
      f'observed value: {alignment}'
    ]))
    self._alignment = alignment

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

    _hbar = '-'*self.w
    _lines = [
      name,
      _hbar,
      self.v.unit,
      _hbar,
      *self.v.values
    ]
    super().__init__(lines=_lines, alignment=alignment)

  __repr__ = lambda self: self.__class__.__name__+'('+', '.join([
    'name='+repr(self._name),
    'vector='+repr(self._vector)
  ])+')'
  
  n = name = property(lambda self: self._name)
  t = type = property(lambda self: self.v.type)
  u = unit = unit_str = property(lambda self: self.v.unit_str)
  v = vector = property(lambda self: self._vector)
  w = width = property(lambda self: max([self.v.w, self.n.w, self.v.u.w]))

f = lambda x: LeafBlock(**x)

def t():
  from hak.pf import f as pf
  from hak.pxyz import f as pxyz
  from f.random.alignment import f as r_a
  def t_a():
    x = {'name': N('foo'), 'vector': V(['a', 'bb']), 'alignment': A('right')}
    y = B(
      lines=['foo', '---', 'str', '---', '  a', ' bb'],
      alignment=x['alignment']
    )
    z = f(x)
    return pxyz(x, [str(y)], [str(z)], new_line=1)
  if not t_a(): return pf('!t_a')
  def t_name():
    x = {'name': N('foo'), 'vector': V([0, 1]), 'alignment': r_a()}
    return pxyz(x, N('foo'), f(x).n)
  if not t_name(): return pf('!t_name')
  def t_repr():
    x = {'name': N('foo'), 'vector': V(['a', 'bb']), 'alignment': r_a()}
    y = "LeafBlock(name=Name('foo'), vector=Vector(['a', 'bb']))"
    return pxyz(x, y, repr(f(x)))
  if not t_repr(): return pf('!t_repr')
  def t_type():
    x = {'name': N('foo'), 'vector': V(['a', 'bb']), 'alignment': r_a()}
    return pxyz(x, type('-'), f(x).type)
  if not t_type(): return pf('!t_type')
  def t_type_error():
    def t_type_error_alignment():
      x = {'name': 'foo', 'vector': V(['a', 'bb']), 'alignment': 'boom!'}
      try: f(x); return 0
      except TypeError: return 1
    if not t_type_error_alignment(): return pf('!t_type_error_alignment')
    def t_type_error_name():
      x = {'name': 'foo', 'vector': V(['a', 'bb'])}
      try: f(x); return 0
      except TypeError: return 1
    if not t_type_error_name(): return pf('!t_type_error_name')
    def t_type_error_vector():
      x = {'name': N('foo'), 'vector': ['a', 'bb']}
      try: f(x); return 0
      except TypeError: return 1
    if not t_type_error_vector(): return pf('!t_type_error_vector')
    return 1
  if not t_type_error(): return pf('!t_type_error')
  def t_unit():
    x = {'name': N('foo'), 'vector': V(['a', 'bb']), 'alignment': r_a()}
    from k.unit import Unit as U
    return pxyz(x, U('str'), f(x).unit)
  if not t_unit(): return pf('!t_unit')
  def t_vector():
    x = {'name': N('foo'), 'vector': V([0, 1, 2]), 'alignment': r_a()}
    return pxyz(x, V([0, 1, 2]), f(x).v)
  if not t_vector(): return pf('!t_vector')
  def t_width():
    def t_width_name():
      x = {'name': N('foo'), 'vector': V(['a', 'bb']), 'alignment': r_a()}      
      return pxyz(x, 3, f(x).w)
    if not t_width_name(): return pf('!t_width_name')
    def t_width_vector():
      x = {
        'name': N('foo'),
        'vector': V(['a', 'bb', 'ccc', 'dddd']),
        'alignment': r_a()
      }
      return pxyz(x, 4, f(x).w)
    if not t_width_vector(): return pf('!t_width_vector')
    def t_width_vector_unit():
      x = {'name': N('oo'), 'vector': V(['a', 'bb']), 'alignment': r_a()}
      return pxyz(x, 3, f(x).w)
    if not t_width_vector_unit(): return pf('!t_width_vector_unit')
    return 1
  if not t_width(): return pf('!t_width')
  return 1
