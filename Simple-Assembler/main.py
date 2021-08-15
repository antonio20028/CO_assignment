import sys

regs = ["R0", "R1", "R2", "R3", "R4", "R5", "R6"]
mem_addrs = ["[R0]", "[R1]", "[R2]", "[R3]", "[R4]", "[R5]", "[R6]"]
tmp = ["var"]
errors = []
instructions = [
    {
        "type": "A",
        "instructions": ["add", "sub", "mul", "xor", "or", "and"],
       }, 
    
       {
        "type": "B",
        "instructions": ["mov", "rs", "ls"]},
       {
        "type": "C",
        "instructions": ["div", "not", "cmp"]},
       {
        "type": "D",
        "instructions": ["ld", "st"]},
       {
        "type": "E",
        "instructions": ["jmp", "jlt", "jgt", "je"]},
       {
        "type": "F",
        "instructions": ["hlt"]
     }
    ]
immediates = ["$%s"%i for i in range(0, 255)]

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

def registerError(reg):
    errors.append("%s is not a valid register "%reg)
    
def mem_addrError(reg):
    errors.append("%s is not a valid mem_addr "%reg)
    
def argumentsError(args):
    errors.append("%s is not a valid register "%args)

def immediateError(imm):
    errors.append("%s is not a valid immediate"%imm)

    
def isTypeA(instruction, args):
    if instruction in instructions[0]["instructions"]:
        if len(args) == 3:
            for i in range(len(args)):
                if isValid_register(args[i].strip()):
                    return True
                else:
                    registerError(args[i])  
        else:
            errors.append("A type A instruction receives 3 arguments, but %s was given"%len(args))
                    
def isTypeB(instruction, args):
    if instruction in instructions[1]["instructions"]:
        if len(args) == 2:
            if isValid_register(args[0].strip()):
                if isValid_immediate(args[1].strip()):
                    return True
                else:
                    immediateError(args[1])
            else:
                registerError(args[0])
        else:
            errors.append("A type B instruction receives 2 arguments, but %s was given"%len(args))
            
def isTypeC(instruction, args):
    if instruction in instructions[2]["instructions"]:
        if len(args) == 2:
            if isValid_register(args[0].strip()):
                if isValid_register(args[1].strip()):
                    return True
                else:
                    registerError(args[1])
            else:
                registerError(args[0])
        else:
            errors.append("A type C instruction receives 2 arguments, but %s was given "%len(args))
            
def isTypeD(instruction, args):
    if instruction in instructions[3]["instructions"]:
        if len(args) == 2:
            if isValid_register(args[0].strip()):
                if isValid_mem_addr(args[1].strip()):
                    return True
                else:
                    mem_addrError(args[1])
            else:
                registerError(args[0])      
        else:
            errors.append("A type D instruction receives 2 arguments but %s was given"%len(args))
            
def isTypeE(instruction, args):
    if instruction in instructions[4]["instructions"]:
        if len(args) == 1:
            if isValid_mem_addr(args[0].strip()):
                return True
            else:
                mem_addrError(args[0])
        else:
            errors.append("A type E just receives 1 arguments, but %s was given"%len(args))
            
def isTypeF(instruction, args):
    if instruction in instructions[5]["instructions"]:
        if len(args) == 0:
            return True
        
def isValid_register(arg):
    if arg in regs:
        return True
    
def isValid_mem_addr(mem_addr):
    if mem_addr in mem_addrs:
        return True
    
def isValid_immediate(imm):
    if imm in immediates:
        return True

   
    
def isValid_instruction(instruction):
    if instruction.strip() in tmp:
        return True

def fetch_instructions(line):
    assembly_code = []
    assembly_code.append(line)
    
    return assembly_code
                
def all_instruction():
    for i in range(len(instructions)):
        tmp.extend(instructions[i]["instructions"])
        
def switch_case(instruction, args):
   if instruction == "add":
        return isTypeA(instruction, args)
    
   elif instruction == "sub":
        return isTypeA(instruction, args)
        
   elif instruction == "div":
       return isTypeC(instruction, args)
    
   elif instruction == "mul":
      return isTypeC(instruction, args)

    
   elif instruction == "st":
       return isTypeD(instruction, args)
    
   elif instruction == "ld":
       return isTypeD(instruction, args)
    
   elif instruction == "mov":
       return isTypeB(instruction, args)
    
   elif instruction == "mov":
        return isTypeC(instruction, args)
    
   elif instruction == "rs":
       return isTypeB(instruction, args)
    
   elif instruction == "ls":
       return isTypeB(instruction, args)
    
   elif instruction == "xor":
       return isTypeA(instruction, args)
    
   elif instruction == "or":
       return isTypeA(instruction, args)
    
   elif instruction == "and":
       return isTypeA(instruction, args)
    
   elif instruction == "not":
       return isTypeC(instruction, args)
    
   elif instruction == "cmp":
        return isTypeC(instruction, args)
    
   elif instruction == "jmp":
       return isTypeE(instruction, args)
    
   elif instruction == "jlt":
        return isTypeE(instruction, args)
    
   elif instruction == "jgt":
       return isTypeE(instruction, args)
    
   elif instruction == "je":
       return isTypeE(instruction, args)
     
def halt(): 
    sys.exit()

if __name__ == "__main__":
    args = []
    instruction = ""
    flag  = False
    assembly = []
    
    all_instruction()
    for instruct in sys.stdin:
        instruction = instruct.strip().split(" ")[0]
        args = instruct.strip().split(" ")[1:]
        
        #in code errors
        if instruction.strip() != "hlt":
            if isValid_instruction(instruction.strip()):
                switch_case(instruction.strip(), args)
                assembly = fetch_instructions(instruction)
            else:
                errors.append("%s is not a valid instruction"%instruction)
             
            #assembly file error 
            if len(errors) == 0 and flag:
               if assembly[0].split(" ").strip("")[0] == "var":
                   if assembly[-1].strip() == "hlt":
                       print("debugged")
                   else:
                       errors.append("hlt instruction not found")
               else:
                    errors.append("var not found")
            else:
                for err in errors:
                    print(err)
                    halt()
        else:
           halt()