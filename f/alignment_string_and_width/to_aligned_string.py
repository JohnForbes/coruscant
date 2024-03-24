from k.alignment import Alignment as A

def f(alignment: A, string: str, width: int) -> str:
  if not isinstance(alignment, A):
    raise TypeError(f'alignment must be Alignment, got {type(alignment)}')
  if not isinstance(string, str):
    raise TypeError(f'string must be str, got {type(string)}')
  if not isinstance(width, int):
    raise TypeError(f'width must be int, got {type(width)}')
  if alignment == A('left'): return f'{string:<{width}}'
  if alignment == A('centre'): return f'{string:^{width}}'
  if alignment == A('right'): return f'{string:>{width}}'
  raise NotImplementedError('\n'.join([
    'This line should be unreachable.',
    'Something went wrong.'
    f'string: {string}',
    f'type(string): {type(string)}',
    f'width: {width}',
    f'type(width): {type(width)}',
    f'alignment: {alignment}',
    f'type(alignment): {type(alignment)}',
  ]))

def t():
  from hak.pf import f as pf
  from hak.pxyz import f as pxyz
  def t_left():
    x = {'string': 'foo', 'width': 5, 'alignment': A('left')}
    return pxyz(x, 'foo  ', f(**x))
  if not t_left(): return pf('!t_left')
  def t_centre():
    x = {'string': 'foo', 'width': 5, 'alignment': A('centre')}
    return pxyz(x, ' foo ', f(**x))
  if not t_centre(): return pf('!t_centre')
  def t_right():
    x = {'string': 'foo', 'width': 5, 'alignment': A('right')}
    return pxyz(x, '  foo', f(**x))
  if not t_right(): return pf('!t_right')
  return 1
