from os.path import exists
from subprocess import run as sprun

from f.string.filepath.load import f as load
from f.string.to_cy import f as cy
from f.string.to_mg import f as mag
# from f.strings.filepath_and_content.save import f as save
from hak.file.save import f as save

def f(a, b, ask):
  if exists(a):
    print(f'a: {mag(a)}')
    if not any([a.endswith(_) for _ in [
      '.pdf',
      '.bak',
      '.db',
      '.x',
      '.xlsx',
      '.zip',
      '.pkl'
    ]]):
      save(a, load(a))
    sprun(args=['code', a])
  __=mag(a)

  response=input(cy(f"Proceed with '")+a+cy(f"'? (Q/Y/N):")) if ask else 'Y'

  if response=='Y':
    result = sprun(args=['git', 'add', a], capture_output=True, cwd='.')
    print(cy("Executing 'git add'"))
    print(f'result.stdout.decode():\n{result.stdout.decode()}')
    print(cy("Executing 'git commit'"))
    result = sprun(
      args=['git', 'commit', '-m', f'{b} {a}.'], capture_output=True, cwd='.'
    )
    print(f'result.stdout.decode():\n{result.stdout.decode()}')
    print(cy("Executing 'git push'"))
    result = sprun(args=['git', 'push'], capture_output=True, cwd='.')
    print(f'result.stdout.decode():\n{result.stdout.decode()}')
  elif response=='Q': exit()
  else: print('Cancelled.')

t = lambda: 1
