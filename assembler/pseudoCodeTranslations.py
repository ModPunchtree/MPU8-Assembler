
def operations() -> tuple:
    return ("NOP", "RST", "ADD", "ADC", "SUB", "SBB", "MOV", "IMM", "INC", "DEC", "NEG", "LSH", "LSC", "LCF","RCF", "NOR", "AND", "NOT", "FLG", "SETX", "SETY", "SETMX", "SETMY", "PRT", "VSH", "SPT", "RPT", "HLT", "JMP", "RET", "STL", "FFG", "CLR", "STR", "LOD", "OR", "NAND", "DSL", "LSL", "CMP", "DLSL")

def convertMMIOPointers(key: str) -> str:
    key = key.upper()
    MMIOPointers = {"*MULTA": 128,
                    "*MULTB": 129,
                    "*MULTLOW": 128,
                    "*MULTHIGH": 129,
                    "*DIVISOR": 130,
                    "*DIVIDENDLOW": 132,
                    "*DIVIDENDHIGH": 131,
                    "*QUOTENT": 130,
                    "*REMAINDER": 131,
                    "*ROUNDEDQUOTENT": 132,
                    "*BCD0": 133,
                    "*BCD1": 134,
                    "*BCD2": 135,
                    "*BCD3": 136,
                    "*BCD4": 137,
                    "*BCD5": 138,
                    "*BCD6": 139,
                    "*BCD7": 140,
                    "*BCD8": 141,
                    "*BCD9": 142,
                    "*BUFFER": 143,
                    "*ACF_NOR": 144,
                    "*NOR_OR": 145,
                    "*ACTIVATEUSERINPUT": 146,
                    "*BYTEADDRESS": 147,
                    "*PAGEADDRESS": 148,
                    "*LOWBYTE": 147,
                    "*HIGHBYTE": 148,
                    "*CLR": 149,
                    "*HLT": 150,
                    "*VSH": 151,
                    "*X": 152,
                    "*Y": 153,
                    "*MACROX": 154,
                    "*MACROY": 155,
                    "*CHAR0": 157,
                    "*CHAR1": 158,
                    "*CHAR2": 159,
                    "*CHAR3": 160,
                    "*IN": 161,
                    "*TOGGLEOR": 162,
                    "*GLOBALTIMER": 163,
                    "*SHIFTX": 164,
                    "*SHIFTY": 165}
    return str(MMIOPointers[key])

def incorrectNumberOfOperands(debug: object) -> None:
    expected = ""
    for i in debug.expectedNumberOfOperands:
        expected += f"{i} or"
    expected = expected[: -2]
        
    raise Exception(f"FATAL - Incorrect number of operands in operation: {debug.operation}\nIn line: {debug.line}\n Expected {expected} number of operands, but found {debug.numberOfOperands}")

