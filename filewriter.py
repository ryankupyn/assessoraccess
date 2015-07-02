def jsonwriter(filename, text):
    jfile = open(filename, "a")
    for hop in text:
        jfile.write(str(hop))
    jfile.write("\n")
    jfile.close()
