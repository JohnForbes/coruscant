from k.block import Block
from typing import List
from k.flat_container import FlatContainer as FC

def f(dicts: List[dict]) -> Block:
  if not isinstance(dicts, list): raise TypeError('\n'.join([
    'dicts is expected to be of type list',
    f'observed type: {type(dicts)}',
    f'observed value: {dicts}'
  ]))
  if len(dicts) == 0: return Block()
  if dicts[0] == {}: return Block()
  
  fc = FC(dicts)
  if len(fc.leaf_blocks) == 1: return fc.leaf_blocks[0]

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

  # def t_nested():
  #   x = [{'a': {'b': 1, 'c': 1}}, {'a': {'b': 2, 'c': 2}}]
  #   y = Block([
  #     '  a  ',
  #     '-----',
  #     'b | c',
  #     '--|--',
  #     '1 | 1',
  #     '2 | 2'
  #   ])
  #   z = f(x)
  #   return pxyz(x, y, z)
  # if not t_nested(): return pf('!t_nested')
  return 1
