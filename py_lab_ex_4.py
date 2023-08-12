
#single inheritance
class library():
    name="kavaskar"
    def __init__(self):
        print("hello this is library") 
    def display(self):
        print("hello i am a library")

class librarian(library):
    def __init__(self):
        print("librarian here")

    def display(self):
        print("hello this is librarian")

#multilevel inheritance
class librarian_det(librarian):
    def __init__(self):
        print("librarian details here")

    def display(self):
        print("hello here you can able to find the librarian details")

#multiple inheritance
class author():
    def __init__(self):
        print("author here")

    def display(self):
        print("hello i will have the details about any authors")

class books(library,author):
    def __init__(self):
        print("books here")
    def __init__(self):
        print("hello i am having the details of both the library and the authors")

#hirarchial inehritance
class user(library):
    def __init__(self):
        print("user here")

    def display(self):
        print("hello i am the user reading book is my hobby")

#calling multilevel
l_det=librarian_det()
l_det.display()


#calling multiple inheritance
bk=books()
bk.display()

#calling hirarichial
usr=user()
usr.display()