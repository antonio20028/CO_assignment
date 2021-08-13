
import sys

regs = ["R0", "R1", "R2", "R3", "R4", "R5", "R6"]

instructions = ["add", "sub", "div",
                "mul", "st", "ld", "mov", "rs", "ls", "xor", "or", "and", "not", "cmp", "jmp", "jlt"]
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

def isValid_register(arg):
    if arg in regs or arg in range(0, 255):
        return True
    
def isValid_instruction(instruction):
    if instruction in instructions:
        return True

def switch_case(instruction, args):
   if instruction == "add":
        if len(args) == 3:
            return True
   elif instruction == "sub":
        if len(args) == 3:
            return True
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
                            errors.append(f" {arg} is not a valid register")
                          
                else:
                    errors.append(f"this instruction requires 3 arguments, but {len(args)} was given")
                
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
