from k.block import Block as B
from typing import List

class Blocks:
  def __init__(self, blocks: List[B]):
    self._blocks = blocks
  
  blocks = property(lambda self: self._blocks)
  h_max = property(lambda s: max([b.h for b in s._blocks]))
  evened_heights = property(lambda s: s.to_blocks_with_evened_heights())

  __eq__ = lambda self, other: self.blocks == other.blocks
  __getitem__ = lambda self, i: self._blocks[i]  
  __iter__ = lambda self: iter(self._blocks)
  __len__ = lambda self: len(self.blocks)
  __repr__ = lambda self: self.__class__.__name__+'('+repr(self.blocks)+')'

  def to_blocks_with_evened_heights(self):
    h_max = self.h_max
    result = Blocks([b for b in self._blocks])
    for b in result:
      while b.h < h_max:
        b.append('')
    return Blocks(result)

  def hstack(self, margin=0) -> B:
    if not self._blocks: return B([])
    if len(self._blocks) == 1: return self._blocks[0]
    _blocks = self.evened_heights
    _lines = []
    _b_0 = _blocks[0]
    margins = []
    for i_line in range(_b_0.h):
      margins.append(margin)
    # print(margins)
    for i_line in range(_b_0.h):
      separator = ' '*margins[i_line]+'|'+' '*margins[i_line]
      _lines.append(separator.join([b[i_line] for b in _blocks]))
    return B(_lines)
  
  def vstack(self) -> B:
    def _f_blocks(blocks):
      lines = []
      w = max([b.w for b in blocks])
      for b in blocks[:-1]:
        lines += b.lines + ['-'*w]
      lines += blocks[-1].lines
      return B(lines)
    return (
      _f_blocks(self.blocks)
      if self.blocks
      else B([])
    )
  
  def append(self, block: B):
    if not isinstance(block, B): raise TypeError('\n'.join([
      'block is expected to be of type Block',
      f'observed type: {type(block)}',
      f'observed value: {block}'
    ]))
    self._blocks.append(block)

  top_lines = property(lambda self: [b.top_line for b in self._blocks])

  hstack_width = property(
    lambda s, margin: len(
      (' '*margin+'|'+' '*margin).join([b[0] for b in s._blocks])
    )
  )

f = lambda x: Blocks(**x)

def t():
  from hak.pf import f as pf
  from hak.pxyz import f as pxyz
  from hak.pxyf import f as pxyf

  def t_init():
    x = {'blocks': [B('a'), B('b')]}
    y = x['blocks']
    z = f(x).blocks
    return pxyz(x, y, z)
  if not t_init(): return pf('t_init')

  def t_hstack():
    def t_no_blocks():
      x = {'blocks': [B([])]}
      y = B([])
      z = f(x).hstack()
      return pxyz(x, y, z, new_line=1)
    if not t_no_blocks(): return pf('!t_no_blocks')
    def t_one_block():
      x = {'blocks': [B([
          "---------",
          "    Name ",
          "---------",
          "         ",
          "---------",
          "   Alice ",
          "     Bob ",
          " Charlie ",
          "---------",
        ])]
      }
      y = B([
        "---------",
        "    Name ",
        "---------",
        "         ",
        "---------",
        "   Alice ",
        "     Bob ",
        " Charlie ",
        "---------",
      ])
      z = f(x).hstack()
      return pxyz(x, y, z, new_line=1)
    if not t_one_block(): return pf('!t_one_block')
    def t_two_blocks():
      u = B([
        "---------",
        "    Name ",
        "---------",
        "         ",
        "---------",
        "   Alice ",
        "     Bob ",
        " Charlie ",
        "---------",
      ])
      v = B([
        "---------------",
        "          Info ",
        "-----|---------",
        " Age | Country ",
        "-----|---------",
        "  28 |     USA ",
        "  35 |  Canada ",
        "  22 |      UK ",
        "-----|---------",
      ])
      x = {'blocks': [u, v]}
      y = B([
        "---------|---------------",
        "    Name |          Info ",
        "---------|-----|---------",
        "         | Age | Country ",
        "---------|-----|---------",
        "   Alice |  28 |     USA ",
        "     Bob |  35 |  Canada ",
        " Charlie |  22 |      UK ",
        "---------|-----|---------",
      ])
      z = f(x).hstack()
      return pxyz(x, y, z, new_line=1)
    if not t_two_blocks(): return pf('!t_two_blocks')
    def t_mismatched_heights():
      x = {'blocks': [
        B(['       John ', '------------', ' Rei | Zenn ']),
        B([' James '])
      ]}
      y = B([
        "       John | James ",
        "------------|       ",
        " Rei | Zenn |       ",
      ])
      z = f(x).hstack()
      return pxyz(x, y, z, new_line=1)
    if not t_mismatched_heights(): return pf('!t_mismatched_heightblocks_s')
    return 1
  if not t_hstack(): return pf('t_hstack')

  def t_vstack():
    u = B([
      "---------------",
      "          Info ",
    ])
    v = B([
      " Age | Country ",
      "-----|---------",
      "  28 |     USA ",
      "  35 |  Canada ",
      "  22 |      UK ",
      "-----|---------",
    ])
    x = {'blocks': [u, v]}
    y = B([
      "---------------",
      "          Info ",
      "---------------",
      " Age | Country ",
      "-----|---------",
      "  28 |     USA ",
      "  35 |  Canada ",
      "  22 |      UK ",
      "-----|---------",
    ])
    z = f(x).vstack()
    return pxyz(x, y, z, new_line=1)
  if not t_vstack(): return pf('!t_vstack')

  def t_repr():
    x = {'blocks': [B('a'), B('b')]}
    return pxyz(x, "Blocks([Block(['a']), Block(['b'])])", repr(f(x)))
  if not t_repr(): return pf('!t_repr')

  def t_eq():
    x = {'blocks': [B('a'), B('b')]}
    return f(x) == f(x)
  if not t_eq(): return pf('!t_eq')

  def t_len():
    x = {'blocks': [B('a'), B('b')]}
    return pxyz(x, 2, len(f(x)))
  if not t_len(): return pf('!t_len')
  return 1
