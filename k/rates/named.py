from hak.rate import Rate as R

class NamedRate(R):
  def __init__(self, name, numerator=0, denominator=1):
    super().__init__(numerator, denominator, unit={name: 1})

  name = property(lambda self: list(self.unit.keys())[0])

  def to_init_str(s):
    _ = '' if s.d == 1 else f', {s.d}'
    __ = f'{s.n}{_}' if float(s) != 0 else ''
    return f'{s.name}({__})'

f = lambda x: NamedRate(**x)

def t():
  from hak.pf import f as pf
  from hak.pxyz import f as pxyz
  def t_a():
    x = {'numerator': 1, 'denominator': 2, 'name': 'AUD'}
    return pxyz(x, R(1, 2, {'AUD': 1}).to_dict(), f(x).to_dict())
  if not t_a(): return pf('!t_a')

  def t_to_init_str():
    def t_to_init_str_n_d():
      x = {'numerator': 1, 'denominator': 2, 'name': 'FOO'}
      return pxyz(x, 'FOO(1, 2)', f(x).to_init_str())
    if not t_to_init_str_n_d(): return pf('!t_to_init_str_n_d')
    def t_to_init_str_n():
      x = {'numerator': 2, 'denominator': 1, 'name': 'FOO'}
      return pxyz(x, 'FOO(2)', f(x).to_init_str())
    if not t_to_init_str_n(): return pf('!t_to_init_str_n')
    def t_to_init_str_0():
      x = {'numerator': 0, 'denominator': 1, 'name': 'FOO'}
      return pxyz(x, 'FOO()', f(x).to_init_str())
    if not t_to_init_str_0(): return pf('!t_to_init_str_0')
    return 1
  if not t_to_init_str(): return pf('!t_to_init_str')
  return 1
