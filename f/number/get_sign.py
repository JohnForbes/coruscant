f = lambda x: 0 if x == 0 else int(x/abs(x))
t = lambda: all([f(-2)==-1, f(2)==1, f(0)==0])
