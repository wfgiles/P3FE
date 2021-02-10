counts = dict()
names = ['Bill', 'John', 'Mary', 'Alex', 'Jeb']
for name in names:
    if name not in counts:
        counts[name] = 1
    else:
        counts[name] = counts[name] + 1
print counts
