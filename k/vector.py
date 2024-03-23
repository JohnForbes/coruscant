from typing import List

class Vector:
  def __init__(self, values: List):
    self._data = values

  def _get_width(self): return -1
  def _get_type(self): return 'blergh'
  def _get_unit_str(self): return 'blergh'

  h = height = property(lambda self: len(self._data))
  w = width = property(lambda self: self._get_width)
  t = type = property(lambda self: self._get_type)
  u = unit = unit_str = property(lambda self: self._get_unit_str)

f = lambda x: Vector(**x)

def t():
  # def __init__(self, values: List):
  #   self._data = values
  # def _get_width(self): return -1
  # def _get_type(self): return 'blergh'
  # def _get_unit_str(self): return 'blergh'
  # h = height = property(lambda self: len(self._data))
  # w = width = property(lambda self: self._get_width)
  # t = type = property(lambda self: self._get_type)
  # u = unit = unit_str = property(lambda self: self._get_unit_str)
  return 1
