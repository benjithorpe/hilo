class MyStuff(object):

    def __init__(self):
        # --> legal to initialize a variable
        self.tangerine = "And now a thousand years between"
        
    def apple(self):
        print("I AM CLASSY APPLES!")


### Getting things from things

# 1. dictionary style

mystuff['apples']

# 2. module style
mystuff.apples()
print(mystuff.tangerine)

# 3. class style
thing = MyStuff()
thing.apples()
print(thing.tangerine)
