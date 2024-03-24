from k.block import Block as B
from typing import List

class Blocks:
  def __init__(self, blocks: List[B]):
    self._blocks = blocks
  
  __iter__ = lambda self: iter(self._blocks)
  __getitem__ = lambda self, i: self._blocks[i]

  h_max = property(lambda s: max([b.h for b in s._blocks]))

  blocks = property(lambda self: self._blocks)

  def to_blocks_with_normalised_heights(self):
    h_max = self.h_max
    result = Blocks([b for b in self._blocks])
    for b in result:
      while b.h < h_max:
        b.append('')
    return Blocks(result)

  normalised_heights = property(lambda s: s.to_blocks_with_normalised_heights())

  def hstack(self) -> B:
    if not self._blocks: return B([])
    if len(self._blocks) == 1: return self._blocks[0]
    _blocks = self.normalised_heights
    _lines = []
    _b_0 = _blocks[0]
    for i_line in range(_b_0.h):
      _lines.append('|'.join([b[i_line] for b in _blocks]))
    return B(_lines)

f = lambda x: Blocks(**x)

def t():
  from hak.pf import f as pf
  from hak.pxyz import f as pxyz

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
  return 1
