d = {'first': 1.05, 'second': 1.025, 'third': 1.125}
f = d.get('first')
s = d.get('second')
t = d.get('third')
if (f >= s) & (f >= t): print('first')
elif (s >= f) & (s >= t): print('second')
else: print('third')