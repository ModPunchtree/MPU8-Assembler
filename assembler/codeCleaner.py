
from assembler.pseudoCodeTranslations import convertMMIOPointers, convertPseudoCode

def cleanCode(rawCode: str) -> list:

    # remove multiline comments
    # replace "  " with " " until "  " doesnt exist
    # replace "\n\n" with "\n" until "\n\n" doesnt exist
    # convert to list
    # remove line comments
    # find and resolve define macros
    # check for double ; on every instruction
    # convert labels to literals
    # convert relatives to literals
    # convert pseudo-asm to asm
    
    code = rawCode
    
    # remove multiline comments
    while code.find("/*") != -1:
        try:
            code = code[: code.index("/*")] + code[code.index("*/") + 2: ]
        except Exception():
            raise "FATAL - Found /* without */"
    
    # replace "  " with " " until "  " doesnt exist
    while code.find("  ") != -1:
        code = code.replace("  ", " ")

    # replace "\n\n" with "\n" until "\n\n" doesnt exist
    while code.find("\n\n") != -1:
        code = code.replace("\n\n", "\n")
    if code.startswith("\n"):
        code = code[1: ]
    if code.endswith("\n"):
        code = code[: -1]
    
    # convert to list
    code = code.split("\n")
    
    # remove line comments
    for lineNumber, line in enumerate(code):
        if "//" in line:
            code[lineNumber] = line[: line.index("//")]
    
    # find and resolve define macros
    lineNumber = 0
    while lineNumber < len(code):
        line = code[lineNumber]
        if line.startswith("@DEFINE"):
            tokens = line.split(" ")
            if len(tokens) != 3:
                raise Exception(f"FATAL - Syntax error in DEFINE macro: {line}")
            key = tokens[1]
            definition = tokens[2]
            code = [line2.replace(key, definition) for line2 in code]
            code.pop(lineNumber)
        else:
            lineNumber += 1

    # check for double ; on every instruction
    for line in code:
        if (not (line.startswith("."))) and (line.count(";") != 2):
            raise Exception(f"FATAL - Incorrect number of ';' on line: {line}")
    
    # convert labels to literals
    lineNumber = 0
    while lineNumber < len(code):
        line = code[lineNumber]
        if line.startswith("."):
            label = line
            code = [line2.replace(label, str(lineNumber)) for line2 in code]
            code.pop(lineNumber)
        else:
            lineNumber += 1
    
    # convert negative numbers
    for lineNumber, line in enumerate(code):
        while line.find("-") != -1:
            try:
                negative = line[line.index("-"): line[line.index("-"): ].index(" ")]
                end = line[line.index("-"): ].index(" ")
            except:
                negative = line[line.index("-"): line[line.index("-"): ].index(")")]
                end = line[line.index("-"): ].index(")")
            number = int(negative, 0) + 256
            code[lineNumber] = line[: line.index("-")] + str(number) + line[end: ]
    
    # convert relatives to literals
    for lineNumber, line in enumerate(code):
        while line.find("~") != -1:
            try:
                relative = line[line.index("~"): line[line.index("~"): ].index(" ")]
                end = line[line.index("~"): ].index(" ")
            except:
                relative = line[line.index("~"): line[line.index("~"): ].index(")")]
                end = line[line.index("~"): ].index(")")
            number = int(relative[1: ], 0)
            literal = str(lineNumber + number)
            code[lineNumber] = line[: line.index("~")] + literal + line[end: ]
    
    # convert mmio locations
    for lineNumber, line in enumerate(code):
        while line.find("*") != -1:
            try:
                mmio = line[line.index("*"): line[line.index("*"): ].index(" ")]
                end = line[line.index("*"): ].index(" ")
            except:
                mmio = line[line.index("*"): line[line.index("*"): ].index(")")]
                end = line[line.index("*"): ].index(")")
            code[lineNumber] = line[: line.index("*")] + convertMMIOPointers(mmio) + line[end: ]
    
    # convert pseudo-asm to asm
    code = [convertPseudoCode(line) for line in code]
    
    return code


