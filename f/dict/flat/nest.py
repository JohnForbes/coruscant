def f(x=None):
  nested_dict = {}
  for keys, value in x.items():
    current_dict = nested_dict
    for key in keys[:-1]:
      if key not in current_dict:
        current_dict[key] = {}
      current_dict = current_dict[key]
    current_dict[keys[-1]] = value
  return nested_dict

def t():
  x = {('a', 'b'): 1, ('a', 'c', 'd'): 2, ('e',): 3}
  y = {'a': {'b': 1, 'c': {'d': 2}}, 'e': 3}
  from hak.pxyf import f as pxyf
  return pxyf(x, y, f)
