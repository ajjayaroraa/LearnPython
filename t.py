for i in range (100):
    j = i+1
    if j % 5 == 0 and j % 7 == 0:
        print("Masai School")
    elif j % 5 == 0:
        print("Masai")
    elif j % 7 == 0:
        print("School")
    else:
        print(j)
