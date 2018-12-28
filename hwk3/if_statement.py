import random
# Valid random numbers
param1 = random.randint(0,20)
param2 = random.randint(10,25)
param3 = random.randint(20,45)
# Valid random number with strings 
param1v = "4"
param2v = "5"
param3v = random.randint(0,10) 
# Invalid random number 
param1i = "s"
param2i = 4
param3i = 1
# Valid float random number
param1f = random.uniform(2,5)
param2f = random.randint(0,5)
param3f = random.randint(0,5)
def check_equal(param1, param2, param3):
    try:
        param1 = int(param1) if type(param1) == str else param1
        param2 = int(param2) if type(param2) == str else param2
        param3 = int(param3) if type(param3) == str else param3
    except ValueError as e:
        return False
    if (param1 == param2) or (param2 == param3) or (param1 == param3):
        return True
    else:
        return False

print("Check equality of : ")
print("{0},{1},{2}".format(param1, param2, param3))
res = check_equal(param1,param2,param3)
print("Result: {}".format(res))
print("{0},{1},{2}".format(param1v, param2v, param3v))
res = check_equal(param1v,param2v,param3v)
print("Result: {}".format(res))
print("{0},{1},{2}".format(param1i, param2i, param3i))
res = check_equal(param1i, param2i, param3i)
print("Result: {}".format(res))
print("{0},{1},{2}".format(param1f, param2f, param3f))
res = check_equal(param1f, param2f, param3f)
print("Result: {}".format(res))


