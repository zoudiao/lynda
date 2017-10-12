def main():
    #f = open("textfile.txt", "w+")

    f = open("textfile.txt","a+")
    for i in range(10):
        f.write("This is line %d\r\n" %(i+1))

    f.close()

    f = open("textfile.txt","r")
    if f.mode == 'r':
        contents = f.read()
        print contents

        fl = f.readline()
        for x in fl:
            print x
            
if __name__ == '__main__':
    main()