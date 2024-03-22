from sys import argv
from f.gitter.main import f as main
from hak.file.load import f as load
from hak.file.save import f as save

if __name__ == '__main__':
  main(ask=argv[-1] != '0')
  save('gitter.py', load('gitter.py'))
