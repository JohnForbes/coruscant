from os.path import exists

def f(directory, filepaths=[]):
  if not exists(directory): return
  from os import listdir
  from os.path import isdir
  from os import remove
  for item in listdir(directory):
    _pi = directory+'/'+item
    f(_pi, filepaths) if isdir(_pi) else remove(_pi)
  from os import rmdir; rmdir(directory)
  return directory

def t():
  temp_dir = './temp_directory_remove'
  temp_files_and_content = [
    (f'{temp_dir}/foo.py', 'f = lambda: None\nt = lambda: f() is None'),
    (f'{temp_dir}/xyz.txt', 'xyz'),
  ]
  def up():
    from os import mkdir
    from f.obj.nop import f as nop
    (mkdir if not exists(temp_dir) else nop)(temp_dir)

    from hak.file.save import f as save
    [save(filename, content) for (filename, content) in temp_files_and_content]
  up()
  f(temp_dir)
  return 0 == exists(temp_dir)
