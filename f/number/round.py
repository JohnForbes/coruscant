from f.number.get_sign import f as sign
from math import floor

f = lambda x: sign(x)*floor(abs(x)+0.5)

def t():
  from hak.pxyf import f as pxyf
  from hak.pf import f as pf
  if not pxyf( 1.5,  2, f): return pf('!t_a')
  if not pxyf( 1.4,  1, f): return pf('!t_b')
  if not pxyf( 0.5,  1, f): return pf('!t_c')
  if not pxyf( 0.4,  0, f): return pf('!t_d')
  if not pxyf( 0.0,  0, f): return pf('!t_e')
  if not pxyf(-0.5, -1, f): return pf('!t_f')
  if not pxyf(-0.4,  0, f): return pf('!t_g')
  if not pxyf(-1.4, -1, f): return pf('!t_h')
  if not pxyf(-1.5, -2, f): return pf('!t_i')
  return 1
