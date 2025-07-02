class Person:
    def __init__ (self , name , age , *degree ):
        self.name = name
        self.age = age
        self.degree = degree
    def person_info1(self):
        print(f"{self.name} : {self.age} years old , welcome to my class")

    def avg1 (self) :
        return f"your avg is {sum(self.degree)/len(self.degree)}"

    @property
    def ageInDays(self):
        return f"Hello {self.name} your age in days is : {self.age * 365}"

class person2 (Person):
    def __init__ (self , name , age  , gender ):
        super ().__init__(name , age)
        self.gender = gender

    def person_info(self):
        return f"{self.name} , {self.age} and the gender is {self.gender} "

class degree (Person):
    def __init__(self, degree , name , age ):
        super().__init__(name, age)
        self.degree = degree


    def degree1(self):
        return f"your degree is {self.degree}"

class Peoples:
    def __init__(self, names):
        self.names = names

    def loopin(self):
        result = ""
        for person in self.names:
            print(f"Person: {person}")
            for skill in self.names[person]:
                level = self.names[person][skill]
                result += f"{skill.upper()} : {level}\n"
        return result

names1 = {
    "Osama": {
        "Html": "70%",
        "Css": "80%",
        "Js": "70%"
    },
    "Ahmed": {
        "Html": "90%",
        "Css": "80%",
        "Js": "90%"
    },
    "Sayed": {
        "Html": "70%",
        "Css": "60%",
        "Js": "90%"
    }
}

peoples1 = Peoples(names1)
print(peoples1.loopin())
