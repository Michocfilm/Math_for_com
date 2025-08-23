def convert(GB):
    mb = GB*1024
    kb = mb*1024
    byte = kb*1024
    bit = byte*8
    print(f"Megabyte (MB) : {mb:.2f}\nKilobyte (KB) : {kb:.2f}\nByte : {byte:.2f}\nBit : {bit:.2f}")

gb= float(input("Gigabyte (GB) : "))
convert(gb)