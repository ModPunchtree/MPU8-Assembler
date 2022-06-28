
from assembler.codeCleaner import cleanCode

def writeMain(key: str, lineNumber: int, flag: int) -> None:
    if safetyValues["main"]:
        raise Exception(f"FATAL - Multiple main operations on lineNumber: {lineNumber} flag: {bool(flag)}")
    safetyValues["main"] = True
    mainDict = {"ADD": [0, 0],
                "ADC": [0, 1],
                "ACF": [1, 0],
                "NOR": [1, 0],
                "OR": [1, 0],
                "RCF": [1, 1]}
    try:
        INSROM[lineNumber][flag][9: 11] = mainDict[key]
    except:
        raise Exception(f"FATAL - Unrecognised main operation: {key}\non lineNumber: {lineNumber} flag: {bool(flag)}")

def writeCSide(key: str, lineNumber: int, flag: int) -> None:
    if safetyValues["cSide"]:
        raise Exception(f"FATAL - Multiple C Side operations on lineNumber: {lineNumber} flag: {bool(flag)}")
    safetyValues["cSide"] = True
    cSideDict = {"R0": [0, 0, 0, 0],
                 "R1": [0, 0, 0, 1],
                 "R2": [0, 0, 1, 0],
                 "R3": [0, 0, 1, 1],
                 "R4": [0, 1, 0, 0],
                 "R5": [0, 1, 0, 1],
                 "R6": [0, 1, 1, 0],
                 "R7": [0, 1, 1, 1],
                 "R8": [1, 0, 0, 0],
                 "R9": [1, 0, 0, 1],
                 "R10": [1, 0, 1, 0],
                 "R11": [1, 0, 1, 1],
                 "R12": [1, 1, 0, 0],
                 "SR": [1, 1, 0, 1],
                 "RP": [1, 1, 1, 0],
                 "SP": [1, 1, 1, 1]}
    try:
        INSROM[lineNumber][flag][20: 24] = cSideDict[key]
    except:
        raise Exception(f"FATAL - Unrecognised C side value: {key}\non lineNumber: {lineNumber} flag: {bool(flag)}")

def writeASide(key: str, lineNumber: int, flag: int) -> None:
    if safetyValues["aSide"]:
        raise Exception(f"FATAL - Multiple A Side operations on lineNumber: {lineNumber} flag: {bool(flag)}")
    safetyValues["aSide"] = True
    
    if key.startswith("!"):
        INSROM[lineNumber][flag][15] = 1
        key = key[1: ]
    
    if key[0].isnumeric():
        writeImmediate(key, lineNumber, flag)
        key = "AI"
    
    aSideDict = {"R0": [0, 0, 0, 0],
                 "R1": [0, 0, 0, 1],
                 "R2": [0, 0, 1, 0],
                 "R3": [0, 0, 1, 1],
                 "R4": [0, 1, 0, 0],
                 "R5": [0, 1, 0, 1],
                 "R6": [0, 1, 1, 0],
                 "R7": [0, 1, 1, 1],
                 "R8": [1, 0, 0, 0],
                 "R9": [1, 0, 0, 1],
                 "R10": [1, 0, 1, 0],
                 "R11": [1, 0, 1, 1],
                 "R12": [1, 1, 0, 0],
                 "AI": [1, 1, 0, 1],
                 "SR": [1, 1, 1, 0],
                 "-": [1, 1, 1, 1]}
    try:
        INSROM[lineNumber][flag][16: 20] = aSideDict[key]
    except:
        raise Exception(f"FATAL - Unrecognised A side value: {key}\non lineNumber: {lineNumber} flag: {bool(flag)}")

