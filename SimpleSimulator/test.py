reg_file = {
    "000": 0,
    "001": 0,
    "010": 2,
    "011": 5,
    "100": 0,
    "101": 0,
    "110": 0,
    "111": 0}

instruction = {"00000": ["000", "010", "011"]}

tmp  = list(instruction.keys())
opcode = tmp[0]
res =  reg_file[instruction.get(opcode)[1]] + reg_file[instruction.get(opcode)[2]]
reg_file[instruction.get(opcode)[0]] = res
print(res)
print(reg_file)