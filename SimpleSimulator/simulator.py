import sys
import operations
import matplotlib.pyplot as plt

mem = []
instructions = []
program_counter = 0
halted = False
vl = 0

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

def get_decimal(value):
    return int(value, 2)

def initialize(single_line):
    opcode = single_line[:5]
    reg = []
    lmop = {}
    global vl

    if opcode in TYPE_A:
        reg.append(single_line[7:10])
        reg.append(single_line[10:13])
        reg.append(single_line[13:16])
        lmop[opcode] = reg
        instructions.append(lmop)
        mem.append(single_line)

    elif opcode in TYPE_B:
        reg.append(single_line[5:8])
        reg.append(single_line[8:])
        lmop[opcode] = reg
        instructions.append(lmop)
        mem.append(single_line)
    
    elif opcode in TYPE_C:
        reg.append(single_line[10:13])
        reg.append(single_line[13:16])
        lmop[opcode] = reg
        instructions.append(lmop)
        mem.append(single_line)

    elif opcode in TYPE_D:
        reg.append(single_line[5:8])
        reg.append(single_line[8:])
        vl = get_decimal(single_line[8:])
        lmop[opcode] = reg
        instructions.append(lmop)
        mem.append(single_line)

    elif opcode in TYPE_E:
        reg.append(single_line[8:])
        lmop[opcode] = reg
        instructions.append(lmop)
        mem.append(single_line)
    
    elif opcode in TYPE_F:
        lmop[opcode] = single_line[5:]
        instructions.append(lmop)
        mem.append(single_line)

