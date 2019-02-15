from collections.abc import Iterable, Iterator

a = []
ia = iter(a)

print(isinstance(a, Iterator))
print(isinstance(ia, Iterator))

