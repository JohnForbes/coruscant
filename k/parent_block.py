from typing import List
from k.block import Block

class ParentBlock(Block):
  def __init__(
    self,
    name: str,
    blocks: List[Block]=[],
    do_upper_border: bool=False,
    do_lower_border: bool=False,
    do_left_border: bool=False,
    do_right_border: bool=False,
    do_vertical_lines: bool=False,
    do_horizontal_line_below_name: bool=True
  ):
    # Create lines object out of blocks data
    super().__init__([])

    # guarantee name is of correct type
    # guarantee name has valid value
    self._name = name

    # guarantee blocks is of correct type
    # guarantee blocks has valid value
    self._blocks = blocks

    # guarantee do_upper_border is of correct type
    # guarantee do_upper_border has valid value
    self._do_upper_border = do_upper_border

    # guarantee do_lower_border is of correct type
    # guarantee do_lower_border has valid value
    self._do_lower_border = do_lower_border

    # guarantee do_left_border is of correct type
    # guarantee do_left_border has valid value
    self._do_left_border = do_left_border

    # guarantee do_right_border is of correct type
    # guarantee do_right_border has valid value
    self._do_right_border = do_right_border

    # guarantee do_vertical_lines is of correct type
    # guarantee do_vertical_lines has valid value
    self._do_vertical_lines = do_vertical_lines

    # guarantee do_horizontal_line_below_name is of correct type
    # guarantee do_horizontal_line_below_name has valid value
    self._do_horizontal_line_below_name = do_horizontal_line_below_name

  block_count = property(lambda self: self.len(self._blocks))

f = lambda x: ParentBlock(**x)

def t():
  x = {
    'name': None,
    'blocks': None,
    'do_upper_border': None,
    'do_lower_border': None,
    'do_left_border': None,
    'do_right_border': None,
    'do_vertical_lines': None,
    'do_horizontal_line_below_name': None
  }
  # Create block expectation to properly test intended functionality
  y = Block()
  z = f(x)
  from hak.pxyz import f as pxyz
  return pxyz(x, y, z)

# t_name
# t_blocks
# t_do_upper_border
# t_do_lower_border
# t_do_left_border
# t_do_right_border
# t_do_vertical_lines
# t_do_horizontal_line_below_name
