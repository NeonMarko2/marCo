
import sys

FileToRead = sys.argv[1]

LinesOfCode = []
with open(FileToRead,'r') as file:
    for line in file:
        if line.endswith('\n'):
            LinesOfCode.append(line[:-1])
            continue
        LinesOfCode.append(line)


Variables = []
for i in range(10):
    Variables.append(0)

tokens = []
def Lexer(line):
    index = 0
    tokens.clear()

    while index < len(line):

        if line[index].isspace():

            index += 1

        elif line[index].isalpha():
            start = index

            while index < len(line) and line[index].isalpha():
                index += 1

            end = index
            tokens.append(str(line[start:end]))

        elif line[index].isnumeric():
            start = index

            while index < len(line) and line[index].isnumeric():
                index += 1

            end = index

            tokens.append(int(line[start:end]))

        elif line[index] == '[':
            start = index

            while index < len(line) and not line[index] == ']':
                index += 1

            index += 1
            end = index
            tokens.append(str(line[start:end]))

        elif line[index] == '<':
            tokens.append('<')
            index+=1
        elif line[index] == '>':
            tokens.append('>')
            index+=1
        elif line[index] == '=':
            tokens.append('=')
            index+=1
        elif line[index] == '~':
            tokens.append('~')
            index+=1


def Interperter():
    index = 0

    lineIndex = 0

    scope = 0

    while lineIndex < len(LinesOfCode):

        Lexer(LinesOfCode[lineIndex])
        lineIndex += 1

        if len(tokens) == 0:
            continue

        if tokens[0] == "yell":
            if isinstance(tokens[1], int):
                print(Variables[tokens[1]])
            else:
                print(tokens[1])
        elif tokens[0] == "input":
            if len(tokens) > 1:
                var = int(input())
                Variables[int(tokens[1])] = var
            else:
                ind = int(input())
                var = int(input())
                Variables[ind] = var

        elif tokens[0] == "set":
            if isinstance(tokens[2], str) and tokens[2].startswith('['):
                tokens[2] = Variables[int(tokens[2][1:-1])]
            Variables[int(tokens[1])] = tokens[2]
        elif tokens[0] == "add":
            Variables[int(tokens[1])] = Variables[tokens[2]]+Variables[int(tokens[3])]
        elif tokens[0] == "increment":
            Variables[int(tokens[1])] += 1
        elif tokens[0] == "sub":
            Variables[int(tokens[1])] = Variables[tokens[2]]-Variables[int(tokens[3])]
        elif tokens[0] == "mod":
            Variables[int(tokens[1])] = Variables[tokens[2]]%Variables[int(tokens[3])]
        elif tokens[0] == "if":
            boolean = False
            if tokens[2] == '=':
                if Variables[tokens[1]]==Variables[tokens[3]]:
                    boolean = True
            if tokens[2] == '~':
                if Variables[tokens[1]]!=Variables[tokens[3]]:
                    boolean = True
            if tokens[2] == '>':
                if Variables[tokens[1]]>Variables[tokens[3]]:
                    boolean = True
            if tokens[2] == '<':
                if Variables[tokens[1]]<Variables[tokens[3]]:
                    boolean = True
            if boolean:
                continue
            else:
                while lineIndex < len(LinesOfCode):

                    if len(tokens) != 0 and tokens[0] == "end":
                        break

                    Lexer(LinesOfCode[lineIndex])
                    lineIndex += 1
        elif tokens[0] == "jump":
            lineIndex = int(tokens[1])

        else:
            continue




Interperter()