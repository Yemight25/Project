
file = open("yemi.txt",'r')
a = file.read()
split1 = a.split('\n')
for x in split1:

    split2= x.split(' ')
    print(split2)
    the_sum = int(split2[1]) + int(split2[2]) +int(split2[3])
    avg = the_sum / 3

    if (avg > 70):
        print("Student passed")
    else:
        print(" student failed")    