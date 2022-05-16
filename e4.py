def iq_test(test):
    odd_numbers_count = 0
    even_numbers_count = 0
    index = -1
    test_values = []
    test_values = test.split()
    for i in test_values:
        if(int(i) % 2 == 0):
            even_numbers_count += 1
        else:
            odd_numbers_count += 1
    if(even_numbers_count == 1):
        i = 0
        flag = False
        while((i < len(test_values)) and flag == False):
            if(int(test_values[i]) % 2 == 0):
                flag = True
                print(i + 1, " number is even, while the rest of the numbers are odd")
            i += 1
    elif(odd_numbers_count == 1):
        i = 0
        flag = False
        while((i < len(test_values)) and flag == False):
            if(int(test_values[i]) % 2 != 0):
                flag = True
                print(i + 1, " number is odd, while the rest of the numbers are even")
            i += 1
    return test_values

test = "8 2 4 3 18 24"
print(iq_test(test))