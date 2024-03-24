from k.block import Block
from k.blocks import Blocks

class ParentBlock(Block):
  def __init__(self, name: str, blocks: Blocks, blocks_margin: int=1):
    if not isinstance(blocks, Blocks):
      raise TypeError(f'blocks must be Blocks, got {type(blocks)}')
  
    b_base = blocks.hstack(margin=blocks_margin)
    b_name = Block([name])
    b = Blocks([b_name, b_base]).vstack()
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
      'name': 'name',
      'blocks': Blocks([Block(['a', 'c', 'd'])])
    }
    y = Block(lines=[
      'name',
      '----',
      'a',
      'c',
      'd',
    ])
    z = f(x)
    return pxyz(x, [str(y)], [str(z)])
  if not t_one_child_column(): return pf('!t_a')
  def t_two_child_columns():
    x = {
      'name': 'name',
      'blocks': Blocks([Block(['a', 'c', 'd']), Block(['b', 'e'])])
    }
    y = Block(lines=[
      'name ',
      '-----',
      'a | b',
      'c | e',
      'd |  ',
    ])
    z = f(x)
    return pxyz(x, [str(y)], [str(z)])
  if not t_two_child_columns(): return pf('!t_a')
  def t_to_three_columns():
    x = {
      'name': 'name',
      'blocks': Blocks([
        Block(['a', 'd', 'g']),
        Block(['b', 'e', 'h']),
        Block(['c', 'f', 'i'])
      ])
    }
    y = Block(lines=[
      'name',
      '---------',
      'a | b | c',
      'd | e | f',
      'g | h | i',
    ])
    z = f(x)
    return pxyz(x, [str(y)], [str(z)])
  if not t_to_three_columns(): return pf('!t_b')
  return 1
