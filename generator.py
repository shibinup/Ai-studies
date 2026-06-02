def numbers():
    yield 1
    yield 2
    yield 3
gen = numbers()


def count_to_five():

    for i in range(1,6):
        yield i
gen = count_to_five()
print(next(gen))
print(next(gen))
print(next(gen))