def writeBSide(key: str, lineNumber: int, flag: int) -> None:
    if safetyValues["bSide"]:
        raise Exception(f"FATAL - Multiple B Side operations on lineNumber: {lineNumber} flag: {bool(flag)}")
    safetyValues["bSide"] = True
    
    if key.startswith("!"):
        INSROM[lineNumber][flag][8] = 1
        key = key[1: ]
    
    if key[0].isnumeric():
        writeImmediate(key, lineNumber, flag)
        key = "BI"
    
    bSideDict = {"R0": [0, 0, 0, 0],
                 "R1": [0, 0, 0, 1],
                 "R2": [0, 0, 1, 0],
                 "R3": [0, 0, 1, 1],
                 "R4": [0, 1, 0, 0],
                 "R5": [0, 1, 0, 1],
                 "R6": [0, 1, 1, 0],
                 "R7": [0, 1, 1, 1],
                 "R8": [1, 0, 0, 0],
                 "R9": [1, 0, 0, 1],
                 "R10": [1, 0, 1, 0],
                 "R11": [1, 0, 1, 1],
                 "R12": [1, 1, 0, 0],
                 "BI": [1, 1, 0, 1],
                 "DSR": [1, 1, 1, 0],
                 "DSW": [1, 1, 1, 1]}
    try:
        INSROM[lineNumber][flag][4: 8] = bSideDict[key]
    except:
        raise Exception(f"FATAL - Unrecognised B side value: {key}\non lineNumber: {lineNumber} flag: {bool(flag)}")

def writeFlag(key: str, lineNumber: int, flag: int) -> None:
    if safetyValues["flag"]:
        raise Exception(f"FATAL - Multiple flag operations on lineNumber: {lineNumber} flag: {bool(flag)}")
    safetyValues["flag"] = True
    
    flagDict = {"-": [0, 0, 0, 0],
                "CF": [0, 0, 0, 1],
                "!CF": [0, 0, 1, 0],
                "ZF": [0, 0, 1, 1],
                "!ZF": [0, 1, 0, 0],
                "NE": [0, 1, 0, 1],
                "PO": [0, 1, 1, 0],
                "OD": [0, 1, 1, 1],
                "EV": [1, 0, 0, 0],
                "IN": [1, 0, 0, 1],
                "EN": [1, 0, 1, 0],
                "LE": [1, 0, 1, 1],
                "GR": [1, 1, 0, 0],
                "TR": [1, 1, 0, 1],
                "RPT": [1, 1, 1, 0],
                "LSL": [1, 1, 1, 1]}
    try:
        INSROM[lineNumber][flag][0: 4] = flagDict[key]
    except:
        raise Exception(f"FATAL - Unrecognised flag: {key}\non lineNumber: {lineNumber} flag: {bool(flag)}")

def writeImmediate(immediate: str, lineNumber: int, flag: int) -> None:
    if safetyValues["IMM"]:
        raise Exception(f"FATAL - Multiple immediate values on lineNumber: {lineNumber} flag: {bool(flag)}")
    safetyValues["IMM"] = True

    immediate = int(immediate, 0)
    if immediate > 255:
        raise Exception(f"FATAL - Immediate value: {immediate} does not fit in 8 bits\non lineNumber: {lineNumber} flag: {bool(flag)}")
    immediate = bin(immediate)[2: ]
    while len(immediate) < 8:
        immediate = "0" + immediate
    IMMROM[lineNumber][flag] = [int(i) for i in immediate]

def writeBranch(key: str, lineNumber: int, flag: int) -> None:
    if safetyValues["branch"]:
        raise Exception(f"FATAL - Multiple branch operations on lineNumber: {lineNumber} flag: {bool(flag)}")
    safetyValues["branch"] = True

    branchDict = {"-": [0, 0],
                  "JMP": [0, 1],
                  "RET": [1, 0],
                  "SPT": [1, 1]}
    try:
        INSROM[lineNumber][flag][11: 13] = branchDict[key]
    except:
        raise Exception(f"FATAL - Unrecognised branch: {key}\non lineNumber: {lineNumber} flag: {bool(flag)}")

