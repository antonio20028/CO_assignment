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
TYPE_C = ["00111", "01101", "01110", "00011"]
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

    tmp  = list(instruction.keys())
    opcode = tmp[0]
    flag = reg_file["111"]

    reg_address = instruction.get(opcode)[0]

    if opcode in TYPE_A:
        if opcode == TYPE_A[0]:
            res =  instruction.get(opcode)[1] + instruction.get(opcode)[2]
            if res < 65535:
                reg_file[reg_address] = res
                reg_file[flag] = 0
            else:
                reg_file[flag] = 8
        elif opcode == TYPE_A[1]:
            res = instruction.get(opcode)[1] - instruction.get(opcode)[2]
            if res > 0:
                reg_file[reg_address] = res
                reg_file[flag] = 0
            else:
                reg_file[flag] = 8
        elif opcode == TYPE_A[2]:
                res = instruction.get(opcode)[1] * instruction.get(opcode)[2]
                if res < 65535:
                    reg_file[reg_address] = res
                    reg_file[flag] = 0
                else:
                    reg_file[flag] = 8

        elif opcode == TYPE_A[3]:
            reg_file[reg_address] = instruction.get(opcode)[1] ^ instruction.get(opcode)[2]
        elif opcode == TYPE_A[3]:
            reg_file[reg_address] = instruction.get(opcode)[1] | instruction.get(opcode)[2]
        elif opcode == TYPE_A[4]:
            reg_file[reg_address] = instruction.get(opcode)[1] & instruction.get(opcode)[2]
    elif opcode in TYPE_B:
        if opcode == TYPE_B[0]:
            reg_file[reg_address] = instruction.get(opcode)[1]
        elif opcode == TYPE_B[1]:
            reg_file[reg_address] = reg_file[reg_address] >> instruction.get(opcode)[1]
        elif opcode == TYPE_B[2]:
            reg_file[reg_address] = reg_file[reg_address] << instruction.get(opcode)[1]
    elif opcode in TYPE_C:
        if opcode == TYPE_C[0]:
            if instruction.get(opcode)[1] > 0:
                reg_file["000"] = reg_address / instruction.get(opcode)[1]
                reg_file["001"] = reg_address % instruction.get(opcode)[1]
        elif opcode == TYPE_C[3]:
            reg_file[reg_address] = instruction.get(opcode)[1]
        elif opcode == TYPE_C[1]:
            reg_file[reg_address] = ~(instruction.get(opcode)[1])
        elif opcode == TYPE_C[2]:
            if instruction.get(opcode)[0] < instruction.get(opcode)[1]:
                reg_file[flag] = 4
            elif instruction.get(opcode)[0] > instruction.get(opcode)[1]:
                reg_file[flag] = 2
            else:
                reg_file[flag] = 1
    elif opcode in TYPE_D:
        if opcode == TYPE_D[0]:
            reg_file[reg_address] = reg_file[instruction.get(opcode)[1]]
        elif opcode == TYPE_D[1]:
            reg_file[instruction.get(opcode)[1]] = reg_file[reg_address]
    else:
        halted = True


def update_program_counter(new_pc):
    program_counter = new_pc


def get_register_file():
    for line in reg_file.keys():
        print(reg_file[line])

if __name__ == "__main__":
    
    for line in sys.stdin:
        if line == "":
            break
        initialize(line.strip())

    
    for i in range(len(mem)):
        program_counter = i
        exectute(mem[program_counter])

    sys.stdout.write(program_counter)
    sys.stdout.write(reg_file)
    # while halted != True:
        
    #     instrunction = mem[program_counter]

    #     new_pc = exectute(instrunction)

        
    #     update_program_counter(new_pc)
    #     print(program_counter)
    #     # get_register_file()