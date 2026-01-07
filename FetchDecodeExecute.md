| **Table Of Contents** |
|:-:|
| [Todo](#todo) |
| [Structure](#structure) |
| [Fetch](#fetch) |
| [Decode](#decode) |
| [Execute](#execute) |
| [Connections](#connections) |
| [Cycle](#cycle) |

---
# *TODO*
- ~~8 ring counter~~
- ~~2x4 mux~~
- ~~2x4,8 demux~~
- ~~edit ALU (return all registers + enables)~~
- ~~fix comparator~~
- ~~16 ring counter~~

- ROM loading routine
- ~~SHT negative~~

- update -
---
---



# Structure
## Registers
| Register | Size | Name |
|:-:|:-:|:-:|
| [PC](#pc) | 8 | Program Counter |
| [CIR_Opcode](#cir) | 4 | Current Instruction Register |
| [CIR_Operand](#cir) | 8 | Current Instruction Register |
| [MAR](#mar) | 8 | Memory Address Register |
| [MDR](#mdr) | 8 | Memory Data Register |
| [ACC](#acc) | 8 | Accumulator |
| [FLAG](#flag) | 4 | G, E |
| [RAM_Opcode](#ram) | 32x4 | Random Access Memory |
| [RAM_Operand](#ram) | 32x8 | Random Access Memory |

## Operations
| Mnemonic | Opcode | Details |
|:-:|:-:|:-:|
| [NOP](#0-nop) | 0 | No Operation |
| [LDA](#1-lda) | 1 | Load RAM -> ACC |
| [LDI](#2-ldi) | 2 | Load Immediate -> ACC |
| [STA](#3-sta) | 3 | Store ACC -> RAM |
| [JMP](#4-jmp) | 4 | Jump Unconditionaly |
| [JEQ](#5-jeq) | 5 | Jump if E FLAG |
| [JGT](#6-jgt) | 6 | Jump if G FLAG |
| [CMP](#7-cmp) | 7 | Set FLAG |
| [ADD](#8-sta) | 8 | Add  ACC += RAM |
| [ADI](#9-adi) | 9 | Add ACC += Immediate |
| [SUB](#10-sub) | 10 | Add ACC -= RAM |
| [SBI](#11-sbi) | 11 | Add ACC -= Immediate |
| [SHF](#12-shf) | 12 | Shift ACC <<= RAM |
| [AND](#13-and) | 13 | And ACC &= RAM |
| [ORR](#14-orr) | 14 | Or ACC \|= RAM |
| [XOR](#15-xor) | 15 | Xor ACC ^= RAM |

### Unused
| Mnemonic | Opcode | Details |
|:-:|:-:|:-:|
| NOT | - | Not ACC = ~ACC |
| MUL | - | Multiply ACC *= RAM |
| INC | - | Increment ACC++ |
| DEC | - | Decrement ACC-- |
| JZR | - | Jump if Z FLAG |



# Fetch
```
MAR <- PC
CIR_Opcode <- RAM[MAR]_Opcode *
CIR_Operand <- RAM[MAR]_Operand *
PC <- PC + 1
```
# Decode
Opcode -> 4 bits

Operand -> 8 bits (Data, Address)

### Special
`0`-> NOP

`3`-> STA
```
MAR <- CIR_Operand
```

`4,5,6`-> jumps
```
MDR <- CIR_Operand
```

### ACC/FLAGS <- x
`1,7,8,10,12,13,14,15` (fetch address)
```
MAR <- CIR_Operand
MDR <- RAM[MAR]_Operand
```

`2,9,11` (Immediate)
```
MDR <- CIR_Operand
```



# Execute
### 0-NOP
```
```

### 1-LDA
```
MAR <- CIR_Operand
MDR <- RAM[MAR]_Operand
ACC <- MDR
```

### 2-LDI
```
MDR <- CIR_Operand
ACC <- MDR
```

### 3-STA
```
MAR <- CIR_Operand
RAM[MAR]_Operand <- ACC
```

### 4-JMP
```
MDR <- CIR_Operand
PC <- MDR
```

### 5-JEQ
```
MDR <- CIR_Operand
if E:
    PC <- MDR
```

### 6-JGT
```
MDR <- CIR_Operand
if G:
    PC <- MDR
```

### 7-CMP
```
MAR <- CIR_Operand
MDR <- RAM[MAR]_Operand
FLAG <- compare(ACC, MDR)
```

### 8-ADD
```
MAR <- CIR_Operand
MDR <- RAM[MAR]_Operand
ACC <- ACC + MDR
```

### 9-ADI
```
MDR <- CIR_Operand
ACC <- ACC + MDR
```

### 10-SUB
```
MAR <- CIR_Operand
MDR <- RAM[MAR]_Operand
ACC <- ACC - MDR
```

### 11-SBI
```
MDR <- CIR_Operand
ACC <- ACC - MDR
```

### 12-SHF
```
MAR <- CIR_Operand
MDR <- RAM[MAR]_Operand
ACC <- ACC << MDR
```

### 13-AND
```
MAR <- CIR_Operand
MDR <- RAM[MAR]_Operand
ACC <- ACC & MDR
```

### 14-ORR
```
MAR <- CIR_Operand
MDR <- RAM[MAR]_Operand
ACC <- ACC | MDR
```

### 15-XOR
```
MAR <- CIR_Operand
MDR <- RAM[MAR]_Operand
ACC <- ACC ^ MDR
```



# Connections
### PC
```
ALU 1-> | PC | *-> MAR

1. jumps - DECODE
```

### CIR
```
RAM 1-> | CIR_Operand | /2-> MAR
        |             | \3-> MDR

1. FETCH
2. fetch address - DECODE
3. immediate - DECODE
```

### MAR
```
          PC 1->\ | MAR | *-> RAM[]
CIR_Operand  2->/ |     |

1. FETCH
2. fetch address - DECODE
```

### MDR
```
CIR_Operand 1->\ | MDR | 
        RAM 2->| |     | 4-> ALU
        ACC 3->/ |     | 

1. 1,7,8,10,12,13,14,15 - EXECUTE
2. 2,4,5,6,9,11 - EXECUTE
3. 3 - EXECUTE
4. * - EXECUTE
```

### ACC
```
ALU 1-> | ACC | 2-> MDR

1. * - EXECUTE
2. 3 - EXECUTE
```

### FLAG
```
ALU 1*-> | FLAG | 2*->ALU

1. 7 - EXECUTE
2. 4,5,6 - EXECUTE
```

### RAM
```
ALU 1-> | RAM | /2-> CIR
MAR *-> |     | \3-> MDR

1. 3 - EXECUTE
2. FETCH
3. fetch address - DECODE
```


# Cycle
```
10 tick cycle:
4 - FETCH:
    store MAR<-PC, PC-CIR
    pulse MAR, pulse PC
    store CIR<-RAM, !CIR/MDR
    pulse CIR
4/2 - DECODE:
    1,7,8,10,12,13,14,15:
        store MAR<-CIR, !PC-CIR
        pulse MAR
        store MDR<-RAM, CIR/MDR, CIR-RAM, !(CIR-RAM)-ACC
        pulse MDR
    2,4,5,6,9,11:
        store MDR<-CIR, !CIR-RAM, !(CIR-RAM)-ACC
        pulse MDR
    3:
        store MAR<-CIR, !PC-CIR
        pulse MAR
2 - EXECUTE:
    store x<-ALU
    pulse x
```