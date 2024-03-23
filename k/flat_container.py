from typing import List
from k.vector import Vector

class FlatContainer:
  def __init__(self, dicts: List[dict]):
    self._dicts = dicts
    self._dict = {}
    for d in dicts:
      d_flat = flatten(d)
      for k in d_flat:
        if k not in self._dict: self._dict[k] = []
        self._dict[k].append(d_flat[k])

    self._vectors = {k: Vector(self._dict[k]) for k in self._dict}    

  record_count = property(lambda self: len(self._dicts))
  vector_count = property(lambda self: len(self._dict))
  vectors = property(lambda self: self._vectors)

  _filter_zeroish = lambda self: {
    k: self._vectors[k]
    for k in self._vectors
    if not self._vectors[k].is_zeroish
  }

  non_zeroish_vectors = property(lambda self: self._filter_zeroish())

from f.dict.nested.flatten import f as flatten

f = lambda x: FlatContainer(**x)

def t():
  from hak.pf import f as pf
  from hak.pxyz import f as pxyz
  def t_a():
    x = {
      'dicts': [
        {'a': {'b': 0, 'c': 0}, 'e': {'g': {'h': 6}}},
        {'a': {'b': -1, 'c': 1}, 'e': {'g': {'h': 7}}},
        {'a': {'b': -2, 'c': 2}, 'e': {'g': {'h': 8}}},
      ]
    }
    y = {
      ('a', 'b'): Vector([0, -1, -2]),
      ('a', 'c'): Vector([0, 1, 2]),
      ('e', 'g', 'h'): Vector([6, 7, 8])
    }
    z = f(x).vectors
    return pxyz(x, y, z)
  if not t_a(): return pf('!t_a')

  def t_b():
    x = {
      'dicts': [
        {'a': {'b': 0, 'c': 0}, 'e': {'g': {'h': 6}}},
        {'a': {'b': 0, 'c': 1}, 'e': {'g': {'h': 7}}},
        {'a': {'b': 0, 'c': 2}, 'e': {'g': {'h': 8}}},
      ]
    }
    y = {
      ('a', 'c'): Vector([0, 1, 2]),
      ('e', 'g', 'h'): Vector([6, 7, 8])
    }
    z = f(x).non_zeroish_vectors
    return pxyz(x, y, z)
  if not t_b(): return pf('!t_b')
  return 1
