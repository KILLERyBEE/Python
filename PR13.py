def calculate_case(str):
    up = 0
    low = 0
    for i in str:
        if i.isupper():
            up = up+1
        else:
            low = low + 1

    print(f"Your String has {up} UpperCase Characters")
    print(f"Your String has {low} LowerCase Characters")

a = input("Enter A String: ")
calculate_case(a)