def exectute(instruction, program_counter):

    tmp  = list(instruction.keys())
    opcode = tmp[0]
    flag = reg_file["111"]
    global halted
    reg_address = instruction.get(opcode)[0]
    
    if opcode in TYPE_A:
        if opcode == TYPE_A[0]: # addition
            res =  reg_file[instruction.get(opcode)[1]] + reg_file[instruction.get(opcode)[2]]
            if res < 65535:
                reg_file[reg_address] = res
                reg_file[flag] = 0
            else:
                reg_file[flag] = 8

        elif opcode == TYPE_A[1]: # subtraction
            res = reg_file[instruction.get(opcode)[1]] - reg_file[instruction.get(opcode)[2]]
            if res > 0:
                reg_file[reg_address] = res
                reg_file[flag] = 0
            else:
                reg_file[reg_address] = 0
                reg_file[flag] = 8

        elif opcode == TYPE_A[2]: # multiply
                res = reg_file[instruction(opcode)[1]] * reg_file[instruction.get(opcode)[2]]
                if res < 65535:
                    reg_file[reg_address] = res
                    reg_file[flag] = 0
                else:
                    reg_file[flag] = 8

        elif opcode == TYPE_A[3]: # exclusive or
            reg_file[flag] = 0
            x = get_binary(reg_file[instruction.get(opcode)[1]], 16) 
            y = get_binary(reg_file[instruction.get(opcode)[2]], 16)
            z = ''
            for i in range(16):
                l = str(int(x[i]) ^ int(y[i]))
                z += l
            reg_file[reg_address] = get_decimal(z) 

        elif opcode == TYPE_A[4]: # or
            reg_file[flag] = 0
            x = get_binary(reg_file[instruction.get(opcode)[1]], 16) 
            y = get_binary(reg_file[instruction.get(opcode)[2]], 16)
            z = ''
            for i in range(16):
                l = str(int(x[i]) | int(y[i]))
                z += l
            reg_file[reg_address] = get_decimal(z) 

        elif opcode == TYPE_A[5]: # and
            reg_file[flag] = 0
            x = get_binary(reg_file[instruction.get(opcode)[1]], 16) 
            y = get_binary(reg_file[instruction.get(opcode)[2]], 16)
            z = ''
            for i in range(16):
                l = str(int(x[i]) & int(y[i]))
                z += l
            reg_file[reg_address] = get_decimal(z)

    elif opcode in TYPE_B:
        if opcode == TYPE_B[0]: # move immediate
            reg_file[flag] = 0
            reg_file[reg_address] = get_decimal(instruction.get(opcode)[1])

        elif opcode == TYPE_B[1]: # right shift
            reg_file[flag] = 0
            reg_file[reg_address] = reg_file[reg_address] >> get_decimal(instruction.get(opcode)[1])

        elif opcode == TYPE_B[2]: # left shift
            reg_file[flag] = 0
            reg_file[reg_address] = reg_file[reg_address] << get_decimal(instruction.get(opcode)[1])

    elif opcode in TYPE_C:
        if opcode == TYPE_C[0]: # divide
            reg_file[flag] = 0
            if reg_file[instruction.get(opcode)[1]] > 0:
                reg_file["000"] = reg_file[instruction.get(opcode)[0]] / reg_file[instruction.get(opcode)[1]]
                reg_file["001"] = reg_file[instruction.get(opcode)[0]] % reg_file[instruction.get(opcode)[1]]

        elif opcode == TYPE_C[3]: # move register
            reg_file[flag] = 0
            reg_file[reg_address] = reg_file[instruction.get(opcode)[1]]

        elif opcode == TYPE_C[1]: # invert
            reg_file[flag] = 0
            reg_file[reg_address] = ~(reg_file[instruction.get(opcode)[1]])
            print(reg_file[reg_address])

        elif opcode == TYPE_C[2]: # compare
            if reg_file[instruction.get(opcode)[0]] < reg_file[instruction.get(opcode)[1]]:
                reg_file[flag] = 4
            elif reg_file[instruction.get(opcode)[0]] > reg_file[instruction.get(opcode)[1]]:
                reg_file[flag] = 2
            else:
                reg_file[flag] = 1

    elif opcode in TYPE_D:
        if opcode == TYPE_D[0]: # load
            reg_file[flag] = 0
            reg_file[reg_address] = get_decimal(mem[get_decimal(instruction.get(opcode)[1])])

        elif opcode == TYPE_D[1]: # store
            reg_file[flag] = 0
            mem[get_decimal(instruction.get(opcode)[1])] = get_binary(reg_file[reg_address], 16)

    elif opcode in TYPE_E:
        if opcode == TYPE_E[0]: # unconditional jump
            PC = get_binary(program_counter, 8)
            R0 = get_binary(reg_file["000"], 16)
            R1 = get_binary(reg_file["001"], 16)
            R2 = get_binary(reg_file["010"], 16)
            R3 = get_binary(reg_file["011"], 16)
            R4 = get_binary(reg_file["100"], 16)
            R5 = get_binary(reg_file["101"], 16)
            R6 = get_binary(reg_file["110"], 16)
            Flag = get_binary(reg_file["111"], 16)
            l = [PC, R0, R1, R2, R3, R4, R5, R6, Flag]
            print(" ".join(l))
            return(get_decimal(reg_file[reg_address]))

        elif opcode == TYPE_E[1]: # jump if less than
            if reg_file[flag] == 4:
                reg_file[flag] = 0
                PC = get_binary(program_counter, 8)
                R0 = get_binary(reg_file["000"], 16)
                R1 = get_binary(reg_file["001"], 16)
                R2 = get_binary(reg_file["010"], 16)
                R3 = get_binary(reg_file["011"], 16)
                R4 = get_binary(reg_file["100"], 16)
                R5 = get_binary(reg_file["101"], 16)
                R6 = get_binary(reg_file["110"], 16)
                Flag = get_binary(reg_file["111"], 16)
                l = [PC, R0, R1, R2, R3, R4, R5, R6, Flag]
                print(" ".join(l))
                return(get_decimal(reg_file[reg_address]))

        elif opcode == TYPE_E[2]: # jump if greater than
            if reg_file[flag] == 2:
                reg_file[flag] = 0
                PC = get_binary(program_counter, 8)
                R0 = get_binary(reg_file["000"], 16)
                R1 = get_binary(reg_file["001"], 16)
                R2 = get_binary(reg_file["010"], 16)
                R3 = get_binary(reg_file["011"], 16)
                R4 = get_binary(reg_file["100"], 16)
                R5 = get_binary(reg_file["101"], 16)
                R6 = get_binary(reg_file["110"], 16)
                Flag = get_binary(reg_file["111"], 16)
                l = [PC, R0, R1, R2, R3, R4, R5, R6, Flag]
                print(" ".join(l))
                return(get_decimal(reg_file[reg_address]))

        elif opcode == TYPE_E[3]: # jump if equal
            if reg_file[flag] == 1:
                reg_file[flag] = 0
                PC = get_binary(program_counter, 8)
                R0 = get_binary(reg_file["000"], 16)
                R1 = get_binary(reg_file["001"], 16)
                R2 = get_binary(reg_file["010"], 16)
                R3 = get_binary(reg_file["011"], 16)
                R4 = get_binary(reg_file["100"], 16)
                R5 = get_binary(reg_file["101"], 16)
                R6 = get_binary(reg_file["110"], 16)
                Flag = get_binary(reg_file["111"], 16)
                l = [PC, R0, R1, R2, R3, R4, R5, R6, Flag]
                print(" ".join(l))
                return(get_decimal(reg_file[reg_address]))

    elif opcode in TYPE_F:
        reg_file[flag] = 0
        halted = True

    PC = get_binary(program_counter, 8)
    R0 = get_binary(reg_file["000"], 16)
    R1 = get_binary(reg_file["001"], 16)
    R2 = get_binary(reg_file["010"], 16)
    R3 = get_binary(reg_file["011"], 16)
    R4 = get_binary(reg_file["100"], 16)
    R5 = get_binary(reg_file["101"], 16)
    R6 = get_binary(reg_file["110"], 16)
    Flag = get_binary(reg_file["111"], 16)
    l = [PC, R0, R1, R2, R3, R4, R5, R6, Flag]
    print(" ".join(l))


if __name__ == "__main__":
    
    x = 0
    lst_1 = []
    lst_2 = []
    vl = 56

    for line in sys.stdin:
        if line == "":
            break
        initialize(line.strip())
        x += 1

    y = 256 - x
    lm = '0000000000000000'
    for i in range(y):
        mem.append(lm)
    
    var = 0
    program_counter = 0
    while True:
        lst_1.append(var)
        lst_2.append(program_counter)
        if vl != 56:
            lst_1.append(var)
            lst_2.append(vl)
        opcode = mem[program_counter][:5]
        if opcode in TYPE_E:
            program_counter = exectute(instructions[program_counter], program_counter)
            continue
        if halted == True:
            for i in range(len(mem)):
                print(mem[i])
            break
        exectute(instructions[program_counter], program_counter)
        program_counter += 1
        var += 1

    plt.scatter(lst_1, lst_2)
    plt.show()

