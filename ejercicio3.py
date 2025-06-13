def cero_repetido(*args):

    for num in range(len(args)):
        if len(args) == num+1:
            return "false"
        print(args[num], "el que sigue es ", args[num+1])
        num1 = args[num]
        num2 = args[num+1]
        if args[num] == 0 and args[num+1] == 0:
            return "true"
        else:
            continue




print(cero_repetido(1,2,3,0,1,0))