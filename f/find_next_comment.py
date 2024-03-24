def f():
  from hak.strings.filepaths.py.get import f as _list_py_files
  from hak.file.load import f as load_file
  from hak.string.colour.bright.cyan import f as cy
  from subprocess import run as sprun
  for pyfile in sorted(_list_py_files(root='.', filepaths=[])):
    lines = load_file(pyfile).split('\n')
    for i, l in enumerate(lines):
      _l = l.lstrip()
      if _l.startswith('# ') and not _l.startswith('# ignore_overlength_lines'):
        print('\n'.join([
          cy('Found next comment needing attention:'),
          f'{pyfile}:{i+1}',
          f'{repr(l)}'
        ]))
        sprun(args=['code', '-g', f'{pyfile}:{i+1}'])
        return

t = lambda: 1
