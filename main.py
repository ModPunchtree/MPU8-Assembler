
from assembler.assembler import assemble
from assembler.fileParse import fetchRawMPU8Code

source = input("Input file name without extension: ")

rawCode = fetchRawMPU8Code(source)

instructionROM, immediateROM = assemble(rawCode)

# column checksums
nonFlagROMColumns = []
flagROMColumns = []
for column in range(24):
    nonFlagROMColumns.append([instructionROM[lineNumber][0][column] for lineNumber in range(256)])
    flagROMColumns.append([instructionROM[lineNumber][1][column] for lineNumber in range(256)])
    
nonFlagColumnChecksums = [str(sum(nonFlagROMColumns[column])) for column in range(24)]
flagColumnChecksums = [str(sum(flagROMColumns[column])) for column in range(24)]

nonFlagROM = ""
flagROM = ""
nonFlagImmediate = ""
flagImmediate = ""
for lineNumber in range(256):
    if lineNumber < 10:
        flagROM += " "
        nonFlagROM += " "
        nonFlagImmediate += " "
        flagImmediate += " "
    if lineNumber < 100:
        flagROM += " "
        nonFlagROM += " "
        nonFlagImmediate += " "
        flagImmediate += " "
    flagROM += str(lineNumber) + ": "
    nonFlagROM += str(lineNumber) + ": "
    nonFlagImmediate += str(lineNumber) + ": "
    flagImmediate += str(lineNumber) + ": "
    temp = sum(instructionROM[lineNumber][1])
    if temp > 0:
        flagROM += f"{instructionROM[lineNumber][1][: 12]}{instructionROM[lineNumber][1][12: ]} {temp}*\n"
    else:
        flagROM += f"{instructionROM[lineNumber][1][: 12]}{instructionROM[lineNumber][1][12: ]}\n"
    temp = sum(instructionROM[lineNumber][0])
    if temp > 0:
        nonFlagROM += f"{instructionROM[lineNumber][0][: 12]}{instructionROM[lineNumber][0][12: ]} {temp}*\n"
    else:
        nonFlagROM += f"{instructionROM[lineNumber][0][: 12]}{instructionROM[lineNumber][0][12: ]}\n"
    temp = sum(immediateROM[lineNumber][0])
    if temp > 0:
        nonFlagImmediate += f"{immediateROM[lineNumber][0][: 4]}{immediateROM[lineNumber][0][4: ]} {temp}*\n"
    else:
        nonFlagImmediate += f"{immediateROM[lineNumber][0][: 4]}{immediateROM[lineNumber][0][4: ]}\n"
    temp = sum(immediateROM[lineNumber][1])
    if temp > 0:
        flagImmediate += f"{immediateROM[lineNumber][1][: 4]}{immediateROM[lineNumber][1][4: ]} {temp}*\n"
    else:
        flagImmediate += f"{immediateROM[lineNumber][1][: 4]}{immediateROM[lineNumber][1][4: ]}\n"
        
nonflagColumn = "     " + " ".join(nonFlagColumnChecksums[: 12]) + " | " + " ".join(nonFlagColumnChecksums[12: ])
flagColumn = "     " + " ".join(flagColumnChecksums[: 12]) + " | " + " ".join(flagColumnChecksums[12: ])

answer = ((f"Non-flag Instruction ROM:\n{nonFlagROM}{nonflagColumn}\n\nFlag Instruction ROM:\n{flagROM}{flagColumn}\n\nNon-flag Immediate ROM\n{nonFlagImmediate}\nFlag Immediate ROM\n{flagImmediate}").replace(",", " ")).replace("][", " | ")

print(answer)




