
def operations() -> tuple:
    return ("NOP", "RST", "ADD", "ADC", "SUB", "SBB", "MOV", "IMM", "INC", "DEC", "NEG", "LSH", "LSC", "LCF","RCF", "NOR", "AND", "NOT", "FLG", "SETX", "SETY", "SETMX", "SETMY", "PRT", "VSH", "SPT", "RPT", "HLT", "JMP", "RET", "STL", "FFG", "CLR", "STR", "LOD", "OR", "NAND", "DSL", "LSL", "CMP", "DLSL")

def convertMMIOPointers(key: str) -> str:
    key = key.upper()
    MMIOPointers = {
        "*MULTA": 128,
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
        "*SHIFTY": 165
        }
    return str(MMIOPointers[key])

def convertChar(char: str) -> str:
    char = char[1: -1]
    characterSet = {
        "0": "0",
        "1": "1",
        "2": "2",
        "3": "3",
        "4": "4",
        "5": "5",
        "6": "6",
        "7": "7",
        "8": "8",
        "9": "9",
        "A": "10",
        "B": "11",
        "C": "12",
        "D": "13",
        "E": "14",
        "F": "15",
        "G": "16",
        "H": "17",
        "I": "18",
        "J": "19",
        "K": "20",
        "L": "21",
        "M": "22",
        "N": "23",
        "O": "24",
        "P": "25",
        "Q": "26",
        "R": "27",
        "S": "28",
        "T": "29",
        "U": "30",
        "V": "31",
        "W": "32",
        "X": "33",
        "Y": "34",
        "Z": "35",
        "a": "36",
        "b": "37",
        "c": "38",
        "d": "39",
        "e": "40",
        "f": "41",
        "g": "42",
        "h": "43",
        "i": "44",
        "j": "45",
        "k": "46",
        "l": "47",
        "m": "48",
        "n": "49",
        "o": "50",
        "p": "51",
        "q": "52",
        "r": "53",
        "s": "54",
        "t": "55",
        "u": "56",
        "v": "57",
        "w": "58",
        "x": "59",
        "y": "60",
        "z": "61",
        "00": "62",
        "01": "63",
        "10": "64",
        "11": "65",
        "20": "66",
        "21": "67",
        "30": "68",
        "31": "69",
        "40": "70",
        "41": "71",
        "50": "72",
        "51": "73",
        "60": "74",
        "61": "75",
        "70": "76",
        "71": "77",
        "80": "78",
        "81": "79",
        "90": "80",
        "91": "81",
        "A0": "82",
        "A1": "83",
        "B0": "84",
        "B1": "85",
        "C0": "86",
        "C1": "87",
        "D0": "88",
        "D1": "89",
        "E0": "90",
        "E1": "91",
        "F0": "92",
        "F1": "93",
        "G0": "94",
        "G1": "95",
        "H0": "96",
        "H1": "97",
        "I0": "98",
        "I1": "99",
        "J0": "100",
        "J1": "101",
        "K0": "102",
        "K1": "103",
        "L0": "104",
        "L1": "105",
        "M0": "106",
        "M1": "107",
        "N0": "108",
        "N1": "109",
        "O0": "110",
        "O1": "111",
        "P0": "112",
        "P1": "113",
        "Q0": "114",
        "Q1": "115",
        "R0": "116",
        "R1": "117",
        "S0": "118",
        "S1": "119",
        "T0": "120",
        "T1": "121",
        "U0": "122",
        "U1": "123",
        "V0": "124",
        "V1": "125",
        "W0": "126",
        "W1": "127",
        "X0": "128",
        "X1": "129",
        "Y0": "130",
        "Y1": "131",
        "Z0": "132",
        "Z1": "133",
        "a0": "134",
        "a1": "135",
        "b0": "136",
        "b1": "137",
        "c0": "138",
        "c1": "139",
        "d0": "140",
        "d1": "141",
        "e0": "142",
        "e1": "143",
        "f0": "144",
        "f1": "145",
        "g0": "146",
        "g1": "147",
        "h0": "148",
        "h1": "149",
        "i0": "150",
        "i1": "151",
        "j0": "152",
        "j1": "153",
        "k0": "154",
        "k1": "155",
        "l0": "156",
        "l1": "157",
        "m0": "158",
        "m1": "159",
        "n0": "160",
        "n1": "161",
        "o0": "162",
        "o1": "163",
        "p0": "164",
        "p1": "165",
        "q0": "166",
        "q1": "167",
        "r0": "168",
        "r1": "169",
        "s0": "170",
        "s1": "171",
        "t0": "172",
        "t1": "173",
        "u0": "174",
        "u1": "175",
        "v0": "176",
        "v1": "177",
        "w0": "178",
        "w1": "179",
        "x0": "180",
        "x1": "181",
        "y0": "182",
        "y1": "183",
        "z0": "184",
        "z1": "185",
        "+": "186",
        "-": "187",
        "=": "188",
        "/": "189",
        "*": "190",
        "!": "191",
        "?": "192",
        "%": "193",
        ".": "194",
        ",": "195",
        "(": "196",
        ")": "197",
        "[": "198",
        "]": "199",
        "{": "200",
        "}": "201",
        "<": "202",
        ">": "203",
        "<=": "204",
        ">=": "205",
        ":": "206",
        ";": "207",
        "_": "208",
        "|": "209",
        "||": "210",
        "^": "211",
        "~": "212",
        "\\": "213",
        "°": "214",
        "&": "215",
        "\"": "216",
        "@": "217",
        "'": "218",
        "$": "219",
        " ": "220",
        "LH": "221",
        "HL": "222",
        "HH": "223"
    }
    
    return characterSet[char]

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
                    
                    translation = []
                    tokens = tokens[: operationIndex] + translation + tokens[tokenIndex: ]
                    tokenIndex += len(translation) - (numberOfOperands + 3)
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
                    
                    translation = ["ADD", "(", "R0", operands[0], "DSW", ")"]
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



