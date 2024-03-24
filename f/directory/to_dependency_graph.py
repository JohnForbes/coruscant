from f.string.filepath.to_import_paths import f as f2i
from hak.file.load import f as load
from os.path import exists

def f(filepaths):
  _fps = filepaths
  _fps = [_ for _ in _fps if _.endswith('.py')]
  _fps = [_ for _ in _fps if exists(_)]

  _import_path_to_filepath = {}
  for _fp in _fps:
    _import_paths = f2i(_fp)
    for _ip in _import_paths:
      _import_path_to_filepath[_ip] = _fp

  dependencies = {_fp: set([]) for _fp in _fps}

  for _fp in _fps:
    content = load(_fp)
    for _ip in _import_path_to_filepath:
      _ip_1 = f'{_ip} import '
      if _fp != _import_path_to_filepath[_ip]:
        if any([
          '.'+_ip_1 in content,
          ' '+_ip_1 in content
        ]):
          dependencies[_fp].add(_import_path_to_filepath[_ip])

  return dependencies

def t():
  from hak.directory.filepaths.get import f as get_filepaths
  def up():
    from hak.directory.make import f as mkdir
    _temp_dir = '../_temp'
    mkdir(_temp_dir)
    from hak.file.save import f as save
    _files = {
      'a.py': '\n'.join([
        'from .b import f as f_b',
        'from .c import f as f_c',
        'f = lambda x: f_b(x) + f_c(x)',
        't = lambda: 1',
        ''
      ]),
      'b.py': '\n'.join([
        'from .c import f as f_c',
        'f = lambda x: f_c(x)',
        't = lambda: 1',
        ''
      ]),
      'c.py': '\n'.join([
        'f = lambda x: x+1',
        't = lambda: 1',
        ''
      ])
    }
    for _ in _files: save(f'{_temp_dir}/{_}', _files[_])
    return _temp_dir
  temp_dir = up()
  x = get_filepaths(filepaths=[], root=temp_dir)
  y = {
    f'{temp_dir}/a.py': {f'{temp_dir}/c.py', f'{temp_dir}/b.py'},
    f'{temp_dir}/c.py': set(),
    f'{temp_dir}/b.py': {f'{temp_dir}/c.py'}
  }
  z = f(x)
  def dn(temp_dir):
    from hak.directory.remove import f as remove_dir
    remove_dir(temp_dir)
  dn(temp_dir)
  from hak.pxyz import f as pxyz
  return pxyz(x, y, z)