def writeFlagMultiplexer(key: str, lineNumber: int, flag: int) -> None:
    if safetyValues["flagMultiplexer"]:
        raise Exception(f"FATAL - Multiple flag multiplexer operations on lineNumber: {lineNumber} flag: {bool(flag)}")
    safetyValues["flagMultiplexer"] = True

    flagMultiplexerDict = {"FFG": [0, 0],
                           "-": [0, 1],
                           "STL": [1, 0],
                           "DSL": [1, 1]}
    try:
        INSROM[lineNumber][flag][13: 15] = flagMultiplexerDict[key]
    except:
        raise Exception(f"FATAL - Unrecognised flag multiplexer operation: {key}\non lineNumber: {lineNumber} flag: {bool(flag)}")

def assemble(rawCode: str) -> list:
    
    code = cleanCode(rawCode)
    
    global INSROM
    INSROM = [[[0 for bitIndex in range(24)] for flag in range(2)] for instructionNumber in range(256)]
    for flag in range(2):
        for instructionNumber in range(256):
            INSROM[instructionNumber][flag][14] = 1 # fix FFG jank
    
    global IMMROM
    IMMROM = [[[0 for bitIndex in range(8)] for flag in range(2)] for instructionNumber in range(256)]

    if len(code) > 256:
        raise Exception(f"FATAL - Code is longer than 256 lines\nThe code is currently {len(code)} lines long")
    
    for lineNumber, line in enumerate(code):
        global safetyValues
        safetyValues = {"flag": False,
                        "bSide": False,
                        "main": False,
                        "branch": False,
                        "flagMultiplexer": False,
                        "aSide": False,
                        "cSide": False,
                        "IMM": False}
        
        tokenNumber = 0
        flag = 0
        while tokenNumber < len(line):
            if line[tokenNumber] in ("ADD", "ADC", "ACF", "NOR", "OR", "RCF"):
                writeMain(line[tokenNumber], lineNumber, flag)
                tokenNumber += 2
                
                writeCSide(line[tokenNumber], lineNumber, flag)
                tokenNumber += 1

                writeASide(line[tokenNumber], lineNumber, flag)
                tokenNumber += 1
                
                writeBSide(line[tokenNumber], lineNumber, flag)
                tokenNumber += 2
            
            elif line[tokenNumber] == "FLG":
                tokenNumber += 2
                writeFlag(line[tokenNumber], lineNumber, flag)
                tokenNumber += 2
            
            elif line[tokenNumber] == "RPT":
                writeFlag(line[tokenNumber], lineNumber, flag)
                tokenNumber += 2
                if line[tokenNumber][0].isnumeric():
                    writeImmediate(line[tokenNumber], lineNumber, flag)
                    tokenNumber += 1
                tokenNumber += 1
            
            elif line[tokenNumber] == "LSL":
                writeFlag(line[tokenNumber], lineNumber, flag)
                tokenNumber += 3

            elif line[tokenNumber] in ("JMP", "RET", "SPT"):
                writeBranch(line[tokenNumber], lineNumber, flag)
                tokenNumber += 2
                if line[tokenNumber][0].isnumeric():
                    writeImmediate(line[tokenNumber], lineNumber, flag)
                    tokenNumber += 1
                tokenNumber += 1
            
            elif line[tokenNumber] in ("FFG", "STL", "DSL"):
                writeFlagMultiplexer(line[tokenNumber], lineNumber, flag)
                tokenNumber += 3
                
            elif line[tokenNumber] == ";":
                
                if flag == 0:
                    safetyValues["flag"] = False
                    safetyValues["bSide"] = False
                    safetyValues["main"] = False
                    safetyValues["branch"] = False
                    safetyValues["flagMultiplexer"] = False
                    safetyValues["aSide"] = False
                    safetyValues["cSide"] = False
                    safetyValues["IMM"] = False
                    flag = 1
                    
                tokenNumber += 1

            else:
                raise Exception(f"FATAL - Unrecognised operation: {line[tokenNumber]}\non line: {line}")

    return INSROM, IMMROM










