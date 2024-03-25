from k.block import Block as B
from k.blocks import Blocks as Bs

class ParentBlock(B):
  def __init__(
    self,
    address: tuple,
    blocks_margin: int,
    blocks: Bs,
  ):
    if not isinstance(address, tuple): raise TypeError('\n'.join([
      'address must be of type tuple',
      f'observed type: {type(address)}',
      f'observed value: {address}'
    ]))
    self._address = address

    if not isinstance(blocks_margin, int):
      raise TypeError(f'blocks_margin must be int, got {type(blocks_margin)}')

    if not isinstance(blocks, Bs):
      raise TypeError(f'blocks must be Blocks, got {type(blocks)}')
  
    self._name = address[-1] if address else ''
    self._blocks = blocks
    b_base = blocks.hstack(margin=blocks_margin)
    b_name = B([self._name])
    
    if b_name.w > b_base.w:
      factor = (b_name.w - (blocks.count-1)*(blocks_margin*2+len('|')))/blocks.w
      _widened = blocks.widen(factor)
      b_base = _widened.hstack(margin=blocks_margin)
    b = Bs([b_name, b_base]).vstack()
    b = b.carry_down_vertical_lines()
    super().__init__(b.lines)

  ad = address = property(lambda self: self._address)
  block_count = property(lambda self: self.len(self._blocks))
  p = parent = property(lambda self: self.ad[-2] if len(self.ad) > 1 else None)
  n = name = property(lambda self: self._name)

f = lambda x: ParentBlock(**x)

def t():
  from hak.pf import f as pf
  from hak.pxyz import f as pxyz
  def t_one_child_column():
    x = {
      'address': ('name',),
      'blocks_margin': 1,
      'blocks': Bs([B(['a', 'c', 'd'])]),
    }
    y = B(lines=['name', '----', 'a', 'c', 'd'])
    return pxyz(x, [str(y)], [str(f(x))])
  if not t_one_child_column(): return pf('!t_one_child_column')
  def t_two_child_columns():
    x = {
      'address': ('name',),
      'blocks_margin': 1,
      'blocks': Bs([B(['a', 'c', 'd']), B(['b', 'e'])]),
    }
    y = B(lines=['name ', '-----', 'a | b', 'c | e', 'd |  '])
    z = f(x)
    return pxyz(x, [str(y)], [str(z)])
  if not t_two_child_columns(): return pf('!t_two_child_columns')
  def t_dog_blocks():
    x = {
      'address': ('dog',),
      'blocks_margin': 1,
      'blocks': Bs([B(['ab', 'de', 'gh'])]),
    }
    y = B(lines=['dog', '---', 'ab', 'de', 'gh'])
    return pxyz(x, [str(y)], [str(f(x))])
  if not t_dog_blocks(): return pf('!t_dog_blocks')
  def t_to_three_columns():
    x = {
      'address': ('name',),
      'blocks_margin': 1,
      'blocks': Bs([
        B(['a', 'd', 'g']),
        B(['b', 'e', 'h']),
        B(['c', 'f', 'i'])
      ]),
    }
    y = B(lines=[
      'name',
      '---------',
      'a | b | c',
      'd | e | f',
      'g | h | i',
    ])
    return pxyz(x, [str(y)], [str(f(x))])
  if not t_to_three_columns(): return pf('!t_to_three_columns')
  def t_nested():
    _dog_blocks = Bs([B(['ab', 'de', 'gh'])])
    _cat_blocks = Bs([B(['ab', 'de', 'gh']), B(['c', 'f', 'i'])])
    _fish_blocks = Bs([B(['a', 'b']), B(['d', 'e']), B(['g', 'h'])])
    _blocks = Bs([
      ParentBlock(address=('dog',), blocks_margin=1, blocks=_dog_blocks),
      ParentBlock(address=('cat',), blocks_margin=1, blocks=_cat_blocks),
      ParentBlock(address=('fish',), blocks_margin=1, blocks=_fish_blocks)
    ])
    x = {
      'address': ('nested',),
      'blocks_margin': 1,
      'blocks': _blocks,
    }
    y = B(lines=[
      '         nested         ',
      '------------------------',
      'dog |  cat   |   fish   ',
      '--- | ------ | ---------',
      'ab  | ab | c | a | d | g',
      'de  | de | f | b | e | h',
      'gh  | gh | i |   |   |  ',
    ])
    return pxyz(x, str(y), str(f(x)), new_line=1)
  if not t_nested(): return pf('!t_nested')

  def t_very_long_name():
    x = {
      'address': ('very_long_name',),
      'blocks_margin': 1,
      'blocks': Bs([
        ParentBlock(
          address=('b',),
          blocks_margin=1,
          blocks=Bs([B(['y', 'd'])])
        ),
        ParentBlock(
          address=('c',),
          blocks_margin=1,
          blocks=Bs([B([2, 5])])
        ),
        ParentBlock(
          address=('d',),
          blocks_margin=1,
          blocks=Bs([B([3, 6])])
        ),
      ]),
    }
    y = B([
      'very_long_name',
      '--------------',
      ' b  |  c  | d ',
      '--- | --- | --',
      ' y  |  2  | 3 ',
      ' d  |  5  | 6 ',
    ])
    z = f(x)
    return pxyz(x, y, z, new_line=1)
  if not t_very_long_name(): return pf('!t_very_long_name')
  return 1
