
def single(text):
    return f'{text}'


def double(text):
    return f'{text} {text}'


def meow(func):
    say = func("Meow")
    print(say)


meow(double)
