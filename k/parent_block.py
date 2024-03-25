from k.block import Block as B
from k.blocks import Blocks as Bs

class ParentBlock(B):
  def __init__(
    self,
    blocks_margin: int,
    blocks: Bs,
    name: str,
  ):
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
    x = {
      'blocks_margin': 1,
      'blocks': Bs([B(['a', 'c', 'd'])]),
      'name': 'name',
    }
    y = B(lines=['name', '----', 'a', 'c', 'd'])
    return pxyz(x, [str(y)], [str(f(x))])
  if not t_one_child_column(): return pf('!t_one_child_column')
  def t_two_child_columns():
    x = {
      'blocks_margin': 1,
      'blocks': Bs([B(['a', 'c', 'd']), B(['b', 'e'])]),
      'name': 'name',
    }
    y = B(lines=['name ', '-----', 'a | b', 'c | e', 'd |  '])
    return pxyz(x, [str(y)], [str(f(x))])
  if not t_two_child_columns(): return pf('!t_two_child_columns')
  def t_dog_blocks():
    x = {
      'blocks_margin': 1,
      'blocks': Bs([B(['ab', 'de', 'gh'])]),
      'name': 'dog',
    }
    y = B(lines=['dog', '---', 'ab', 'de', 'gh'])
    return pxyz(x, [str(y)], [str(f(x))])
  if not t_dog_blocks(): return pf('!t_dog_blocks')
  def t_to_three_columns():
    x = {
      'blocks_margin': 1,
      'blocks': Bs([
        B(['a', 'd', 'g']),
        B(['b', 'e', 'h']),
        B(['c', 'f', 'i'])
      ]),
      'name': 'name',
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
      ParentBlock(
        blocks_margin=1,
        blocks=_dog_blocks,
        name='dog'
      ),
      ParentBlock(
        blocks_margin=1,
        blocks=_cat_blocks,
        name='cat'
      ),
      ParentBlock(
        blocks_margin=1,
        blocks=_fish_blocks,
        name='fish'
      )
    ])
    x = {
      'blocks_margin': 1,
      'blocks': _blocks,
      'name': 'nested',
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
  return 1
