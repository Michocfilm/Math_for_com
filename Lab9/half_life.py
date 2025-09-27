import math
def Drug_concentration(initial_dose:int, half_life:int, duration:int, interval:int):
    # สูตรคำนวณค่า k (อัตราการสลายตัว) จากครึ่งชีวิตของยา : k = ln(2) / half_life
    k = math.log(2) / half_life
    
    # dictionary เก็บผลลัพธ์ key เวลา value ความเข้มข้น
    concentration_dict = {}
    
    for t in range(0, duration + 1, interval):
        C = initial_dose * math.exp(-k * t)
        concentration_dict[t] = C
    
    print(f"ปริมาณยาเริ่มต้น: {initial_dose} มิลลิกรัม\nครึ่งชีวิตของยา: {half_life} ชั่วโมง\nระยะเวลาที่คำนวณ: {duration} ชั่วโมง\n")
    
    print("ความเข้มข้นของยาตามเวลา:")
    print("เวลา (ชั่วโมง) | ความเข้มข้น (มิลลิกรัม)")
    print("-----------------------------------")
    for t, C in concentration_dict.items():
        print(f"{t:12d} | {C:18.2f}")
    
    print(f"\nเวลาที่ความเข้มข้นลดลงครึ่งหนึ่ง: {half_life} ชั่วโมง")

initial_dose = int(input("ปริมาณยาเริ่มต้น: "))
half_life = int(input("ครึ่งชีวิตของยา: "))
duration = int(input("ระยะเวลาที่คำนวณ: "))
interval = 2
Drug_concentration(initial_dose, half_life, duration, interval)
