x=8
y=str(2)
try:
    z=x/y

#below is the generic exception handling
#except Exception as e:
#    print("Handled Exception:", e)
#    z=None
#for a specific error handling
except ZeroDivisionError as e1:
    print("Zero Division Handled:",e1)
    z=None
except TypeError as e2:
    print("Type Error Handled:",type(e2).__name__)
    z=None

print("Division value:", z)
