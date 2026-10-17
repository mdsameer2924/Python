with open("demo.txt", "w+") as f:
    f.write("my name is Sameer")
    print(f.readline(1))

with open("demo.txt", "r") as re:
    re.readline(1)
