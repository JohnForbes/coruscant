from k.block import Block as B
from k.blocks import Blocks as Bs

class ParentBlock(B):
  def __init__(self, name: str, blocks: Bs, blocks_margin: int=1):
    if not isinstance(blocks, Bs):
      raise TypeError(f'blocks must be Blocks, got {type(blocks)}')
  
    b_base = blocks.hstack(margin=blocks_margin)
    b_name = B([name])
    b = Bs([b_name, b_base]).vstack()
    b = b.carry_down_vertical_lines()
    super().__init__(b.lines)

    self._name = name
    self._blocks = blocks

  block_count = property(lambda self: self.len(self._blocks))

f = lambda x: ParentBlock(**x)

def t():
  from hak.pf import f as pf
  from hak.pxyz import f as pxyz
  def t_one_child_column():
    x = {'name': 'name', 'blocks': Bs([B(['a', 'c', 'd'])])}
    y = B(lines=['name', '----', 'a', 'c', 'd'])
    return pxyz(x, [str(y)], [str(f(x))])
  if not t_one_child_column(): return pf('!t_one_child_column')
  def t_two_child_columns():
    x = {'name': 'name', 'blocks': Bs([B(['a', 'c', 'd']), B(['b', 'e'])])}
    y = B(lines=['name ', '-----', 'a | b', 'c | e', 'd |  '])
    return pxyz(x, [str(y)], [str(f(x))])
  if not t_two_child_columns(): return pf('!t_two_child_columns')
  def t_dog_blocks():
    x = {'name': 'dog', 'blocks': Bs([B(['ab', 'de', 'gh'])])}
    y = B(lines=['dog', '---', 'ab', 'de', 'gh'])
    return pxyz(x, [str(y)], [str(f(x))])
  if not t_dog_blocks(): return pf('!t_dog_blocks')
  def t_to_three_columns():
    x = {
      'name': 'name',
      'blocks': Bs([B(['a', 'd', 'g']), B(['b', 'e', 'h']), B(['c', 'f', 'i'])])
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
      ParentBlock(name='dog', blocks=_dog_blocks),
      ParentBlock(name='cat', blocks=_cat_blocks),
      ParentBlock(name='fish', blocks=_fish_blocks)
    ])
    x = {'name': 'nested', 'blocks': _blocks}
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
  return 1
