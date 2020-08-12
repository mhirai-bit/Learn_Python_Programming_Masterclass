def print_backwards(*args, **kwargs):
    print(kwargs["file"], file=None)
    print(kwargs["end"], file=None)
    for word in args[::-1]:
        print(word[::-1], **kwargs)

with open("backwards.txt", "w") as backwards:
    print_backwards("hello", "planet", "earth", "take", "me", "to", "your", "leader", file=backwards, end="\n")