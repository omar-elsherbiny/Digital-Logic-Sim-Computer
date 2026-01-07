operations=[]
opcode=0
while opcode!=-1:
    opcode,operand=int(input('opcode: ')), int(input('operand: '))
    operations.append(opcode*256+operand)

print('\n'.join(list(map(str,operations))))