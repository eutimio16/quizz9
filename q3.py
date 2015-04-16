def superpower(a, b):
    p=1
    if (a==b):
        c=b*(a*a)
    else:
        while(p!=b):
            c= a*a
            p=p + 1
    return c
a=int(input(" give me number"))
b=int(input("give me a number"))
power=superpower(a,b)
print(power)