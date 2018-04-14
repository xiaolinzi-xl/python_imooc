
class Test():
    def __bool__(self):
        print('bool called')
        return False

    def __len__(self):
        print('len called')
        return 1

test = Test()

if test:
    print('S')
else:
    print('F')

print(bool(None))
print(bool([]))
print(bool(test))