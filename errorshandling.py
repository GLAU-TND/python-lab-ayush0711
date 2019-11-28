## question 2 solution

try:
    a=int(input())  # ValueError
    b=int(input())
    c=input()
    d=a+b
    l=c+b   # TypeEror
    a.append(3)   #AttributeError
except ValueError:
    raise ValueError("Value Error Occured")
except TypeError:
    raise TypeError("Type Error Occured")
except AttributeError:
    raise AttributeError("Attribute Error Occured")