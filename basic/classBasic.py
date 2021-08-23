from os import name, read


class Name:
    def __init__(self,x,y):
        self.lastname = x 
        self.firstname = y
class File:
    def __init__(self,name):
        self.name = name
        self.file = None
    def open(self):
        self.file = open(self.name, mode = "r", encoding="utf-8") 
    def read(self):
        data = self.file.read()
        print(data)
if __name__ =="__main__":
    name1 = Name("jason","chen")
    name2 = Name("shrimp","chen")
    print(name1.firstname,name2.firstname)
    data = File("company.txt")
    data.open()
    data.read()