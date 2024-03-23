from k.rates.aud import AUD
from k.rates.usd import USD
from k.rates.usd_instruments.rhi import RHI
from k.rates.ord import ORD
from k.rates.f import F

def f(x):
  if isinstance(x, int) and x == 0: return 1
  if isinstance(x, str) and x == '': return 1
  if isinstance(x, type(None)) and x is None: return 1
  if isinstance(x, dict):
    if isinstance(x, dict): return all([f(x[k]) for k in x])
    if x == dict(): return 1
  if isinstance(x, tuple) and x == tuple(): return 1
  for _rate in [AUD, USD, RHI, ORD, F]:
    if isinstance(x, _rate) and x == _rate(0): return 1
  return 0

def t():
  from hak.pf import f as pf
  from hak.pxyf import f as pxyf
  def t_int():
    if not pxyf(1, 0, f): return pf('!t_int_0')
    if not pxyf(0, 1, f): return pf('!t_int_1')
    return 1
  if not t_int(): return pf('!t_int')

  def t_str():
    if not pxyf('a', 0, f): return pf('!t_str_0')
    if not pxyf('', 1, f): return pf('!t_str_1')
    return 1
  if not t_str(): return pf('!t_str')

  if not pxyf(None, 1, f): return pf('!t_none')

  def t_dict():
    if not pxyf({'a': 1}, 0, f): return pf('!t_dict_0')
    if not pxyf({}, 1, f): return pf('!t_dict_1')
    if not pxyf({'a': {'b': AUD(0), 'c': AUD(1)}}, 0, f): return pf('!t_a_0')
    if not pxyf({'a': {'b': AUD(0), 'c': AUD(0)}}, 1, f): return pf('!t_a_1')
    return 1
  if not t_dict(): return pf('t_dict')

  def t_tuple():
    if not pxyf(('a', 0), 0, f): return pf('!t_tuple_0')
    if not pxyf(tuple(), 1, f): return pf('!t_tuple_1')
    return 1
  if not t_tuple(): return pf('!t_tuple')

  def t_non_zeroish_obj():
    class K: pass
    return pxyf(K(), 0, f)
  if not t_non_zeroish_obj(): return pf('!t_non_zeroish_obj')

  def t_aud():
    if not pxyf(AUD(1), 0, f): return pf('!t_aud_0')
    if not pxyf(AUD(0), 1, f): return pf('!t_aud_1')
    return 1
  if not t_aud(): return pf('!t_aud')

  return 1
