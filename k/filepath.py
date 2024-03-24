from k.string import String
class Filepath(String):
  def __init__(self, value: str):
    super().__init__(value)

  file_name = property(lambda self: self._v.split('/')[-1])
  file_extension = property(lambda self: self._v.split('.')[-1])
  directory = property(lambda self: '/'.join(self._v.split('/')[:-1]))
  parent_directory = property(lambda self: '/'.join(self._v.split('/')[:-2]))
  absolute_path = property(lambda self: self._v)

  def _get_exists(self): from os.path import exists; return exists(self._v)
  exists = property(lambda self: self._get_exists)
  does_not_exist = property(lambda self: not self.exists)

f = lambda x: Filepath(**x)

def t():
  from hak.pxyz import f as pxyz
  x = {'value': 'abc'}
  return pxyz(x, x['value'], str(f(x)))
