# the function supports multiple args
# kwargs is variable number of named arguments like galleons=100,sickles=50,knuts=25
def f(*args, **kwargs):
    print("Positional: ", kwargs)
    print("Positional: ", args)


f(galleons=100, sickles=50, knuts=25)
f(100, 50, 25)
