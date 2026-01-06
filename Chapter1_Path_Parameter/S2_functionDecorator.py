
def fence(func):     # decorator function
    def wrapper():
        print("+"*10)
        func()
        print("+"*10)
    return wrapper

@fence              # applying decorator    
def log():
    print("decorated!")

log()

# or 
# another_fence = fence(log)
# another_fence()