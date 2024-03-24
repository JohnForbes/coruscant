from k.block import Block as B
from k.alignment import Alignment as A

# is_block
f = lambda b: isinstance(b, B)
t = lambda: all([
  f(B(['---', '   ', '---'], alignment=A('centre'))),
  not f(['---', '   ', '---']),
])
