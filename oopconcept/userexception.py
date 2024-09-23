class Accident(Exception):
    def __init__(self,message):
        self.msg = message
    def print_exception(self):
        print("User defined exception", self.msg)

try:
    raise Accident("car-crash")
except Accident as e1:
    e1.print_exception()
finally:
    print("take a detour")