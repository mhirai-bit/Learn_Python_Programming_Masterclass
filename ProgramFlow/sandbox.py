activity_list = ["Exit", "Learn Python", "Learn Java", "Go swimming", "Have dinner", "Go to bed"]
chosen_num = "-"

while True:
    print()
    if chosen_num in "12345":
        print("Let's {}!".format(activity_list[int(chosen_num)].casefold()))
    elif chosen_num == "0":
        break
    else:
        print("Please chose from the list.")
    print("-" * 80)
    i = 0
    for sentence in activity_list:
        print("{} .\t{}".format(i,sentence))
        i += 1
    chosen_num = input()
print("Goodbye")