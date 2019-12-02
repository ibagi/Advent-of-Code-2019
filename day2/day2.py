import fileinput
import itertools
from operator import mul, add


def terminate(operandA, operandB):
    pass


def parse_program():
    return [int(x) for x in fileinput.input().readline().split(",")]


def intcode_program(program, opcodes, instruction_offset=4):
    ip = 0
    running = True
    while running:
        (opcode, indexA, indexB, target) = program[ip:ip + instruction_offset]
        operandA = program[indexA]
        operandB = program[indexB]

        (operator, running) = opcodes[opcode]
        program[target] = operator(operandA, operandB)
        ip += instruction_offset

    return program[0]


operators = {
    1: (add, True),
    2: (mul, True),
    99: (terminate, False)
}

program = parse_program()
solution = intcode_program(program, operators)

print(solution)
