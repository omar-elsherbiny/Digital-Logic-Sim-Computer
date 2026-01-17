# Digital Logic Sim Computer

> 8-bit processor implemented in a **Digital Logic Simulator**.  
> Full documentation: [Documentation.pdf](./Documentation.pdf)

---

## Demo

<p align="center">
  <img src="./assets/FibDemo.gif" alt="Demo">
</p>

*Program to calculate Fibonacci of 7 shown in GIF:*
<small>

<pre>
00: LDI 1     (513)
01: STA 244   (1012)
02: LDI 1     (513)
03: STA 245   (1013)
04: LDI 2     (514)
05: STA 247   (1015)
06: LDA 244   (500)
07: ADD 245   (2293)
08: STA 246   (1014)
09: LDA 245   (501)
10: STA 244   (1012)
11: LDA 246   (502)
12: STA 245   (1013)
13: LDA 247   (503)
14: ADI 1     (2305)
15: NOP 6     (6)
16: CMP 15    (1807)
17: STA 247   (1015)
18: JGT 20    (1556)
19: JMP 6     (1030)
20: LDA 245   (501)
</pre>
</small>

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
Helper script to convert from the Assembly-like language to the decimal ROM codes
*Example Program:*
```
LDA 200
ADI 1  
STA 200
```
*Example Output program.txt*
```
456
2305
968
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