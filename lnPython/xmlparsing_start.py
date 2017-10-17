import xml.dom.minidom

def main():

    doc = xml.dom.minidom.parse("samplehtml.html")

    print doc.nodeName
    print doc.firstChild.tagName

    skills = doc.getElementsByTagName("skill")
    print "%d skills:" % skills.length

    for skill in skills:
        print skill.getAttribute("name")


    newSkill = doc.createElement("skill")
    newSkill.setAttribute("name","jQuery")

    doc.firstChild.appendChild(newSkill)


if __name__ == '__main__':
    main()
