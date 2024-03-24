class Line:
  def __init__(self, string: str, number: int):
    self._string = string
    self._number = number
    self._initialized = True
  
  string = property(lambda self: self._string)
  number = property(lambda self: self._number)
  __str__ = lambda self: f'{self.line_number}: {self.line}'

f = lambda x: Line(**x)

def t():
  from hak.pf import f as pf
  from hak.pxyz import f as pxyz

  def t_line():
    x = {'string': 'def f():', 'number': 10}
    return pxyz(x, x['string'], f(x).string)
  if not t_line(): return pf('!t_line')

  def t_line_number():
    x = {'string': 'def f():', 'number': 10}
    return pxyz(x, x['number'], f(x).number)
  if not t_line_number(): return pf('!t_line_number')

  def t_immutable():
    x = {'string': 'def f():', 'number': 10}
    z = f(x)
    try: z.string = "def g():"; return pf('!t_immutable')
    except AttributeError: pass
    try: z.number = 20; return pf('!t_immutable')
    except AttributeError: pass
    return 1
  if not t_immutable(): return pf('!t_immutable')
  return 1
