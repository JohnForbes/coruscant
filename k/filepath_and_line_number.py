class FilepathAndLineNumber:
  def __init__(self, filepath: str, line_number: int):
    self._filepath = filepath
    self._line_number = line_number
    self._initialized = True

  filepath = property(lambda self: self._filepath)
  line_number = property(lambda self: self._line_number)

f = lambda x: FilepathAndLineNumber(**x)

def t():
  from hak.pf import f as pf
  from hak.pxyz import f as pxyz

  def t_filepath():
    x = {'filepath': '/path/to/file.py', 'line_number': 10}
    return pxyz(x, x['filepath'], f(x).filepath)
  if not t_filepath(): return pf('!t_filepath')

  def t_line():
    x = {'filepath': '/path/to/file.py', 'line_number': 10}
    return pxyz(x, x['line_number'], f(x).line_number)
  if not t_line(): return pf('!t_line')

  def t_immutable():
    x = {'filepath': '/path/to/file.py', 'line_number': 10}
    z = f(x)
    try: z.filepath = "/new/path/to/file.py"; return pf('!t_immutable')
    except AttributeError: pass
    try: z.line_number = 20; return pf('!t_immutable')
    except AttributeError: pass
    return 1
  if not t_immutable(): return pf('!t_immutable')
  return 1
