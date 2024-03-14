
fh = open("text.txt", "w")
fh.write("content1\n")
fh.write("content2\n")
fh.close()

fh2 = open("text.txt", "a")
fh2.write("content3\n")
fh2.close()