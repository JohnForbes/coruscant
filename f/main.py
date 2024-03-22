def f(x):
  if not x: return ''
  k = list(x.keys())[0] 
  v = x[k]
  return '\n'.join([k, '-', v])

def t():
  from hak.pf import f as pf
  from hak.pxyz import f as pxyz
  def t_simplest():
    x = {}
    y = ''
    z = f(x)
    return pxyz(x, y, z)
  if not t_simplest(): return pf('!t_simplest')

  def t_a():
    from f.random.string import f as rand_str
    k = rand_str(max_length=1)
    from random import randint; v = str(randint(a=0, b=9))
    x = {k: v}
    y = '\n'.join([k, '-', v])
    z = f(x)
    return pxyz(x, [y], [z])
  if not t_a(): return pf('!t_a')

  return 1
