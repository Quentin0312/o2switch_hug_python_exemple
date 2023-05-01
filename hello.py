import hug


@hug.get('/hello')
def say_hello():
    return "Hello world!"
