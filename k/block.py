from typing import List

class Block:
  def __init__(self, lines: List=[]): self._lines = lines
  w = width = property(lambda s: max([len(str(l)) for l in s._lines]))
  lines = property(lambda s: [f'{l:<{s.w}}' for l in s._lines])
  h = height = property(lambda s: len(s._lines))
  __eq__ = lambda u, v: u.lines == v.lines
  __str__ = lambda s: '\n'.join(s.lines)
  __getitem__ = lambda self, index: self.lines[index]

  def append(s, line: str):
    s._lines += line.split('\n') if '\n' in line else [line]

f = lambda x: Block(**x)

def t():
  from hak.pxyz import f as pxyz
  from hak.pf import f as pf
  def t___init__():
    x = {'lines': [0, 'foo', 1.23]}
    return pxyz(x, [0, 'foo', 1.23], f(x)._lines)
  if not t___init__(): return pf('!t___init__')
  
  def t_width():
    x = {'lines': [0, 'foo', 1.23]}
    return pxyz(x, 4, f(x).width)
  if not t_width(): return pf('!t_width')

  def t_w():
    x = {'lines': [0, 'foo', 1.23]}
    return pxyz(x, 4, f(x).w)
  if not t_w(): return pf('!t_w')

  def t_lines():
    x = {'lines': [0, 'foo', 1.23]}
    return pxyz(x, ['0   ', 'foo ', '1.23'], f(x).lines)
  if not t_lines(): return pf('!t_lines')

  def t_height():
    x = {'lines': [0, 'foo', 1.23]}
    return pxyz(x, 3, f(x).height)
  if not t_height(): return pf('!t_height')

  def t_h():
    x = {'lines': [0, 'foo', 1.23]}
    return pxyz(x, 3, f(x).h)
  if not t_h(): return pf('!t_h')

  t___eq__ = lambda: Block() == Block()
  if not t___eq__(): return pf('!t___eq__')

  def t___str__():
    x = {'lines': ['a', '-', 0]}
    return pxyz(x, ['a\n-\n0'], [str(f(x))])
  if not t___str__(): return pf('!t___str__')

  def t_append_line():
    block = Block()
    x = 'boo\nfoo'
    block.append(x)
    return pxyz(x, ['boo', 'foo'], block.lines)
  if not t_append_line(): return pf('!t_append_line')

  def t_get_item():
    x = {'lines': ['a', 'b', 'c']}
    return pxyz(x, 'b', f(x)[1])
  if not t_get_item(): return pf('!t_get_item')
  return 1
