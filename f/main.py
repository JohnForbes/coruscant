from k.block import Block
from typing import List

def f(dicts: List[dict], align: str='right') -> Block:
  if not isinstance(dicts, list): raise TypeError('\n'.join([
    'dicts is expected to be of type list',
    f'observed type: {type(dicts)}',
    f'observed value: {dicts}'
  ]))
  if len(dicts) == 0: return Block()
  if dicts[0] == {}: return Block()
  return Block([
    list(dicts[0].keys())[0],
    '-',
    *[d[list(dicts[0].keys())[0]] for d in dicts]
  ])

def t():
  from hak.pf import f as pf
  from hak.pxyz import f as pxyz
  from hak.pxyf import f as pxyf
  if not pxyf([{}], Block(), f): return pf('!t_simplest')

  def t_a():
    x = [{'a': 1}, {'a': 2}]
    y = Block(['a', '-', '1', '2'])
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

  return 1
