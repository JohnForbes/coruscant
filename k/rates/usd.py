from k.rates.named import NamedRate

class USD(NamedRate):
  def __init__(self, numerator=0, denominator=1):
    super().__init__('USD', numerator, denominator)

  def __add__(l, r):
    if isinstance(r, USD): return USD(l.n * r.d + r.n * l.d, l.d * r.d)
    elif isinstance(r, NamedRate):
      if r.unit == {'USD': 1}: return l + USD(r.n, r.d)
      else: raise NotImplementedError('!15: branch not yet written')
    elif isinstance(r, (int, float)): return l + USD(r, 1)
    else: raise TypeError('Unsupported operand type for +')

f = lambda x: USD(**x)

def t():
  from hak.pf import f as pf
  from hak.rate import Rate as R
  from hak.pxyz import f as pxyz
  def t_a():
    x = {'numerator': 1, 'denominator': 2}
    return pxyz(x, R(1, 2, {'USD': 1}).to_dict(), f(x).to_dict())
  if not t_a(): return pf('!t_a')

  def t_to_init_str():
    def t_to_init_str_n_d():
      x = {'numerator': 1, 'denominator': 2}
      return pxyz(x, 'USD(1, 2)', f(x).to_init_str())
    if not t_to_init_str_n_d(): return pf('!t_to_init_str_n_d')
    def t_to_init_str_n():
      x = {'numerator': 2, 'denominator': 1}
      return pxyz(x, 'USD(2)', f(x).to_init_str())
    if not t_to_init_str_n(): return pf('!t_to_init_str_n')
    return 1
  if not t_to_init_str(): return pf('!t_str')
  return 1
