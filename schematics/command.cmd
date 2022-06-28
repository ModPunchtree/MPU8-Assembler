cd "C:\Users\modpu\OneDrive\Repositories\MPU8-Assembler\schematics"
SnbtCmd.exe path "C:\Users\modpu\OneDrive\Repositories\MPU8-Assembler\schematics\test_IMMROM.snbt" to-nbt > "test_IMMROM.schematic"
gzip "test_IMMROM.schematic"
rename "C:\Users\modpu\OneDrive\Repositories\MPU8-Assembler\schematics\test_IMMROM.schematic.gz" "test_IMMROM.schematic"