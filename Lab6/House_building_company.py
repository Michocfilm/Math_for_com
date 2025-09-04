import math

def calculate_angles(a: float, b: float, c: float) -> float:
    """ฟังก์ชันที่ 1 คำนวณมุมของรูปสามเหลี่ยม"""
    # Cosine Rule: cosA = (b^2 + c^2 - a^2) / (2bc)
    A:float = math.degrees(math.acos((b**2 + c**2 - a**2) / (2 * b * c)))
    B:float = math.degrees(math.acos((a**2 + c**2 - b**2) / (2 * a * c)))
    C:float = math.degrees(math.acos((a**2 + b**2 - c**2) / (2 * a * b)))
    return A,B,C


def sum_of_angles(angles: float) -> tuple[float, bool]:
    """ฟังก์ชันที่ 2 คำนวณผลบวกของมุมรวมภายในสามเหลี่ยม"""
    total:float = sum(angles)
    return total, total == 180

a:float = float(input("a = "))
b:float = float(input("b = "))
c:float = float(input("c = "))
angles = calculate_angles(a, b, c)
print(f"Angle A = {angles[0]:.2f}")
print(f"Angle B = {angles[1]:.2f}")
print(f"Angle C = {angles[2]:.2f}")

total, check = sum_of_angles(angles)
print(f"Sum of internal angles = {total:.2f}")
print(f"Is the sum equal to 180?: {check}")
