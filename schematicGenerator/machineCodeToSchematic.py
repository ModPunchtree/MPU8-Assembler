
from os import system, getcwd, name as osname

from os.path import normpath

def runCommand () -> None:

    currentDirectory = getcwd ()

    if osname == "nt":
        system (f"{currentDirectory}\\schematics\\command.cmd") # no need to account for posix on a nt system
    elif osname == "posix":
        system (f"wine cmd.exe /c {currentDirectory}/schematics/command.cmd") # no need to account for nt on a posix system
    else:
        print (f"unknown system {osname}")

def fetchEmptyInstructionROM() -> tuple:
    
    f = open( normpath ("schematics/MPU8_INSROM.snbt"), "r")
    result = f.read()
    f.close()
    
    index = result.index("BlockData:") + len("BlockData:")
    start = result[: index]
    result = result[index: ]
    index = result.index("]") + 1
    end = result[index: ]
    result = result[: index]
    result = result.replace("b", "")
    result = result.replace("B;", "")
    result = eval(result)
    index = 0
    while index < len(result):
        if result[index] < 0:
            result[index] += 256
            result.pop(index + 1)
        index += 1
    
    return start, result, end

def fetchEmptyImmediateROM() -> tuple:

    f = open( normpath ("schematics/MPU8_IMMROM.snbt"), "r")
    result = f.read()
    f.close()
    
    index = result.index("BlockData:") + len("BlockData:")
    start = result[: index]
    result = result[index: ]
    index = result.index("]") + 1
    end = result[index: ]
    result = result[: index]
    result = result.replace("b", "")
    result = result.replace("B;", "")
    result = eval(result)
    index = 0
    while index < len(result):
        if result[index] < 0:
            result[index] += 256
            result.pop(index + 1)
        index += 1
    
    return start, result, end

def generateSchematics(instructionROM: list, immediateROM: list, name: str) -> None:
    
    currentDirectory = getcwd()
    
    start, outputBlocks, end = fetchEmptyInstructionROM()

    lengthX = 79
    lengthY = 39
    lengthZ = 59

    for flag in range(2):
        for instruction in range(256):
            for bit in range(24):
                value = instructionROM[instruction][flag][bit]

                # x coord
                blockX = (((15 - ((instruction >> 1) % 16)) * 5) + 1) + 1 - (instruction % 2)
                
                # y coord
                blockY = (((instruction >> 5) * 5) + 2) + flag
                
                # z coord
                blockZ = ((bit % 12) * 2) + 1
                if bit > 11:
                    blockZ += 34
                if flag and (bit < 12):
                    blockZ -= 1
                elif flag:
                    blockZ += 1

                blockIndex = blockX + (blockZ * lengthX) + (blockY * lengthX * lengthZ)
                    
                if value:
                    if (flag == 0) and (bit % 2):
                        outputBlocks[blockIndex] = 94 # 94 = south torch
                    elif flag == 0:
                        outputBlocks[blockIndex] = 93 # 93 = north torch
                    elif (bit in (4, 19)) and (instruction % 2):
                        outputBlocks[blockIndex] = 211 # 211 = east torch
                    elif bit in (4, 19):
                        outputBlocks[blockIndex] = 210 # 210 = west torch
                    else:
                        outputBlocks[blockIndex] = 212 # 212 = top torch
                else:
                    outputBlocks[blockIndex] = 0 # 0 = glowstone
    
    index = 0
    while index < len(outputBlocks):
        if outputBlocks[index] >= 128:
            outputBlocks[index] -= 256
            outputBlocks.insert(index + 1, 1)
        index += 1
    
    outputBlocks = str(outputBlocks).replace(" ", "")
    outputBlocks = outputBlocks[: -1] + "b]"
    outputBlocks = "[B;" + outputBlocks[1: ]
    outputBlocks = outputBlocks.replace(",", "b,")
    
    result = start + outputBlocks + end
    
    f = open( normpath (f"schematics/{name}_INSROM.snbt"), "w")
    f.write(result)
    f.close()
    
    command = f"""cd \"{currentDirectory}\\schematics\"
SnbtCmd.exe path \"{currentDirectory}\\schematics\\{name}_INSROM.snbt\" to-nbt > \"{name}_INSROM.schematic\"
gzip \"{name}_INSROM.schematic\"
rename \"{currentDirectory}\\schematics\\{name}_INSROM.schematic.gz\" \"{name}_INSROM.schematic\""""
    f = open( normpath ("schematics/command.cmd"), "w")
    f.write(command)
    f.close()
    
    runCommand ()

    ################################################################################
    
    # Immediate ROM
    
    ################################################################################

    start, outputBlocks, end = fetchEmptyImmediateROM()

    lengthX = 67
    lengthY = 33
    lengthZ = 41
    
    for flag in range(2):
        for instruction in range(256):
            for bit in range(8):
                value = immediateROM[instruction][flag][bit]
                
                # x coord
                blockX = (63 - ((instruction & 31) << 1))
                if (instruction + 1) & 7:
                    blockX -= (1 - ((7 - bit) & 1))
                
                # y coord
                if instruction & 1:
                    if (instruction + 1) & 7:
                        blockY = ((((7 - bit) + 1) - (((7 - bit) + 1) & 1)) << 1) + (1 - ((7 - bit) & 1))
                    else:
                        blockY = 2 + ((7 - bit) << 1)
                else:
                    blockY = 2 + (((7 - bit) - ((7 - bit) & 1)) << 1) + ((7 - bit) & 1)
                if flag == 0:
                    blockY += 16
                
                # z coord
                blockZ = (36, 34, 26, 24, 16, 14, 6, 4)[instruction >> 5]
                
                blockIndex = blockX + (blockZ * lengthX) + (blockY * lengthX * lengthZ)
                
                
                if ((instruction + 1) & 7 == 0) and (bit & 1):
                    if value == 1:
                        outputBlocks[blockIndex] = 4 # torch east
                    else:
                        outputBlocks[blockIndex] = 0 # glowstone
                elif (instruction >> 5) & 1:
                    if value == 1:
                        outputBlocks[blockIndex] = 5 # torch south
                    else:
                        outputBlocks[blockIndex] = 0 # glowstone
                else:
                    if value == 1:
                        outputBlocks[blockIndex] = 1 # torch north
                    else:
                        outputBlocks[blockIndex] = 0 # glowstone

    index = 0
    while index < len(outputBlocks):
        if outputBlocks[index] >= 128:
            outputBlocks[index] -= 256
            outputBlocks.insert(index + 1, 1)
        index += 1

    outputBlocks = str(outputBlocks).replace(" ", "")
    outputBlocks = outputBlocks[: -1] + "b]"
    outputBlocks = "[B;" + outputBlocks[1: ]
    outputBlocks = outputBlocks.replace(",", "b,")
    
    result = start + outputBlocks + end
    
    f = open( normpath (f"schematics/{name}_IMMROM.snbt"), "w")
    f.write(result)
    f.close()
    
    command = f"""cd \"{currentDirectory}\\schematics\"
SnbtCmd.exe path \"{currentDirectory}\\schematics\\{name}_IMMROM.snbt\" to-nbt > \"{name}_IMMROM.schematic\"
gzip \"{name}_IMMROM.schematic\"
rename \"{currentDirectory}\\schematics\\{name}_IMMROM.schematic.gz\" \"{name}_IMMROM.schematic\""""
    f = open( normpath ("schematics/command.cmd"), "w")
    f.write(command)
    f.close()
    
    runCommand ()
