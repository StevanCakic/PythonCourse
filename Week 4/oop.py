class Post:
    # Class object attribute
    class_var = ""
    def __init__(self, name, description="Default Description", author="Admin", id=1):
        self.name = name
        self.description = description
        self.author = author
        self.__id = id

post_a = Post("Clanak 1", "Probni clanak", "Marko Markovic")
post_b = Post(name="Clanak 2", author="Ivan Ivanovic")
# post_c = Post() # moze li ovo?
print(post_a) # zasto ovako stampa
print(post_a.name)
print(post_a.class_var)
print(post_b.class_var)
print(type(post_a))