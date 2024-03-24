def f(filename):
  with open(filename, 'r', encoding='utf8') as φ:
    return φ.read()

def t():
  temp_dir_0 = './_temp_file_load'
  temp_files_and_content = [(f'{temp_dir_0}/foo.py', 'foo')]
  def up():
    from os.path import exists
    from os import mkdir
    [mkdir(temp_dir) for temp_dir in [temp_dir_0] if not exists(temp_dir)]
    from hak.file.save import f as save
    [save(filename, content) for (filename, content) in temp_files_and_content]
  up()
  test_result = 'foo' == f(f'{temp_dir_0}/foo.py')
  def dn():
    from os import remove
    [remove(filename) for (filename, _) in temp_files_and_content]
    from f.string.directory.remove import f as remove_dir
    remove_dir(temp_dir_0)
  dn()
  return test_result
