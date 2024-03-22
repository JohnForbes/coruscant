from hak.directory.clean import f as clean_directory
from hak.test.do import f as do_test
from hak.test.final_line.check import f as _check_final_line
from hak.test.line_lengths.check import f as _check_line_lengths
from hak.test.oldest_file.print import f as _print_oldest_file
from f.analyse_lines import f as analyse_lines

def main():
  print('|'+'-'*78+'|')
  z = do_test(False)
  print(z['message'])
  if z['result']:
    _check_line_lengths()
    _check_final_line()
    _print_oldest_file()

  print('|'+'-'*78+'|')
  analyse_lines()
  print('|'+'-'*78+'|')
  clean_directory('.')
  return z['result']

if __name__ == '__main__':
  _ = main()
