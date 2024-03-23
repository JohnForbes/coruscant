def f(string, width, alignment):
  alignment_domain = {'left', 'centre', 'right'}
  if alignment not in alignment_domain: raise ValueError('\n'.join([
    'alignment not in expected domain',
    f'alignment_domain: {alignment_domain}'
  ]))
  if alignment == 'left': return f'{string:<{width}}'
  if alignment == 'centre': return f'{string:^{width}}'
  if alignment == 'right': return f'{string:>{width}}'
  raise NotImplementedError('\n'.join([
    'This line should be unreachable.',
    'Something has gone wrong.'
  ]))

def t():
  from hak.pxyz import f as pxyz
  from hak.pf import f as pf
  def t_left():
    x = {'string': 'foo', 'width': 5, 'alignment': 'left'}
    y = 'foo  '
    return pxyz(x, y, f(**x))
  if not t_left(): return pf('!t_left')
  def t_centre():
    x = {'string': 'foo', 'width': 5, 'alignment': 'centre'}
    y = ' foo '
    return pxyz(x, y, f(**x))
  if not t_centre(): return pf('!t_centre')
  def t_right():
    x = {'string': 'foo', 'width': 5, 'alignment': 'right'}
    y = '  foo'
    return pxyz(x, y, f(**x))
  if not t_right(): return pf('!t_right')
  def t_out_of_domain():
    x = {'string': 'foo', 'width': 4, 'alignment': 'elephant'}
    try: f(**x); return 0
    except ValueError: return 1
  if not t_out_of_domain(): return pf('!t_out_of_domain')
  return 1
