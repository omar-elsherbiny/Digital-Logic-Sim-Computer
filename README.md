# Digital Logic Sim Computer

> 8-bit processor implemented in a **Digital Logic Simulator**.  
> Full documentation: [Documentation.pdf](./Documentation.pdf)

---

## Demo

<p align="center">
  ![Demo](./assets/demo.gif)
</p>

*Program shown in GIF:*

```txt
LOAD A, 0x05
ADD A, 0x03
STORE A, 0x10
HALT
```

## Operations
| Mnemonic | Opcode | Details |
|:-:|:-:|:-:|
| NOP | 0 | No Operation |
| LDA | 1 | Load RAM -> ACC |
| LDI | 2 | Load Immediate -> ACC |
| STA | 3 | Store ACC -> RAM |
| JMP | 4 | Jump Unconditionaly |
| JEQ | 5 | Jump if E FLAG |
| JGT | 6 | Jump if G FLAG |
| CMP | 7 | Set FLAG |
| ADD | 8 | Add  ACC += RAM |
| ADI | 9 | Add ACC += Immediate |
| SUB | 10 | Add ACC -= RAM |
| SBI | 11 | Add ACC -= Immediate |
| SHF | 12 | Shift ACC <<= RAM |
| AND | 13 | And ACC &= RAM |
| ORR | 14 | Or ACC \|= RAM |
| XOR | 15 | Xor ACC ^= RAM |

## Python Helper
Helper script to convert from the Assembly-like language to the decimal ROM program
*Example Program:*
```
```
*Example Output program.txt*
```
```

## Files
```
Chips/               # Logic chips
Documentation.pdf    # CPU design & instructions
Operation2Decimal.py # Python helper script
program.txt          # Example program
```

## Credits
Inspired by [Sebastian Lague’s Digital Logic Sim](https://www.youtube.com/playlist?list=PLFt_AvWsXl0dPhqVsKt1Ni_46ARyiCGSq)