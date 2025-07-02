class Person:
    def __init__ (self , name , age , *degree ):
        self.name = name
        self.age = age
        self.degree = degree
    def person_info1(self):
        print(f"{self.name} : {self.age} years old , welcome to my class")

    def avg1 (self) :
        return f"your avg is {sum(self.degree)/len(self.degree)}"


class person2 (Person):
    def __init__ (self , name , age  , gender ):
        super ().__init__(name , age)
        self.gender = gender

    def person_info(self):
        return f"{self.name} , {self.age} and the gender is {self.gender} "
