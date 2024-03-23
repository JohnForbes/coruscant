from k.rates.named import NamedRate
from hak.rate import Rate as R

class AUD(NamedRate):
  def __init__(self, numerator=0, denominator=1):
    super().__init__('AUD', numerator, denominator)

  def __add__(l, r):
    if isinstance(r, AUD): return AUD(l.n * r.d + r.n * l.d, l.d * r.d)
    elif isinstance(r, R):
      if r.unit == {'AUD': 1}: return l + AUD(r.n, r.d)
      else: raise NotImplementedError('!15: branch not yet written')
    elif isinstance(r, (int, float)): return l + AUD(r, 1)
    else: raise TypeError('Unsupported operand type for +')
  
  def __mul__(u, v):
    _ = super().__mul__(v)
    return AUD(_.n, _.d)
  
f = lambda x: AUD(**x)

def t():
  from hak.pf import f as pf
  from hak.pxyz import f as pxyz
  def t_a():
    x = {'numerator': 1, 'denominator': 2}
    return pxyz(x, R(1, 2, {'AUD': 1}).to_dict(), f(x).to_dict())
  if not t_a(): return pf('!t_a')

  def t_to_init_str():
    def t_to_init_str_n_d():
      x = {'numerator': 1, 'denominator': 2}
      return pxyz(x, 'AUD(1, 2)', f(x).to_init_str())
    if not t_to_init_str_n_d(): return pf('!t_to_init_str_n_d')
    def t_to_init_str_n():
      x = {'numerator': 2, 'denominator': 1}
      return pxyz(x, 'AUD(2)', f(x).to_init_str())
    if not t_to_init_str_n(): return pf('!t_to_init_str_n')
    return 1
  if not t_to_init_str(): return pf('!t_to_init_str')
  return 1
