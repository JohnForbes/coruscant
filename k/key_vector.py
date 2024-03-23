from k.vector import Vector

class KeyVector:
  def __init__(self, key: str, vector: Vector):
    # guarantee key is of type str
    self._k = key

    # guarantee vector is of type vector
    self._v = vector
  
  def _get_unit_str(self):
    # consider type when generating this output
    return ''

  def _get_width(self):
    # consider vector width
    # consider key width
    # consider unit width
    return -1

  t = type = property(lambda self: self._v.type)
  u = unit = unit_str = property(lambda self: self._v.unit_str)
  w = width = property(lambda self: self._get_width())

f = lambda x: KeyVector(**x)

# fix this t
t = lambda: 1

# test that width is an int
# test that width is in [0, inf]
# test that width is sensible given the data
# t_type
# t_unit
# t_width
