from k.alignment import Alignment as A
from k.block import Block as B
from k.name import Name as N
from k.vector import Vector as V

class LeafBlock(B):
  def __init__(
    self,
    address: tuple,
    alignment: A,
    vector: V,
  ):
    if not isinstance(address, tuple): raise TypeError('\n'.join([
      'address must be of type tuple',
      f'observed type: {type(address)}',
      f'observed value: {address}'
    ]))
    self._address = address

    if not isinstance(alignment, A): raise TypeError('\n'.join([
      'alignment must be of type Alignment',
      f'observed type: {type(alignment)}',
      f'observed value: {alignment}'
    ]))
    self._alignment = alignment

    self._name = N(address[-1])

    if not isinstance(vector, V): raise TypeError('\n'.join([
      'vector must be of type str',
      f'observed type: {type(vector)}',
      f'observed value: {vector}'
    ]))
    self._vector = vector

    _hbar = '-'*self.w
    _lines = [
      self._name,
      _hbar,
      self.v.unit,
      _hbar,
      *self.v.values
    ]
    super().__init__(lines=_lines, alignment=alignment)

  __repr__ = lambda self: self.__class__.__name__+'('+', '.join([
    'address='+repr(self._address),
    'alignment='+repr(self._alignment),
    'vector='+repr(self._vector)
  ])+')'
  
  al = alignment = property(lambda self: self._alignment)
  ad = address = property(lambda self: self._address)
  p = parent = property(lambda self: self.ad[-2] if len(self.ad) > 1 else None)
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
  def t_address():
    x = {
      'address': ('foo', 'goo'),
      'vector': V(['a', 'bb']),
      'alignment': r_a()
    }
    return pxyz(x, ('foo', 'goo'), f(x).ad)
  if not t_address(): return pf('!t_address')

  def t_simple():
    x = {
      'address': ('foo',),
      'vector': V(['a', 'bb']),
      'alignment': A('right')
    }
    y = B(
      lines=['foo', '---', 'str', '---', '  a', ' bb'],
      alignment=x['alignment']
    )
    z = f(x)
    return pxyz(x, [str(y)], [str(z)], new_line=1)
  if not t_simple(): return pf('!t_simple')
  def t_name():
    x = {'address': ('foo',), 'vector': V([0, 1]), 'alignment': r_a()}
    return pxyz(x, N('foo'), f(x).n)
  if not t_name(): return pf('!t_name')
  def t_repr():
    x = {'address': ('foo',), 'vector': V(['a', 'bb']), 'alignment': r_a()}
    y = 'LeafBlock('+', '.join([
      f"address=('foo',)",
      f"alignment={repr(x['alignment'])}",
      f"vector=Vector(['a', 'bb'])"
    ])+')'
    return pxyz(x, y, repr(f(x)))
  if not t_repr(): return pf('!t_repr')
  def t_type():
    x = {'address': ('foo',), 'vector': V(['a', 'bb']), 'alignment': r_a()}
    return pxyz(x, type('-'), f(x).type)
  if not t_type(): return pf('!t_type')
  def t_type_error():
    def t_type_error_alignment():
      x = {'address': 'foo', 'vector': V(['a', 'bb']), 'alignment': 'boom!'}
      try: f(x); return 0
      except TypeError: return 1
    if not t_type_error_alignment(): return pf('!t_type_error_alignment')
    def t_type_error_name():
      x = {'address': 'foo', 'vector': V(['a', 'bb'])}
      try: f(x); return 0
      except TypeError: return 1
    if not t_type_error_name(): return pf('!t_type_error_name')
    def t_type_error_vector():
      x = {'address': ('foo',), 'vector': ['a', 'bb']}
      try: f(x); return 0
      except TypeError: return 1
    if not t_type_error_vector(): return pf('!t_type_error_vector')
    return 1
  if not t_type_error(): return pf('!t_type_error')
  def t_unit():
    x = {'address': ('foo',), 'vector': V(['a', 'bb']), 'alignment': r_a()}
    from k.unit import Unit as U
    return pxyz(x, U('str'), f(x).unit)
  if not t_unit(): return pf('!t_unit')
  def t_vector():
    x = {'address': ('foo',), 'vector': V([0, 1, 2]), 'alignment': r_a()}
    return pxyz(x, V([0, 1, 2]), f(x).v)
  if not t_vector(): return pf('!t_vector')
  def t_width():
    def t_width_name():
      x = {'address': ('foo',), 'vector': V(['a', 'bb']), 'alignment': r_a()}
      return pxyz(x, 3, f(x).w)
    if not t_width_name(): return pf('!t_width_name')
    def t_width_vector():
      x = {
        'address': ('foo',),
        'vector': V(['a', 'bb', 'ccc', 'dddd']),
        'alignment': r_a()
      }
      return pxyz(x, 4, f(x).w)
    if not t_width_vector(): return pf('!t_width_vector')
    def t_width_vector_unit():
      x = {'address': ('oo',), 'vector': V(['a', 'bb']), 'alignment': r_a()}
      return pxyz(x, 3, f(x).w)
    if not t_width_vector_unit(): return pf('!t_width_vector_unit')
    return 1
  if not t_width(): return pf('!t_width')
  def t_parent():
    def t_parent_none():
      x = {'address': ('foo',), 'vector': V(['a', 'bb']), 'alignment': r_a()}
      return pxyz(x, None, f(x).p)
    if not t_parent_none(): return pf('!t_parent_none')
    def t_parent_some():
      x = {
        'address': ('foo', 'goo'),
        'vector': V(['a', 'bb']),
        'alignment': r_a()
      }
      return pxyz(x, 'foo', f(x).p)
    if not t_parent_some(): return pf('!t_parent_some')
    return 1
  if not t_parent(): return pf('!t_parent')
  def t_alignment():
    x = {
      'address': ('foo', '  goo'),
      'vector': V(['a', 'bb']),
      'alignment': r_a()
    }
    return pxyz(x, x['alignment'], f(x).al)
  if not t_alignment(): return pf('!t_alignment')
  return 1
