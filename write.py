#1
f=open("one.txt","w")
f.write("hello everyone\n")
f.write("i am from bsc it\n")
f.close()

#2
f=open("one.txt","w")
f.write("new content only\n")
f.close()

#3
f=open("one.txt","a")
f.write("Atmiya university\n")
f.close()

#4
f=open("two.txt","w")
lines=["python programming\n",
"file handling"]
f.writelines(lines)
f.close()