from typing import List
from f.string_width_and_alignment.to_aligned_string import f as _f_align
from k.alignment import Alignment as A

class Block:
  def __init__(self, lines: List, alignment: A=A('centre')):
    self._lines = lines
    if not isinstance(alignment, A): raise TypeError('\n'.join([
      'alignment must be of type Alignment',
      f'observed type: {type(alignment)}',
      f'observed value: {alignment}'
    ]))
    self._alignment = alignment

  w = width = property(lambda s: max([len(str(l)) for l in s._lines]))
  lines = property(lambda s: [_f_align(l, s.w, s._alignment) for l in s._lines])
  h = height = property(lambda s: len(s._lines))
  __eq__ = lambda u, v: u.lines == v.lines
  __str__ = lambda s: '\n'.join(s.lines)
  __getitem__ = lambda self, index: self.lines[index]

  def append(s, line: str):
    s._lines += line.split('\n') if '\n' in line else [line]

f = lambda x: Block(**x)

def t():
  from hak.pf import f as pf
  from hak.pxyz import f as pxyz
  from f.random.alignment import f as rand_alignment
  def t___init__():
    x = {'lines': [0, 'foo', 1.23], 'alignment': A('left')}
    return pxyz(x, [0, 'foo', 1.23], f(x)._lines)
  if not t___init__(): return pf('!t___init__')
  
  def t_width():
    x = {'lines': [0, 'foo', 1.23], 'alignment': A('left')}
    return pxyz(x, 4, f(x).width)
  if not t_width(): return pf('!t_width')

  def t_w():
    x = {'lines': [0, 'foo', 1.23], 'alignment': A('left')}
    return pxyz(x, 4, f(x).w)
  if not t_w(): return pf('!t_w')

  def t_lines():
    x = {'lines': [0, 'foo', 1.23], 'alignment': A('left')}
    return pxyz(x, ['0   ', 'foo ', '1.23'], f(x).lines)
  if not t_lines(): return pf('!t_lines')

  def t_height():
    x = {'lines': [0, 'foo', 1.23], 'alignment': A('left')}
    return pxyz(x, 3, f(x).height)
  if not t_height(): return pf('!t_height')

  def t_h():
    x = {'lines': [0, 'foo', 1.23], 'alignment': A('left')}
    return pxyz(x, 3, f(x).h)
  if not t_h(): return pf('!t_h')

  def t___eq__():
    _alignment = rand_alignment()
    return Block([], _alignment) == Block([], _alignment)
  if not t___eq__(): return pf('!t___eq__')

  def t___str__():
    x = {'lines': ['a', '-', 0], 'alignment': A('left')}
    return pxyz(x, ['a\n-\n0'], [str(f(x))])
  if not t___str__(): return pf('!t___str__')

  def t_append_line():
    _alignment = rand_alignment()
    block = Block([], _alignment)
    x = 'boo\nfoo'
    block.append(x)
    return pxyz(x, ['boo', 'foo'], block.lines)
  if not t_append_line(): return pf('!t_append_line')

  def t_get_item():
    x = {'lines': ['a', 'b', 'c'], 'alignment': rand_alignment()}
    return pxyz(x, 'b', f(x)[1])
  if not t_get_item(): return pf('!t_get_item')

  def t_alignment_te():
    x = {'lines': ['a', 'b', 'c'], 'alignment': 'boom!'}
    try: f(x); return 0
    except TypeError: return 1
  if not t_alignment_te(): return pf('!t_alignment_te')
  return 1
