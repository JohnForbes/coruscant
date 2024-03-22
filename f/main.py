from k.block import Block

def f(x: dict) -> Block:
  if not isinstance(x, dict): raise TypeError('\n'.join([
    'x is expected to be of type dict',
    f'observed type: {type(x)}'
    f'observed value: {x}'
  ]))
  if not x: return Block()
  k = list(x.keys())[0] 
  v = x[k]
  return Block([k, '-', v])

def t():
  from hak.pf import f as pf
  from hak.pxyz import f as pxyz
  from hak.pxyf import f as pxyf
  if not pxyf({}, Block(), f): return pf('!t_simplest')

  def t_a():
    from f.random.string import f as rand_str
    k = rand_str(max_length=1)
    from random import randint; v = str(randint(a=0, b=9))
    x = {k: v}
    y = Block([k, '-', v])
    z = f(x)
    return pxyz(x, [y], [z])
  if not t_a(): return pf('!t_a')

  def t_throw_if_not_dict():
    def t_throw_if_not_dict_0():
      x = 'blergh'
      y = 'x is expected to be of type dict'
      try:
        f(x)
      except TypeError as te:
        if y not in str(te): return pf('y not in te')
      return 1
    if not t_throw_if_not_dict_0(): return pf('!t_throw_if_not_dict_0')
    def t_throw_if_not_dict_1():
      x = {'blergh': 'blargh'}
      f(x)
      return 1
    if not t_throw_if_not_dict_1(): return pf('!t_throw_if_not_dict_1')
    return 1
  if not t_throw_if_not_dict(): return pf('!t_throw_if_not_dict')
  return 1
