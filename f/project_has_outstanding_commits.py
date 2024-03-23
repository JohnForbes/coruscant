def f():
  from subprocess import run as sprun
  _ = sprun(args=['git', 'status', '-s'], capture_output=True, cwd='.')
  return len(_.stdout.decode('utf-8').split('\n')) > 1

t = lambda: 1
