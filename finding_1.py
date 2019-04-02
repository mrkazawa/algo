print("Welcome! Press Q to exit")

while True:
    j = 1
    text = input("Insert number:")
    if text == 'Q' or text == 'q':
        break
    else:
        text = int(text)
        for i in range(9999):
            if j % text == 0:
                print(i + 1)
                break
            j = (j * 10) + 1