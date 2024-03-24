def f(filepath: str, content: str):
  with open(filepath, 'w') as φ:
    φ.write(content)
    return content

def t():
  from hak.pf import f as pf
  _root = './temp_save_string'
  _filepath = f'{_root}/temp.txt'
  from os.path import exists
  from os import mkdir
  from f.obj.nop import f as nop
  up = lambda: (mkdir if not exists(_root) else nop)(_root)
  up()

  x_content = 'apple'
  result = f(_filepath, x_content)

  def dn():
    if exists(_filepath):
      from os import remove
      remove(_filepath)
    from os import rmdir; rmdir(_root)

  if not exists(_filepath):
    dn()
    return pf(f'{_filepath} file was not created by file.write.run()')

  with open(_filepath, 'r') as _file:
    file_content = _file.read()

  if file_content != x_content:
    dn()
    return pf(f'{file_content} != {x_content}')

  if result != x_content:
    dn()
    return pf(f'{result} != {x_content}')

  dn()
  return 1
