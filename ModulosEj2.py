import time as t
hora= t.localtime()

if hora.tm_hour > 19:
    print("es hora de ir a casa")
else: print("no es hora dse ir a casa")