from k.string import String
class Name(String):
  def __init__(self, value: str):
    super().__init__(value)

f = lambda x: String(**x)

def t():
  from hak.pxyz import f as pxyz
  x = {'value': 'abc'}
  return pxyz(x, x['value'], str(f(x)))
