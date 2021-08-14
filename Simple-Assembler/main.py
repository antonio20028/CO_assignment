import sys

regs = ["R0", "R1", "R2", "R3", "R4", "R5", "R6"]


type_A = ["add", "sub", "mul", "xor", "or", "and"]
type_B = ["mov", "rs", "ls"]
type_C = ["div", "not", "cmp"]
type_D = ["ld", "st"]
type_E = ["jmp", "jlt", "jgt", "je"]

errors = []

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


def isTypeA(instruction, args):
    if instruction in type_A:
        if len(args) == 3:
            for i in range(len(args)):
                if isValid_register(args[i]):
                    return True
                
                    
def isTypeB(instruction, args):
    if instruction in type_B:
        if len(args) == 2:
            if isValid_register(args[0]) and args[1] in range(0, 255):
                return True


def isValid_register(arg):
    if arg in regs:
        return True
    
def isValid_instruction(instruction):
    if instruction in type_A or  type_B or type_C or type_D or type_E:
        return True
    

def switch_case(instruction, args):
   if instruction == "add":
        return isTypeA(instruction, args)
    
   elif instruction == "sub":
        return isTypeA(instruction, args)
        
   elif instruction == "div":
       if len(args) == 2:
           return True
   elif instruction == "mul":
       if len(args) == 3:
           return True
   elif instruction == "st":
       if len(args) == 2:
           return True
   elif instruction == "ld":
       if len(args) == 2:
           return True
   elif instruction == "mov":
       if len(args) == 2:
           return True

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
                if switch_case(instruction.strip(), args):
                    for arg in args:
                        if isValid_register(arg.rstrip("\n").strip()):
                            flag = True
                        else:
                            errors.append("The %s is not a valid register"%arg)
                          
                else:
                    errors.append("this instruction requires 3 arguments, but %s was given"%len(args))
                
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
