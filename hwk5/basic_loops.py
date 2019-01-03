for i in range(100):
    res_list = [i%j for j in range(1, i+1) if i%j == 0]
    if len(res_list) == 2:
        print("===prime: {}".format(i))
    if i%3 == 0 and i%5 == 0:
        print("FizzBuzz: {}".format(i)) 
        continue
    if i%3 == 0:
        print("Fizz: {}".format(i))
    if i%5 == 0:
        print("Buzz: {}".format(i))
