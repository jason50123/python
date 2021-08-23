def editing(x,y):
    with open("test.txt", mode = "w", encoding = "utf-8") as file:
        for i in range(1,x+1):
            for j in range(1,y+1):
                file.write(str(i)+ "* "+ str(j)+ " = "+ str(i*j) +"\n")
def drawing(x):
    with open("draw.txt", mode = "w", encoding= "utf-8") as file:
        for i in range(1,x+1):
            for j in range(x-i,0,-1):
                file.write("x")
            for k in range(1,2*i,1):
                file.write("*")
            file.write("\n")
if __name__ == "__main__":
    """x,y = map(int,input("please enter the number u want: ").split())
    editing(x,y)
    """
    drawing(10)
