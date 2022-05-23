a = ['cde', 'cfc', 'abc']
sorted(a, key=lambda s: (s[0], s[-1]))

print(a)
