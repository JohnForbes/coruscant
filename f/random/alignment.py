from d.domains import alignment as domain
from k.alignment import Alignment as A

def f() -> A: from random import choice; return choice([A(a) for a in domain])
t = lambda: all([f() in domain for _ in range(100)])