def convertPseudoCode(line: str) -> tuple:
    
    class debugList:
        line = ""
        operation = ""
        numberOfOperands = 0
        expectedNumberOfOperands = (0, )
    
    temp = line.replace("(", " ( ").replace(")", " ) ").replace(";", " ; ").replace("  ", " ").replace("  ", " ")
    if temp.startswith(" "):
        temp = temp[1: ]
    if temp.endswith(" "):
        temp = temp[: -1]
    tokens = temp.split(" ")
    
    debug = debugList
    
    tokenIndex = 0
    while tokenIndex < len(tokens):
        
        if tokens[tokenIndex] in operations():
            operationIndex = tokenIndex
            operation = tokens[tokenIndex]
            
            tokenIndex += 2
            operands = []
            while tokens[tokenIndex] != ")":
                operands.append(tokens[tokenIndex])
                tokenIndex += 1
            tokenIndex += 1
    
            numberOfOperands = len(operands)
            
            debug.line = line
            debug.operation = operation
            debug.numberOfOperands = numberOfOperands
            
            match operation:
                case "NOP":
                    debug.expectedNumberOfOperands = (0, )
                    if numberOfOperands not in debug.expectedNumberOfOperands:
                        incorrectNumberOfOperands(debug)
                case "RST":
                    debug.expectedNumberOfOperands = (1, )
                    if numberOfOperands not in debug.expectedNumberOfOperands:
                        incorrectNumberOfOperands(debug)
                    
                    translation = ["ADD", "(", operands[0], "R0", "R0", ")"]
                    tokens = tokens[: operationIndex] + translation + tokens[tokenIndex: ]
                    tokenIndex += len(translation) - (numberOfOperands + 3)
                case "ADD":
                    debug.expectedNumberOfOperands = (2, 3)
                    if numberOfOperands not in debug.expectedNumberOfOperands:
                        incorrectNumberOfOperands(debug)
                    
                    if numberOfOperands == 2:
                        translation = ["ADD", "(", operands[0], operands[0], operands[1], ")"]
                        tokens = tokens[: operationIndex] + translation + tokens[tokenIndex: ]
                        tokenIndex += len(translation) - (numberOfOperands + 3)
                case "ADC":
                    debug.expectedNumberOfOperands = (2, 3)
                    if numberOfOperands not in debug.expectedNumberOfOperands:
                        incorrectNumberOfOperands(debug)
                    
                    if numberOfOperands == 2:
                        translation = ["ADC", "(", operands[0], operands[0], operands[1], ")"]
                        tokens = tokens[: operationIndex] + translation + tokens[tokenIndex: ]
                        tokenIndex += len(translation) - (numberOfOperands + 3)
                case "SUB":
                    debug.expectedNumberOfOperands = (2, 3)
                    if numberOfOperands not in debug.expectedNumberOfOperands:
                        incorrectNumberOfOperands(debug)
                    
                    if numberOfOperands == 2:
                        translation = ["ADC", "(", operands[0], operands[0], f"!{operands[1]}", ")"]
                        tokens = tokens[: operationIndex] + translation + tokens[tokenIndex: ]
                        tokenIndex += len(translation) - (numberOfOperands + 3)
                    elif numberOfOperands == 3:
                        translation = ["ADC", "(", operands[0], operands[1], f"!{operands[2]}", ")"]
                        tokens = tokens[: operationIndex] + translation + tokens[tokenIndex: ]
                        tokenIndex += len(translation) - (numberOfOperands + 3)
                case "SBB":
                    debug.expectedNumberOfOperands = (2, 3)
                    if numberOfOperands not in debug.expectedNumberOfOperands:
                        incorrectNumberOfOperands(debug)
                    
                    if numberOfOperands == 2:
                        translation = ["ADD", "(", operands[0], operands[0], f"!{operands[1]}", ")"]
                        tokens = tokens[: operationIndex] + translation + tokens[tokenIndex: ]
                        tokenIndex += len(translation) - (numberOfOperands + 3)
                    elif numberOfOperands == 3:
                        translation = ["ADD", "(", operands[0], operands[1], f"!{operands[2]}", ")"]
                        tokens = tokens[: operationIndex] + translation + tokens[tokenIndex: ]
                        tokenIndex += len(translation) - (numberOfOperands + 3)
                case "MOV":
                    debug.expectedNumberOfOperands = (2, )
                    if numberOfOperands not in debug.expectedNumberOfOperands:
                        incorrectNumberOfOperands(debug)
                    
                    translation = ["ADD", "(", operands[0], operands[1], "R0", ")"]
                    tokens = tokens[: operationIndex] + translation + tokens[tokenIndex: ]
                    tokenIndex += len(translation) - (numberOfOperands + 3)
                case "IMM":
                    debug.expectedNumberOfOperands = (2, )
                    if numberOfOperands not in debug.expectedNumberOfOperands:
                        incorrectNumberOfOperands(debug)
                    
                    translation = ["ADD", "(", operands[0], operands[1], "R0", ")"]
                    tokens = tokens[: operationIndex] + translation + tokens[tokenIndex: ]
                    tokenIndex += len(translation) - (numberOfOperands + 3)
                case "INC":
                    debug.expectedNumberOfOperands = (1, 2)
                    if numberOfOperands not in debug.expectedNumberOfOperands:
                        incorrectNumberOfOperands(debug)
                    
                    if numberOfOperands == 1:
                        translation = ["ADC", "(", operands[0], operands[0], "R0", ")"]
                        tokens = tokens[: operationIndex] + translation + tokens[tokenIndex: ]
                        tokenIndex += len(translation) - (numberOfOperands + 3)
                    elif numberOfOperands == 2:
                        translation = ["ADC", "(", operands[0], operands[1], "R0", ")"]
                        tokens = tokens[: operationIndex] + translation + tokens[tokenIndex: ]
                        tokenIndex += len(translation) - (numberOfOperands + 3)
                case "DEC":
                    debug.expectedNumberOfOperands = (1, 2)
                    if numberOfOperands not in debug.expectedNumberOfOperands:
                        incorrectNumberOfOperands(debug)
                    
                    if numberOfOperands == 1:
                        translation = ["ADD", "(", operands[0], operands[0], "!R0", ")"]
                        tokens = tokens[: operationIndex] + translation + tokens[tokenIndex: ]
                        tokenIndex += len(translation) - (numberOfOperands + 3)
                    elif numberOfOperands == 2:
                        translation = ["ADD", "(", operands[0], operands[1], "!R0", ")"]
                        tokens = tokens[: operationIndex] + translation + tokens[tokenIndex: ]
                        tokenIndex += len(translation) - (numberOfOperands + 3)
                case "NEG":
                    debug.expectedNumberOfOperands = (1, 2)
                    if numberOfOperands not in debug.expectedNumberOfOperands:
                        incorrectNumberOfOperands(debug)
                    
                    if numberOfOperands == 1:
                        translation = ["ADC", "(", operands[0], f"!{operands[0]}", "R0", ")"]
                        tokens = tokens[: operationIndex] + translation + tokens[tokenIndex: ]
                        tokenIndex += len(translation) - (numberOfOperands + 3)
                    elif numberOfOperands == 2:
                        translation = ["ADC", "(", operands[0], f"!{operands[1]}", "R0", ")"]
                        tokens = tokens[: operationIndex] + translation + tokens[tokenIndex: ]
                        tokenIndex += len(translation) - (numberOfOperands + 3)
                case "LSH":
                    debug.expectedNumberOfOperands = (1, 2)
                    if numberOfOperands not in debug.expectedNumberOfOperands:
                        incorrectNumberOfOperands(debug)
                    
                    if numberOfOperands == 1:
                        translation = ["ADD", "(", operands[0], operands[0], operands[0], ")"]
                        tokens = tokens[: operationIndex] + translation + tokens[tokenIndex: ]
                        tokenIndex += len(translation) - (numberOfOperands + 3)
                    elif numberOfOperands == 2:
                        translation = ["ADD", "(", operands[0], operands[1], operands[1], ")"]
                        tokens = tokens[: operationIndex] + translation + tokens[tokenIndex: ]
                        tokenIndex += len(translation) - (numberOfOperands + 3)
                case "LSC":
                    debug.expectedNumberOfOperands = (1, 2)
                    if numberOfOperands not in debug.expectedNumberOfOperands:
                        incorrectNumberOfOperands(debug)
                    
                    if numberOfOperands == 1:
                        translation = ["ADC", "(", operands[0], operands[0], operands[0], ")"]
                        tokens = tokens[: operationIndex] + translation + tokens[tokenIndex: ]
                        tokenIndex += len(translation) - (numberOfOperands + 3)
                    elif numberOfOperands == 2:
                        translation = ["ADC", "(", operands[0], operands[1], operands[1], ")"]
                        tokens = tokens[: operationIndex] + translation + tokens[tokenIndex: ]
                        tokenIndex += len(translation) - (numberOfOperands + 3)
                case "LCF":
                    debug.expectedNumberOfOperands = (1, 2)
                    if numberOfOperands not in debug.expectedNumberOfOperands:
                        incorrectNumberOfOperands(debug)
                    
                    if numberOfOperands == 1:
                        translation = ["ACF", "(", operands[0], operands[0], operands[0], ")"]
                        tokens = tokens[: operationIndex] + translation + tokens[tokenIndex: ]
                        tokenIndex += len(translation) - (numberOfOperands + 3)
                    elif numberOfOperands == 2:
                        translation = ["ACF", "(", operands[0], operands[1], operands[1], ")"]
                        tokens = tokens[: operationIndex] + translation + tokens[tokenIndex: ]
                        tokenIndex += len(translation) - (numberOfOperands + 3)
                case "RCF":
                    debug.expectedNumberOfOperands = (1, 2)
                    if numberOfOperands not in debug.expectedNumberOfOperands:
                        incorrectNumberOfOperands(debug)
                    
                    if numberOfOperands == 1:
                        translation = ["RCF", "(", operands[0], operands[0], "R0", ")"]
                        tokens = tokens[: operationIndex] + translation + tokens[tokenIndex: ]
                        tokenIndex += len(translation) - (numberOfOperands + 3)
                case "NOR":
                    debug.expectedNumberOfOperands = (2, 3)
                    if numberOfOperands not in debug.expectedNumberOfOperands:
                        incorrectNumberOfOperands(debug)
                    
                    if numberOfOperands == 2:
                        translation = ["NOR", "(", operands[0], operands[0], operands[1], ")"]
                        tokens = tokens[: operationIndex] + translation + tokens[tokenIndex: ]
                        tokenIndex += len(translation) - (numberOfOperands + 3)
                case "AND":
                    debug.expectedNumberOfOperands = (2, 3)
                    if numberOfOperands not in debug.expectedNumberOfOperands:
                        incorrectNumberOfOperands(debug)
                    
                    if numberOfOperands == 2:
                        translation = ["NOR", "(", operands[0], f"!{operands[0]}", f"!{operands[1]}", ")"]
                        tokens = tokens[: operationIndex] + translation + tokens[tokenIndex: ]
                        tokenIndex += len(translation) - (numberOfOperands + 3)
                    elif numberOfOperands == 3:
                        translation = ["NOR", "(", operands[0], f"!{operands[1]}", f"!{operands[2]}", ")"]
                        tokens = tokens[: operationIndex] + translation + tokens[tokenIndex: ]
                        tokenIndex += len(translation) - (numberOfOperands + 3)
                case "NOT":
                    debug.expectedNumberOfOperands = (1, 2)
                    if numberOfOperands not in debug.expectedNumberOfOperands:
                        incorrectNumberOfOperands(debug)
                    
                    if numberOfOperands == 1:
                        translation = ["ADD", "(", operands[0], f"!{operands[0]}", "R0", ")"]
                        tokens = tokens[: operationIndex] + translation + tokens[tokenIndex: ]
                        tokenIndex += len(translation) - (numberOfOperands + 3)
                    elif numberOfOperands == 2:
                        translation = ["ADD", "(", operands[0], f"!{operands[1]}", "R0", ")"]
                        tokens = tokens[: operationIndex] + translation + tokens[tokenIndex: ]
                        tokenIndex += len(translation) - (numberOfOperands + 3)
                case "FLG":
                    debug.expectedNumberOfOperands = (1, )
                    if numberOfOperands not in debug.expectedNumberOfOperands:
                        incorrectNumberOfOperands(debug)
                case "SETX":
                    debug.expectedNumberOfOperands = (1, )
                    if numberOfOperands not in debug.expectedNumberOfOperands:
                        incorrectNumberOfOperands(debug)
                    if operands[0][0].isnumeric():
                        raise Exception(f"FATAL - SETX cannot accept immediate values\nOn line: {line}")
                    
                    translation = ["ADD", "(", "SR", operands[0], "R0", ")", "SPT", "(", "152", ")"]
                    tokens = tokens[: operationIndex] + translation + tokens[tokenIndex: ]
                    tokenIndex += len(translation) - (numberOfOperands + 3)
                case "SETY":
                    debug.expectedNumberOfOperands = (1, )
                    if numberOfOperands not in debug.expectedNumberOfOperands:
                        incorrectNumberOfOperands(debug)
                    if operands[0][0].isnumeric():
                        raise Exception(f"FATAL - SETY cannot accept immediate values\nOn line: {line}")
                    
                    translation = ["ADD", "(", "SR", operands[0], "R0", ")", "SPT", "(", "153", ")"]
                    tokens = tokens[: operationIndex] + translation + tokens[tokenIndex: ]
                    tokenIndex += len(translation) - (numberOfOperands + 3)
                case "SETMX":
                    debug.expectedNumberOfOperands = (1, )
                    if numberOfOperands not in debug.expectedNumberOfOperands:
                        incorrectNumberOfOperands(debug)
                    if operands[0][0].isnumeric():
                        raise Exception(f"FATAL - SETMX cannot accept immediate values\nOn line: {line}")
                    
                    translation = ["ADD", "(", "SR", operands[0], "R0", ")", "SPT", "(", "154", ")"]
                    tokens = tokens[: operationIndex] + translation + tokens[tokenIndex: ]
                    tokenIndex += len(translation) - (numberOfOperands + 3)
                case "SETMY":
                    debug.expectedNumberOfOperands = (1, )
                    if numberOfOperands not in debug.expectedNumberOfOperands:
                        incorrectNumberOfOperands(debug)
                    if operands[0][0].isnumeric():
                        raise Exception(f"FATAL - SETMY cannot accept immediate values\nOn line: {line}")
                    
                    translation = ["ADD", "(", "SR", operands[0], "R0", ")", "SPT", "(", "155", ")"]
                    tokens = tokens[: operationIndex] + translation + tokens[tokenIndex: ]
                    tokenIndex += len(translation) - (numberOfOperands + 3)
                case "PRT":
                    debug.expectedNumberOfOperands = (1, )
                    if numberOfOperands not in debug.expectedNumberOfOperands:
                        incorrectNumberOfOperands(debug)
                    
                    translation = ["ADD", "(", "DSW", operands[0], "R0", ")"]
                    tokens = tokens[: operationIndex] + translation + tokens[tokenIndex: ]
                    tokenIndex += len(translation) - (numberOfOperands + 3)
                case "VSH":
                    debug.expectedNumberOfOperands = (0, )
                    if numberOfOperands not in debug.expectedNumberOfOperands:
                        incorrectNumberOfOperands(debug)
                    
                    translation = ["SPT", "(", "151", ")"]
                    tokens = tokens[: operationIndex] + translation + tokens[tokenIndex: ]
                    tokenIndex += len(translation) - (numberOfOperands + 3)
                case "SPT":
                    debug.expectedNumberOfOperands = (1, )
                    if numberOfOperands not in debug.expectedNumberOfOperands:
                        incorrectNumberOfOperands(debug)
                        
                    if not operands[0][0].isnumeric():
                        translation = ["ADD", "(", "SP", operands[0], "R0", ")"]
                        tokens = tokens[: operationIndex] + translation + tokens[tokenIndex: ]
                        tokenIndex += len(translation) - (numberOfOperands + 3)
                case "RPT":
                    debug.expectedNumberOfOperands = (1, )
                    if numberOfOperands not in debug.expectedNumberOfOperands:
                        incorrectNumberOfOperands(debug)
                        
                    if not operands[0][0].isnumeric():
                        translation = ["ADD", "(", "RP", operands[0], "R0", ")"]
                        tokens = tokens[: operationIndex] + translation + tokens[tokenIndex: ]
                        tokenIndex += len(translation) - (numberOfOperands + 3)
                case "HLT":
                    debug.expectedNumberOfOperands = (0, )
                    if numberOfOperands not in debug.expectedNumberOfOperands:
                        incorrectNumberOfOperands(debug)
                        
                    translation = ["SPT", "(", "150", ")", "STL", "(", ")", "LSL", "(", ")"]
                    tokens = tokens[: operationIndex] + translation + tokens[tokenIndex: ]
                    tokenIndex += len(translation) - (numberOfOperands + 3)
                case "JMP":
                    debug.expectedNumberOfOperands = (1, )
                    if numberOfOperands not in debug.expectedNumberOfOperands:
                        incorrectNumberOfOperands(debug)
                case "RET":
                    debug.expectedNumberOfOperands = (0, )
                    if numberOfOperands not in debug.expectedNumberOfOperands:
                        incorrectNumberOfOperands(debug)
                case "STL":
                    debug.expectedNumberOfOperands = (0, 1)
                    if numberOfOperands not in debug.expectedNumberOfOperands:
                        incorrectNumberOfOperands(debug)
                    
                    if numberOfOperands == 1:
                        translation = ["STL", "(", ")", "JMP", "(", operands[0], ")"]
                        tokens = tokens[: operationIndex] + translation + tokens[tokenIndex: ]
                        tokenIndex += len(translation) - (numberOfOperands + 3)
                case "FFG":
                    debug.expectedNumberOfOperands = (0, )
                    if numberOfOperands not in debug.expectedNumberOfOperands:
                        incorrectNumberOfOperands(debug)
                case "CLR":
                    debug.expectedNumberOfOperands = (0, )
                    if numberOfOperands not in debug.expectedNumberOfOperands:
                        incorrectNumberOfOperands(debug)
                    
                    translation = ["SPT", "(", "149", ")"]
                    tokens = tokens[: operationIndex] + translation + tokens[tokenIndex: ]
                    tokenIndex += len(translation) - (numberOfOperands + 3)
                case "STR":
                    debug.expectedNumberOfOperands = (1, )
                    if numberOfOperands not in debug.expectedNumberOfOperands:
                        incorrectNumberOfOperands(debug)
                    
                    translation = ["ADD", "(", "SR", operands[0], "R0", ")"]
                    tokens = tokens[: operationIndex] + translation + tokens[tokenIndex: ]
                    tokenIndex += len(translation) - (numberOfOperands + 3)
                case "LOD":
                    debug.expectedNumberOfOperands = (1, )
                    if numberOfOperands not in debug.expectedNumberOfOperands:
                        incorrectNumberOfOperands(debug)
                    
                    translation = ["ADD", "(", operands[0], "SR", "R0", ")"]
                    tokens = tokens[: operationIndex] + translation + tokens[tokenIndex: ]
                    tokenIndex += len(translation) - (numberOfOperands + 3)
                case "OR":
                    debug.expectedNumberOfOperands = (2, 3)
                    if numberOfOperands not in debug.expectedNumberOfOperands:
                        incorrectNumberOfOperands(debug)
                    
                    if numberOfOperands == 2:
                        translation = ["OR", "(", operands[0], operands[0], operands[1], ")"]
                        tokens = tokens[: operationIndex] + translation + tokens[tokenIndex: ]
                        tokenIndex += len(translation) - (numberOfOperands + 3)
                case "NAND":
                    debug.expectedNumberOfOperands = (2, 3)
                    if numberOfOperands not in debug.expectedNumberOfOperands:
                        incorrectNumberOfOperands(debug)
                    
                    if numberOfOperands == 2:
                        translation = ["OR", "(", operands[0], f"!{operands[0]}", f"!{operands[1]}", ")"]
                        tokens = tokens[: operationIndex] + translation + tokens[tokenIndex: ]
                        tokenIndex += len(translation) - (numberOfOperands + 3)
                    elif numberOfOperands == 3:
                        translation = ["OR", "(", operands[0], f"!{operands[1]}", f"!{operands[2]}", ")"]
                        tokens = tokens[: operationIndex] + translation + tokens[tokenIndex: ]
                        tokenIndex += len(translation) - (numberOfOperands + 3)
                case "DSL":
                    debug.expectedNumberOfOperands = (0, 1)
                    if numberOfOperands not in debug.expectedNumberOfOperands:
                        incorrectNumberOfOperands(debug)
                    
                    if numberOfOperands == 1:
                        translation = ["DSL", "(", ")", "JMP", "(", operands[0], ")"]
                        tokens = tokens[: operationIndex] + translation + tokens[tokenIndex: ]
                        tokenIndex += len(translation) - (numberOfOperands + 3)
                case "LSL":
                    debug.expectedNumberOfOperands = (0, 1)
                    if numberOfOperands not in debug.expectedNumberOfOperands:
                        incorrectNumberOfOperands(debug)
                    
                    number = int(operands[0]) - 6
                    if number < 0:
                        number += 256
                    operands[0] = str(number)
                    
                    if numberOfOperands == 1:
                        translation = ["STL", "(", ")", "JMP", "(", operands[0], ")", "LSL", "(", ")"]
                        tokens = tokens[: operationIndex] + translation + tokens[tokenIndex: ]
                        tokenIndex += len(translation) - (numberOfOperands + 3)
                case "CMP":
                    debug.expectedNumberOfOperands = (1, 2)
                    if numberOfOperands not in debug.expectedNumberOfOperands:
                        incorrectNumberOfOperands(debug)
                    
                    if numberOfOperands == 1:
                        translation = ["ADD", "(", "R0", operands[0], "R0", ")"]
                        tokens = tokens[: operationIndex] + translation + tokens[tokenIndex: ]
                        tokenIndex += len(translation) - (numberOfOperands + 3)
                    elif numberOfOperands == 2:
                        translation = ["ADC", "(", "R0", operands[0], f"!{operands[1]}", ")"]
                        tokens = tokens[: operationIndex] + translation + tokens[tokenIndex: ]
                        tokenIndex += len(translation) - (numberOfOperands + 3)
                case "DLSL":
                    debug.expectedNumberOfOperands = (0, 1)
                    if numberOfOperands not in debug.expectedNumberOfOperands:
                        incorrectNumberOfOperands(debug)
                    
                    number = int(operands[0]) - 6
                    if number < 0:
                        number += 256
                    operands[0] = str(number)
                    
                    if numberOfOperands == 1:
                        translation = ["DSL", "(", ")", "JMP", "(", operands[0], ")", "LSL", "(", ")"]
                        tokens = tokens[: operationIndex] + translation + tokens[tokenIndex: ]
                        tokenIndex += len(translation) - (numberOfOperands + 3)
                case _:
                    raise Exception(f"FATAL - Unrecognised Operation: {operation}\nIn line: {line}")
        
        else:
            tokenIndex += 1

    return tuple(tokens)



