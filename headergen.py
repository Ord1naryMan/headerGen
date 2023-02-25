import sys
def main():
    print("Make sure that u are using namespaces and u don't have std:: and anything like this in function names.")

    ans = input("Are u shure u want to continue?: ")
    if(ans != 'y' and ans != 'Y'):
        exit()

    fileName = sys.argv[1]


    cppName = fileName + '.cpp'
    hName = fileName + '.h'

    file = open(cppName, "r")
    try:
        head = open(hName, "w")
    except:
        open(hName, "x")
        head = open(hName, "w")


    #using namespace needed!!!!!!!

    #only one class or classes aare in order
    head.write('#pragma once\n')
    line = file.readline()
    className = []   #checking for class
    while(line):
        line = file.readline()
        if (line.__contains__('::') and line.__contains__('{')):
            tmp = []
            start = end = 0
            start = line.find(' ')
            end = line.find('::')
            if start < end:
                tmp.append(line[start+1: end: 1])
            else:
                tmp.append(line[0:end:1])
            endLine = line.find('{')
            if start < end:
                tmp.append(line[0:start:1] + ' ' + line[end+2:endLine:1])
            else:
                tmp.append(line[end+2:endLine:1])
            className.append(tmp)
    prev = className[0][0]
    head.write('class ' + className[0][0] + '{\n')
    for i in className:
        if i[0] == "":
            continue
        if(prev == i[0]):
            prev = i[0]
            if (i[1].__contains__(':') and not i[1].__contains__('::')):
                head.write('\t' + i[1][:i[1].find(':'):1] + ";\n")
            else:
                head.write('\t' + i[1] + ";\n")
        else:
            prev = i[0]
            head.write('};\n')
            head.write('class ' + i[0] + '{\n')
            if (i[1].__contains__(':') and not i[1].__contains__('::')):
                head.write('\t' + i[1][:i[1].find(':'):1] + ";\n")
            else:
                head.write('\t' + i[1] + ";\n")
    head.write('};\n')
    file.close()
    file = open(cppName, "r")
    for line in file:
        if(line.__contains__('{') and not line.__contains__('for') and  not line.__contains__('while') and not line.__contains__('do') and  not line.__contains__('if') and  not line.__contains__('else') and  not line.__contains__('switch') and  not line.__contains__('enum') and  not line.__contains__('struct') and not line.__contains__('::')):
            head.write(line[0:line.find('{'):1] + ';\n')
if __name__ == '__main__':
    main()
