from k.rates.named import NamedRate

class ORD(NamedRate):
  def __init__(self, numerator=0, denominator=1):
    super().__init__('ORD', numerator, denominator)

f = lambda x: ORD(**x)

def t():
  from hak.pf import f as pf
  from hak.pxyz import f as pxyz
  def t_a():
    x = {'numerator': 1, 'denominator': 2}
    from hak.rate import Rate as R
    return pxyz(x, R(1, 2, {'ORD': 1}).to_dict(), f(x).to_dict())
  if not t_a(): return pf('!t_a')

  def t_to_init_str():
    def t_to_init_str_n_d():
      x = {'numerator': 1, 'denominator': 2}
      return pxyz(x, 'ORD(1, 2)', f(x).to_init_str())
    if not t_to_init_str_n_d(): return pf('!t_to_init_str_n_d')
    def t_to_init_str_n():
      x = {'numerator': 2, 'denominator': 1}
      return pxyz(x, 'ORD(2)', f(x).to_init_str())
    if not t_to_init_str_n(): return pf('!t_to_init_str_n')
    return 1
  if not t_to_init_str(): return pf('!t_str')
  return 1
