try:
    with open ("new.text" ,'r') as file:
        content=file.read()
        result=10/int(content)
        print(result)
        
        
except FileNotFoundError:
    print("File not found")




except ValueError:
    print("ValueError")

