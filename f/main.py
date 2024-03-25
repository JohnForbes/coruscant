from k.block import Block
from typing import List
from k.flat_container import FlatContainer as FC
from k.parent_block import ParentBlock as PB
from f.dict.flat.nest import f as nest
from k.leaf_block import LeafBlock as LB
from k.blocks import Blocks as Bs
from k.block import Block as B

def _accumulate(x, path_so_far=['α']):
  if isinstance(x, dict):
    _blocks = Bs(blocks=[])
    for k in x:
      if isinstance(x[k], B):
        _blocks.append(x[k])
      else:
        _blocks.append(_accumulate(x[k], path_so_far + [k]))
    return PB(tuple(path_so_far), 1, _blocks)
  else:
    if isinstance(x, B):
      return x
    else:
      raise TypeError('\n'.join([
        'x is expected to be either a Block or a dict',
        f'observed type: {type(x)}',
        f'observed value: {x}'
      ]))

def f(dicts: List[dict]) -> Block:
  if not isinstance(dicts, list): raise TypeError('\n'.join([
    'dicts is expected to be of type list',
    f'observed type: {type(dicts)}',
    f'observed value: {dicts}'
  ]))
  if len(dicts) == 0: return Block()
  if dicts[0] == {}: return Block()
  d = nest(FC(dicts).leaf_blocks_as_flat_dict)
  return B(lines=_accumulate(d).lines[2:])

def t():
  from hak.pf import f as pf
  from hak.pxyz import f as pxyz
  from hak.pxyf import f as pxyf
  if not pxyf([{}], Block(), f): return pf('!t_simplest')

  def t_a():
    x = [{'a': 1}, {'a': 2}]
    y = Block([' a ', '---', 'int', '---', ' 1 ', ' 2 '])
    z = f(x)
    if z is None: return pf([
      'z is None',
      f'x: {x}',
      f'[y]: {[y]}',
      f'[z]: {[z]}'
    ])
    return pxyz(x, y, z, new_line=1)
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
    z = f(x)
    return pxyz(x, y, z, new_line=1)
  if not t_nested_2_levels(): return pf('!t_nested_2_levels')

  def t_nested_3_levels():
    x = [
      {'a': {'b': {'c': 1, 'd': 2}, 'e': {'g': 3, 'h': 4}}},
      {'a': {'b': {'c': 5, 'd': 6}, 'e': {'g': 7, 'h': 8}}}
    ]
    y = Block([
      '          a          ',
      '---------------------',
      '    b     |     e    ',
      '--------- | ---------',
      ' c  |  d  |  g  |  h ',
      '--- | --- | --- | ---',
      'int | int | int | int',
      '--- | --- | --- | ---',
      ' 1  |  2  |  3  |  4 ',
      ' 5  |  6  |  7  |  8 ',
    ])
    z = f(x)
    return pxyz(x, y, z, new_line=1)
  if not t_nested_3_levels(): return pf('!t_nested_3_levels')

  def t_very_long_name():
    x = [
      {'very_very_long_name': {'b': 'y', 'c': 2, 'd': 3}},
      {'very_very_long_name': {'b': 'd', 'c': 5, 'd': 6}},
    ]
    y = Block([
      'very_very_long_name',
      '-------------------',
      '  b   |  c  |  d   ',
      '----- | --- | -----',
      ' str  | int | int  ',
      '----- | --- | -----',
      '  y   |  2  |  3   ',
      '  d   |  5  |  6   ',
    ])
    z = f(x)
    return pxyz(x, y, z, new_line=1)
  if not t_very_long_name(): return pf('!t_very_long_name')
  return 1
