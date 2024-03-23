def f(x=None):
  def flatten(dictionary, parent_keys=()):
    flat_dict = {}
    for k, v in dictionary.items():
      if isinstance(v, dict):
        flat_dict.update(flatten(v, parent_keys + (k,)))
      else:
        flat_dict[parent_keys + (k,)] = v
    return flat_dict
  return flatten(x)

def t():
  x = {'a': {'b': 1, 'c': {'d': 2}}, 'e': 3}
  y = {('a', 'b'): 1, ('a', 'c', 'd'): 2, ('e',): 3}
  from hak.pxyf import f as pxyf
  return pxyf(x, y, f)
