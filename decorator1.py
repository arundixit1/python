def hello(name):
    print("Hello",name)

def sm_hello(hello):
    def in_hello(name):
        print("Whatsup idiots")
        return hello(name)

    return in_hello

hello = sm_hello(hello)

hello("Arun")