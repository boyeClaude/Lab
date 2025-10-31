#Learing about function
def greeting(name:str): 
    print("Hello, " + name)

greeting("Alice")

#returning function
def add(numb1, numb2):# type: ignore
    return numb1 + numb2 # type: ignore

result = add(10,3)
print(result)