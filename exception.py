try :
          a=int(input("enter no: "))
          b=int(input("enter no: "))
          c=a/b
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
except ValueError:
    print("Error: Please enter only integers.") 
else:
    print("Succes ! result :",c)
finally:
    print("This line always runs...")