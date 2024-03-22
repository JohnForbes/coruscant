def f(x):
  x = x[2:-3]
  _ = x.split('/')
  q, prefix, latch = set([]), '', 0
  while len(_):
    q.add(prefix+'.'.join(_))
    _ = _[1:]
    if not latch: latch = 1; prefix = '.'
  return q

def t():
  from hak.pf import f as pf
  from hak.pxyf import f as pxyf
  def t_a():
    y = set([
      'f.business_name.to_events',
      '.business_name.to_events',
      '.to_events'
    ])
    return pxyf('./f/business_name/to_events.py', y, f)
  if not t_a(): return pf('!t_a')
  if not pxyf('./gitter.py', set(['gitter']), f): return pf('!t_b')
  return 1
