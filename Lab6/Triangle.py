import math
def calculate_angles(a:float, b:float, A:float) -> float:
    """ฟังก์ชันคำนวณมุมของรูปสามเหลี่ยม"""
    A_rad:float = math.radians(A)   # แปลงมุม A เป็นเรเดียน
    sin_B:float = (b*math.sin(A_rad))/a
    if sin_B > 1:
        sin_B = 1
    elif sin_B < -1:
        sin_B = -1
    B:float = math.degrees(math.asin(sin_B))
    return B

a = 2.5
b = 3.41
A = 30
B = calculate_angles(a, b, A)
print(f"มุม B ประมาณ {B:.2f} องศา")
