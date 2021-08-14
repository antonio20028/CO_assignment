import sys

regs = ["R0", "R1", "R2", "R3", "R4", "R5", "R6"]
mem_addrs = ["[R0]", "[R1]", "[R3]", "[R3]", "[R4]", "[R5]", "[R6]"]

type_A = ["add", "sub", "mul", "xor", "or", "and"]
type_B = ["mov", "rs", "ls"]
type_C = ["div", "not", "cmp"]
type_D = ["ld", "st"]
type_E = ["jmp", "jlt", "jgt", "je"]

errors = []
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
    errors.append("%s is not a valid register "%args[i])

def immediateError(imm):
    errors.append("%s is not a valid immediate"%imm)

    
def isTypeA(instruction, args):
    if instruction in type_A:
        if len(args) == 3:
            for i in range(len(args)):
                if isValid_register(args[i].strip()):
                    return True
                else:
                    registerError(args[i])  
        else:
            errors.append("An type A instruction receives 3 arguments, but %s was given"%len(args))
                    
def isTypeB(instruction, args):
    if instruction in type_B:
        if len(args) == 2:
            if isValid_register(args[0]):
                if isValid_immediate(args[1].strip()):
                    return True
                else:
                    immediateError(args[1])
            else:
                registerError(args[0])
        else:
            errors.append("An type B instruction receives 2 arguments, but %s was given"%len(args))
            
def isTypeC(instruction, args):
    if instruction in type_C:
        if len(args) == 2:
            for i in range(len(args)):
                if isValid_register(args[i]):
                    return True
                else:
                    registerError(args[i])
        else:
            errors.append("An type C instruction receives 2 arguments, but %s was given "%len(args))
            
def isTypeD(instruction, args):
    if instruction in type_D:
        if len(args) == 2:
            if isValid_register(args[0]):
                if isValid_mem_addr(args[1].strip()):
                    return True
                else:
                    mem_addrError(args[1])
            else:
                registerError(args[0])      
        else:
            errors.append("An type D instruction receives 2 arguments but %s was given"%len(args))
            
def isTypeE(instruction, args):
    if instruction in type_E:
        if len(args) == 1:
            if isValid_mem_addr(args[0].strip()):
                return True
            else:
                mem_addrError(args[0])
        else:
            errors.append("An type E just receives 1 arguments, but %s was given"%len(args))
            
def isValid_register(arg):
    if arg in regs:
        return True
    
def isValid_mem_addr(mem_addr):
    if mem_addr in mem_addrs:
        return True
    
def isValid_instruction(instruction):
    if instruction in type_A or  type_B or type_C or type_D or type_E:
        return True
    
def isValid_immediate(imm):
    if imm in immediates:
        return True

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
       return isTpeA(instruction, args)
    
   elif instruction == "or":
       return isTypeA(instruction, args)
    
   elif instruction == "and":
       return isTypeA(instruction, args)
    
   elif instruction == "not":
       return isStypeC(instruction, args)
    
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
    
    for instruct in sys.stdin:
        instruction = instruct.split(" ")[0]
        args = instruct.split(" ")[1:]

        if instruction.strip() != "hlt":
            if isValid_instruction(instruction.strip()):
                switch_case(instruction.strip(), args)
            else:
                errors.append(instruction, " is not a valid instruction")
                
            if len(errors) == 0 and flag:
                pass
            else:
                for err in errors:
                    print(err)
                    halt()
        else:
           halt()
