lst = [1, 3, 4, 6]
print(" append  \n  insert")

a = input("введіть дію: ")
b = input("виберіть тип елемента: ")

if a == "append":
    d = input("введіть елемент:")
    if b == "int":
        if int(d) in lst:
            element = input("добавити ще раз?(yes/no)")
            if element == "yes":
                lst.append(int(d))
    elif b == "str":
        if d in lst:
            element = input("добавити ще раз?(yes/no)")
            if element == "yes":
                lst.append(d)
elif a == "insert":
    c = int(input("виберіть індекс: "))
    d = input("введіть елемент:")
    if b == "int":
        lst.insert(c, int(d))
    elif b == "str":
        lst.insert(c, d)
print(1)
print(lst)