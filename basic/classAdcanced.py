


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def show(self):
        print(self.x, self.y)
class File:
    def __init__(self, name):
        self.name = name 
        self.file = None
    def open(self):
        self.file = open(self.name, mode="r", encoding="utf-8")
    def read(self):
        return self.file.read()
if __name__ == "__main__":
    p = Point(123,456)
    p.show()
    f1 = File("company.txt")
    f1.open()
    data= f1.read()
    print(data)