user_to_write = input("Write Something To Write In Your File : ")
with open("sample.txt" , "w") as f:
    content = f.write(user_to_write)
    print(content)