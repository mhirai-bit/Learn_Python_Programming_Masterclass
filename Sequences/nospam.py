menu = [
    ["egg", "bacon"],
    ["egg", "sausage", "bacon"],
    ["egg", "spam"],
    ["egg", "bacon", "spam"],
    ["egg", "bacon", "sausage", "spam"],
    ["spam", "bacon", "sausage", "spam"],
    ["spam", "sausage", "spam", "bacon", "spam", "tomato", "spam"],
    ["spam", "egg", "spam", "spam", "bacon", "spam"],
]

#delete ver.
# for menu_list in menu:
#     while "spam" in menu_list:
#         menu_list.remove("spam")
#     print(menu_list)
#skip ver.
# for menu_list in menu:
#     print("[", end=" ")
#     for ingre in menu_list:
#         if ingre == "spam":
#             continue
#         else:
#             print("'{0}',".format(ingre) , end="")
#     print("]")
print("-" * 80)
#tercher
for meal in menu:
    for index in range(len(meal) -1 , -1, -1):
        if meal[index] == "spam":
            del meal[index]
    print(", ".join(meal))

