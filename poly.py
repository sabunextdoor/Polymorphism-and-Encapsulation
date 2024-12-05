class dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def info(self):
        print(self.name, self.age)
    def make_sound(self):
        print("bark")
class cat:
            def __init__(self, name, age):
                self.name = name
                self.age = age
            def info(self):
                print(self.name, self.age)
            def make_sound(self):
                print("meow")

obj1=dog("tom",1)
obj2=cat("jerry",1)

for i in (obj1,obj2):
     i.info()
     i.make_sound()