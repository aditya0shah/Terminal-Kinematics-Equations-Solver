import math
# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
print("Physics kinematic calculator!")






    solving_for = input("Which value are you solving for? Answer v0, vf, a, x, t? ")
    
    missing_value = input("Which value are you missing? Answer v0, vf, a, x, t? ")
    
    if missing_value == "x":
        if solving_for == "vf":
            v0 = float(input("What is v0? "))
            a = float(input("What is a? "))
            t = float(input("What is t? "))
            print("vf = " , (v0+a*t))
        elif solving_for == "v0":
            vf = float(input("What is vf? "))
            a = float(input("What is a? "))
            t = float(input("What is t? "))
            print("v0 = " ,(vf-a*t))
        elif solving_for == "a":
            v0 = float(input("What is v0? "))
            vf = float(input("What is vf? "))
            t = float(input("What is t? "))
            print("a = " , (vf-v0)/t)
        else:
            v0 = float(input("What is v0? "))
            vf = float(input("What is vf? "))
            a = float(input("What is a? "))
            print("t = " , (vf-v0)/a)
    elif missing_value == "a":
        if solving_for == "x":
            v0 = float(input("What is v0? "))
            vf = float(input("What is vf? "))
            t = float(input("What is t? "))
            print("x = " , ((vf+v0)/2)*t)
        elif solving_for == "t":
            v0 = float(input("What is v0? "))
            vf = float(input("What is vf? "))
            x = float(input("What is x? "))
            print("t = " , (x/((vf+v0)/2)))
        elif solving_for == "v0":
            vf = float(input("What is vf? "))
            x = float(input("What is x? "))
            t = float(input("What is t? "))
            print("v0 = " ,((2*x)/t)-vf)
        else:
            v0 = float(input("What is v0? "))
            x = float(input("What is x? "))
            t = float(input("What is t? "))
            print("vf = " ,((2*x)/t)-v0)
    elif missing_value == "vf":
        if solving_for == "x":
            v0 = float(input("What is v0? "))
            a = float(input("What is a? "))
            t = float(input("What is t? "))
            print("x = ", (v0*t + (1/2)*a*(t**2)))
        elif solving_for == "v0":
            x = float(input("What is x? "))
            a = float(input("What is a? "))
            t = float(input("What is t? "))
            print("v0 = ", ((x-(1/2)*a*(t**2))/t))
        elif solving_for == "a":
            v0 = float(input("What is v0? "))
            x = float(input("What is x? "))
            t = float(input("What is t? "))
            print("a = " , (((x-v0*t)*2)/(t**2)))
        else:
            v0 = float(input("What is v0? "))
            x = float(input("What is x? "))
            a = float(input("What is a? "))
            a= a/2
            x= x*(-1)
            root = math.sqrt((v0**2)-4*a*x)
            t = (root-v0)
            print("t = " , (t/(2*a)))
    elif missing_value == "v0":
        if solving_for == "x":
            vf = float(input("What is vf? "))
            a = float(input("What is a? "))
            t = float(input("What is t? "))
            print("x = ", (vf*t - (1/2)*a*(t**2)))
        elif solving_for == "vf":
            x = float(input("What is x? "))
            a = float(input("What is a? "))
            t = float(input("What is t? "))
            print("v0 = ", ((x+(1/2)*a*(t**2))/t))
        elif solving_for == "a":
            vf = float(input("What is vf? "))
            x = float(input("What is x? "))
            t = float(input("What is t? "))
            print("a = " , (((x-vf*t)*-2)/(t**2)))
        else:
            vf = float(input("What is vf? "))
            x = float(input("What is x? "))
            a = float(input("What is a? "))
            a= a/-2
            x= x*(-1)
            root = math.sqrt((vf**2)-4*a*x)
            t = (root-vf)
            print("t = " , (t/(2*a)))
    else:
        if solving_for == "vf":
            v0 = float(input("What is v0? "))
            x = float(input("What is x? "))
            a = float(input("What is a? "))
            print("vf = ", math.sqrt((v0**2)+2*a*x))
        elif solving_for == "v0":
            vf = float(input("What is vf? "))
            x = float(input("What is x? "))
            a = float(input("What is a? "))
            print("v0 = " , math.sqrt((vf**2) -2*a*x ))
        elif solving_for == "a":
            v0 = float(input("What is v0? "))
            vf = float(input("What is vf? "))
            a = float(input("What is a? "))
            print("a = ", (((vf**2)-(v0**2))/(2*a)))
        else:
            v0 = float(input("What is v0? "))
            vf = float(input("What is vf? "))
            x = float(input("What is x? "))
            print("x = ", (((vf**2)-(v0**2))/(2*x)))

