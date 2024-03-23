from k.string import String
class Alignment(String):
  def __init__(self, value: str):
    from d.domains import alignment as alignment_domain
    if value not in alignment_domain: raise ValueError('\n'.join([
      'value not in expected domain',
      f'alignment_domain: {alignment_domain}'
    ]))
    super().__init__(value)

  __hash__ = lambda self: hash(self._value)

f = lambda x: Alignment(**x)

def t():
  from hak.pf import f as pf
  from hak.pxyz import f as pxyz
  def t_a():
    from f.random.alignment import f as rand_alignment
    x = {'value': str(rand_alignment())}
    return pxyz(x, x['value'], str(f(x)))
  if not t_a(): return pf('!t_a')
