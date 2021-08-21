import sys

MEM = {}
program_counter = 0
REG_FILE = []

TYPE_A = ["00000", "00001", "00110", "01010", "01011", "01100"]
TYPE_B = ["00000", "01000", "01001"]
TYPE_C = ["00111", "01101", "01110"]
TYPE_D = ["001000", "00101"]
TYPE_E = ["01111", "10000", "10001", "10010"]
TYPE_F = ["10011"]


#helper functions
def get_binary(value, width):
    res = bin(value)
    return res[2:].zfill(width)

def decode_instruction(single_line):
    opcode = single_line[:5]
    reg = []

    if opcode in TYPE_A:
        reg.append(single_line[7:10])
        reg.append(single_line[10:13])
        reg.append(single_line[13:16])
        MEM[opcode] = reg

    elif opcode in TYPE_B:
        reg.append(single_line[7:10])
        reg.append(single_line[10:])
        MEM[opcode] = reg

    

#operations
def sub(input):
    pass

def add(input):
    pass

def div(input):
    pass

def mul(input):
    pass


def ld (input):
    pass

def st(input):
    pass


if __name__ == "__main__":
    print("")

    tmp = open ("/home/iiitd/Documents/assignment/CO_assignment/SimpleSimulator/test", "r")

    for line in tmp.readlines():
        print(decode_instruction(line))
    
    print(MEM)