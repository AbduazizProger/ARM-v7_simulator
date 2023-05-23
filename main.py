registers = [0] * 16
memory = [0] * 1024
isBig = False
i = 0

def add(destination, opr1, opr3):
    registers[destination] = registers[opr1] + registers[opr3]

def sub(destination, opr1, opr3):
    registers[destination] = registers[opr1] - registers[opr3]

def mul(destination, opr1, opr3):
    registers[destination] = registers[opr1] * registers[opr3]

def mov(destination, opr2):
    registers[destination] = opr2

def ldr(destination, opr2):
    registers[destination] = memory[opr2]

def str2(destination, opr2):
    memory[destination] = registers[opr2]

def cmp(opr1, opr2):
    isBig = registers[opr1] > registers[opr2]

def b(destination):
    i = findDestination(code, destination)

def beq(destination):
    if isBig:
        i = findDestination(code, destination)

def bne(destination):
    if not isBig:
        i = findDestination(code, destination)

def findDestination(content, search):
    lines = content
    for i in range(len(lines)):
        if lines[i] == search:
            return i

with open("assembly.txt") as file:
    code = file.read().splitlines()

while i < len(code):
    instruction = code[i].strip()
    instruction_set = instruction.split()
    command = instruction_set[0]
    operand1 = instruction_set[1] if len(instruction_set) > 1 else None

    if command == "b":
        b(operand1)
    elif command == "beq" and isBig:
        beq(operand1)
    elif command == "bne" and not isBig:
        bne(operand1)
    else:
        if command == "mov" and len(instruction_set) > 2:
            operand2 = int(instruction_set[2])
            mov(int(operand1[1]), operand2)
        elif command == "ldr" and len(instruction_set) > 2:
            operand2 = int(instruction_set[2][1:])
            ldr(int(operand1[1]), operand2)
        elif command == "str" and len(instruction_set) > 2:
            operand2 = int(instruction_set[2][1:])
            str2(int(operand1[1]), operand2)
        elif len(instruction_set) > 3:
            operand2 = int(instruction_set[2][1:])
            operand3 = int(instruction_set[3][1:])
            if command == "add":
                add(int(operand1[1]), operand2, operand3)
            elif command == "sub":
                sub(int(operand1[1]), operand2, operand3)
            elif command == "mul":
                mul(int(operand1[1]), operand2, operand3)
    i += 1

print(registers)
print(memory)
