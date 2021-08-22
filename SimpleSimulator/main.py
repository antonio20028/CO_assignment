import sys
import operations

mem = []
program_counter = 0
halted = False

reg_file = {
    "000": 0,
    "001": 0,
    "010": 0,
    "011": 0,
    "100": 0,
    "101": 0,
    "110": 0,
    "111": 0}

TYPE_A = ["00000", "00001", "00110", "01010", "01011", "01100"]
TYPE_B = ["00010", "01000", "01001"]
TYPE_C = ["00111", "01101", "01110"]
TYPE_D = ["00100", "00101"]
TYPE_E = ["01111", "10000", "10001", "10010"]
TYPE_F = ["10011"]


#helper functions
def get_binary(value, width):
    res = bin(value)
    return res[2:].zfill(width)

def initialize(single_line):
    opcode = single_line[:5]
    reg = []
    instruction = dict()

    if opcode in TYPE_A:
        reg.append(single_line[7:10])
        reg.append(single_line[10:13])
        reg.append(single_line[13:16])
        instruction[opcode] = reg
        mem.append(instruction)

    elif opcode in TYPE_B:
        reg.append(single_line[7:10])
        reg.append(single_line[10:])
        instruction[opcode] = reg
        mem.append(instruction)
    
    elif opcode in TYPE_C:
        reg.append(single_line[10:13])
        reg.append(single_line[13:16])
        instruction[opcode] = reg
        mem.append(instruction)

    elif opcode in TYPE_D:
        reg.append(single_line[7:10])
        reg.append(single_line[10:])
        instruction[opcode] = reg
        mem.append(instruction)

    elif opcode in TYPE_E:
        reg.append(single_line[10:])
        instruction[opcode] = reg
        mem.append(instruction)
    
    else:
        sys.exit()

def exectute(instruction):

    return 0

def get_register_file():
    for line in reg_file.keys():
        print(reg_file[line])

if __name__ == "__main__":
    
    for line in sys.stdin:
        if line == "":
            break
        initialize(line.strip())

    while halted != True:
        
        instrunction = mem[program_counter]

        program_counter = exectute(instrunction)

        get_register_file()