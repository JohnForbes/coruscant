from k.block import Block
from typing import List
from k.flat_container import FlatContainer as FC
from k.parent_block import ParentBlock as PB

def f(dicts: List[dict]) -> Block:
  if not isinstance(dicts, list): raise TypeError('\n'.join([
    'dicts is expected to be of type list',
    f'observed type: {type(dicts)}',
    f'observed value: {dicts}'
  ]))
  if len(dicts) == 0: return Block()
  if dicts[0] == {}: return Block()
  
  fc = FC(dicts)
  if fc.addresses_max_length == 1: return fc.leaf_blocks[0]
  if fc.addresses_max_length == 2: return PB(
    address=fc.leaf_blocks[0].ad[:-1],
    blocks_margin=1,
    blocks=fc.leaf_blocks,
  )
  return ':('

def t():
  from hak.pf import f as pf
  from hak.pxyz import f as pxyz
  from hak.pxyf import f as pxyf
  if not pxyf([{}], Block(), f): return pf('!t_simplest')

  def t_a():
    x = [{'a': 1}, {'a': 2}]
    y = Block([' a ', '---', 'int', '---', ' 1 ', ' 2 '])
    return pxyf(x, y, f, new_line=1)
  if not t_a(): return pf('!t_a')

  def t_type_error():
    x = 'a'
    y = 'dicts is expected to be of type list'
    z = None
    try: z = f(x)
    except TypeError as e:
      z = str(e)
      if y in z: return 1
      return pxyz(x, y, z)
    return pxyz(x, y, z)
  if not t_type_error(): return pf('!t_type_error')

  def t_nested_2_levels():
    x = [{'a': {'b': 1, 'c': 1}}, {'a': {'b': 2, 'c': 2}}]
    y = Block([
      '    a    ',
      '---------',
      ' b  |  c ',
      '--- | ---',
      'int | int',
      '--- | ---',
      ' 1  |  1 ',
      ' 2  |  2 ',
    ])
    return pxyf(x, y, f, new_line=1)
  if not t_nested_2_levels(): return pf('!t_nested_2_levels')

  # def t_nested_3_levels():
  #   x = [
  #     {'a': {'b': {'c': 1, 'd': 2}, 'e': {'g': 3, 'h': 4}}},
  #     {'a': {'b': {'c': 5, 'd': 6}, 'e': {'g': 7, 'h': 8}}}
  #   ]
  #   y = Block([
  #     '          a          ',
  #     '---------------------',
  #     '    b     |    e     ',
  #     '----------|----------',
  #     ' c  |  d  |  g  |  h ',
  #     '--- | --- | --- | ---',
  #     'int | int | int | int',
  #     '--- | --- | --- | ---',
  #     ' 1  |  2  |  3  |  4 ',
  #     ' 5  |  6  |  7  |  8 ',
  #   ])
  #   return pxyf(x, y, f, new_line=1)
  # if not t_nested_3_levels(): return pf('!t_nested_3_levels')
  return 1
