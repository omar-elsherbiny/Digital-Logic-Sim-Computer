operations = []
while 1:
    opcode = int(input("opcode: "))
    if opcode == -1:
        break
    operand = int(input("operand: "))
    operations.append(str(opcode * 256 + operand))

print("\n".join(operations))
