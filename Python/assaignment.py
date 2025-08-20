Name = input("Write your name: ")
Note = input("Write your notes: ")
with open ("info.txt" ,'w') as f: 
    f.write(Name + '\n')
    f.write(Note)
with open("info.txt",'r') as f:
    print(f.read())
# 