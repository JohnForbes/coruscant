class String:
  def __init__(self, value: str):
    if not isinstance(value, str):
      raise TypeError('\n'.join([
        'value must be of type str',
        f'observed type: {type(value)}',
        f'observed value: {value}'
      ]))
    self._value = value
  __str__ = lambda self: str(self._value)
  w = width = property(lambda self: len(self._value))
  __eq__ = lambda left, right: str(left) == str(right)
  __format__ = lambda self, format_spec: str(self).__format__(format_spec)
  __repr__ = lambda self: self.__class__.__name__+'('+repr(self._value)+')'
  __hash__ = lambda self: hash(self._value)

f = lambda x: String(**x)

def t():
  from hak.pf import f as pf
  from hak.pxyz import f as pxyz
  def t_init_and_to_string():
    x = {'value': 'abc'}
    return pxyz(x, x['value'], str(f(x)))
  if not t_init_and_to_string(): return pf('!t_init_and_to_string')

  def t_w():
    x = {'value': 'abc'}
    return pxyz(x, len(x['value']), f(x).w)
  if not t_w(): return pf('!t_w')

  def t_type_error():
    def t_type_error_0():
      x = {'value': 'abc'}
      try: f(x); return 1
      except TypeError: return 0
    if not t_type_error_0(): return pf('!t_type_error_0')
    def t_type_error_1():
      class K: pass
      x = {'value': K()}
      try: f(x); return 0
      except TypeError: return 1
    if not t_type_error_1(): return pf('!t_type_error_1')
    return 1
  if not t_type_error(): return pf('!t_type_error')

  def t_eq():
    def t_eq_0(): return String('A') != String('B')
    if not t_eq_0(): return pf('!t_eq_0')
    def t_eq_1(): return String('A') == String('A')
    if not t_eq_1(): return pf('!t_eq_1')
    return 1
  if not t_eq(): return pf('!t_eq')

  def t_hash():
    x = {'value': 'abc'}
    return hash(x['value']) == hash(f(x))
  if not t_hash(): return pf('!t_hash')
  return 1
