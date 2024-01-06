import datetime

def log(func):
    def wrapper(*args, **kwargs):
        with open("log.txt", 'a') as f:
            f.write("called function with args: " + " ".join([str(arg) for arg in args]) + " at: " + str(datetime.datetime.now()))
        val = func(*args, **kwargs)
        return val
    
    return wrapper

@log
def getMeanOf(*args):
    return sum(args)/len(args)

print(getMeanOf(1, 2, 3, 4, 5))
