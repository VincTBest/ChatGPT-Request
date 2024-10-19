def main():
    dir = input("Files Directory: ")
    ex = input("Allowed Extensions [With dot]: ")
    rq = input("Request: ")
    alloweddir = []
    mainstr = f"Request: {rq}"
    import os, time
    listeddir = os.listdir(dir)
    for i_a in listeddir:
        if ex in i_a:
            alloweddir.append(i_a)
    print(f"Allowed files: {alloweddir}")
    for i_b in alloweddir:
        s_a = f"{dir}\\{i_b}"
        s_b = open(s_a, "r")
        s_c = s_b.read()
        mainstr = f"{mainstr}\n{i_b}:\n{s_c}"
    print(f"Output: {mainstr}\nSaved to file: output.txt")
    outputfile = open("./output.txt", "w")
    outputfile.write(f"\n{mainstr}\n")
    time.sleep(9999)


if __name__ == '__main__':
    main()