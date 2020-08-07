numbers = [1, 45, 32, 17, 60]

for number in numbers:
    if number % 8 == 0:
        # reject the list
        print("The numbers are unacceptable")
        break
else: # breakされないときに実行される
    print("All those numbers are fine")