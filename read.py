ile_object = open("hello.txt","r")
print(file_object.read())


f=open("hello.txt","r")
data=f.read #read whole file
print("file content",data)
f.close()

f=open("hello.txt","r")
data=f.read(2)#read whole file
print("file content",data)
f.close()

f=open("hello.txt","r")
line1=f.readline()
print("Line 1:",line1)
f.close()

f=open("hello.txt","r")
lines=f.readlines()
print("List of lines:",lines)
print("Number of lines:",len(lines))
f.close()

f=open("hello.txt","r")
lines=f.readlines()
print(lines[2].strip())
f.close()