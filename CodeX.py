from sys import *

tokens = []

def open_file(filename):
    data = open(filename, "r").read()
    data += "<EOF>"
    return data

def lex(filecontents):
    tok = ""
    state = 0
    string = ""
    expr = ""
    n = ""
    isexpr = 0
    filecontents = list(filecontents)
    for char in filecontents:
        tok += char
        if tok == " ":
            if state == 0:
                tok = ""
            else:
                tok = " "
        elif tok == "\n" or tok == "<EOF>":
            if expr != "" and isexpr == 1:
                tokens.append("EXPR:" + expr)
                print(expr + " - That's an expression, mate.")
                expr = ""
            elif expr != "" and isexpr == 0:
                # print(expr + "NUM")
                tokens.append("NUM:" + expr)
                expr = ""
            tok = ""
        elif tok == "PRINT" or tok == "print":
            tokens.append("PRINT")
            #print("FOUND A PRINT")
            tok = ""
        elif tok == "MLG" or tok == "mlg":
            import mlg
            tok = ""
        elif tok == "NAME" or tok == "name":
            import name
            tok = ""
        elif tok == "TIME" or tok == "time":
            import tod
            tok = ""
        elif tok == "ABOUT" or tok == "about":
            # print("CodeX - A programming language by Meorge after watching some video tutorials on YouTube. It's not very good.")
            import about
            tok = ""
        elif tok == "COMMANDS" or tok == "commands":
            import commands
            tok = ""
        elif tok == "0" or tok == "1" or tok == "2" or tok == "3" or tok == "4" or tok == "5" or tok == "6" or tok == "7" or tok == "8" or tok == "9":
            #print("WE'VE GOT A NUMBER")
            expr += tok
            tok = ""
        elif tok == "+":
            isexpr = 1
            expr += tok
            tok = ""
        elif tok == "{" or tok == "}":
            if state == 0:
                state = 1
            elif state == 1:
                tokens.append("STRING:" + string + "}")
                print("FOUND A STRING")
                string = ""
                state = 0
                tok = ""
        elif state == 1:
            string += tok
            tok = ""
    return tokens
    print(tokens)
    print(toks)

def evalExpression(expr):
    return "Got it, " + expr

def doPRINT(toPRINT):
    if(toPRINT[0:6] == "STRING"):
        toPRINT = toPRINT[8:]
        toPRINT = toPRINT[:-1]
    elif(toPRINT[0:3] == "NUM"):
        toPRINT = toPRINT[4:]
    elif(toPRINT[0:4] == "EXPR"):
        toPRINT = evalExpression(toPRINT[5:])
    print(toPRINT)

def parse(toks):
    i = 0
    while(i < len(toks)):
        if toks[i] + " " + toks[i+1][:6] == "PRINT STRING" or toks[i] + " " + toks[i][:3] == "PRINT NUM" or toks[i] + " " + toks[i][:4] == "PRINT EXPR":
            #print("FOUND STRING")
            if toks[i+1][0:6] == "STRING":
                doPRINT(toks[i+1][7:])
            elif toks[i+1][0:3] == "NUM":
                doPRINT(toks[i+1][4:])
            elif toks[i+1][0:4] == "EXPR":
                doPRINT(toks[i+1][5:])
            i+=2

def run():
    data = open_file(argv[1])
    #data = argv[1]
    toks = lex(data)
    parse(toks)
    parse(tokens)

run()