def calculate_compound_interest(**kwargs:float) -> str:
    """ฟังก์ชันที่ 1 คำนวณดอกเบี้ยทบต้น"""
    p:float = kwargs['principal']
    r:float = kwargs['rate']
    n:int = kwargs['years']
    A:float = p*(1 + (r/100))**n
    B:float = A-p #ดอกเบี้ยที่ได้รับ
    return f"เงินต้น {p:.2f} บาท\nอัตราดอกเบี้ย {r:.2f}% ต่อปี\nระยะเวลา {n} ปี\nจำนวนเงินสุดท้าย {A:.2f} บาท\nดอกเบี้ยที่ได้รับ {B:.2f} บาท"

def display_results(n:str):
    """ฟังก์ชันที่ 2 แสดงผลลัพธ์การคำนวณดอกเบี้ยทบต้น"""
    print(n)

result:str = calculate_compound_interest(principal=50000, rate=3, years=10)
display_results(result)