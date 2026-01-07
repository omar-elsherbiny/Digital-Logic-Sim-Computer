import os

OUT_FILE = "program.txt"

OPS = {
    0: "NOP",
    1: "LDA",
    2: "LDI",
    3: "STA",
    4: "JMP",
    5: "JEQ",
    6: "JGT",
    7: "CMP",
    8: "ADD",
    9: "ADI",
    10: "SUB",
    11: "SBI",
    12: "SHF",
    13: "AND",
    14: "ORR",
    15: "XOR",
}


def clear() -> None:
    os.system("cls" if os.name == "nt" else "clear")


def load_program() -> list[int]:
    if not os.path.exists(OUT_FILE):
        return []
    with open(OUT_FILE, "r") as f:
        return [int(line.strip()) for line in f if line.strip()]


def save_instruction(value) -> None:
    with open(OUT_FILE, "a") as f:
        f.write(f"{value}\n")


def decode(value) -> tuple[int, int]:
    opcode = (value >> 8) & 0xF
    operand = value & 0xFF
    return opcode, operand


while True:
    clear()
    program = load_program()

    print("=== CURRENT PROGRAM ===")
    if not program:
        print("(empty)")
    else:
        for addr, instr in enumerate(program):
            op, opd = decode(instr)
            print(f"{addr:02}: {OPS.get(op, '???')} {opd}   ({instr})")

    print("\n=== ADD INSTRUCTION ===")
    for k in sorted(OPS):
        print(f"{k:>2}: {OPS[k]}")
    print(" x: exit")

    choice = input("\nopcode> ").strip()
    if choice.lower() == "x":
        break

    try:
        opcode = int(choice)
        if opcode not in OPS:
            raise ValueError
    except ValueError:
        input("Invalid opcode. Press Enter...")
        continue

    try:
        operand = int(input("operand (0–255)> "))
        if not (0 <= operand <= 255):
            raise ValueError
    except ValueError:
        input("Invalid operand. Press Enter...")
        continue

    encoded = (opcode << 8) | operand
    save_instruction(encoded)
