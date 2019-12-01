def decException():
    def f2(f1):
        def wrapper(*args,**kwargs):
            try:
                return f1(*args,**kwargs)
            except Exception as e:
                return e
        return wrapper
    return f2


@decException()
def f1(a, b):
    return a/b
print(f1(5,0))