
from os.path import normpath

def fetchRawMPU8Code(name: str) -> str:
    
    fileName = f"MPU8Code/{name}.mpu8"
    
    file = open( normpath (fileName), "r")
    answer = file.read()
    file.close()
    
    return answer

def fetchRawURCLCode(name: str) -> str:
    
    fileName = f"MPU8Code/URCLCode/{name}.mpu8"
    
    file = open( normpath (fileName), "r")
    answer = file.read()
    file.close()
    
    return answer



