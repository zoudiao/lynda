from HTMLParser import HTMLParser
class MyHTMLParser(HTMLParser):

    def handle_comment(self, data):
        print "Encountered comment:",data
        pos = self.getpos()
        print "At line: ", pos[0]," position ", pos[1]

def main():
    parser = MyHTMLParser()

    f = open("samplehtml.html")
    if f.mode == "r":
        contents = f.read()
        parser.feed(contents)

if __name__ == '__main__':
    main()