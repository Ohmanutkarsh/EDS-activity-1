arr = input()
e = input()

arr = arr.split(" ")
c = 0

for i in arr:

    if i == e:
        print(c)
        break

    c += 1

else:
    print("Not found")
