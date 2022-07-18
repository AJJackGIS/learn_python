with open(r"C:\Users\AoJIE\Desktop\fileapi.txt", mode="r", encoding="utf-8") as f:
    # content = f.read()
    # print(content)
    for line in f:
        if line == "" or line == r"\r" or line == r"\n" or line == r"\r\n":
            print("bbb")
        print(line.strip())
