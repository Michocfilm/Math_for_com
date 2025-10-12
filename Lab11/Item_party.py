def input_items(prompt):
    """ฟังก์ชันรับข้อมูลจากผู้ใช้และตรวจสอบความถูกต้อง"""
    try:
        items_input = input(prompt).strip()
        if not items_input:
            raise ValueError("empty")

        items_list = [item.strip() for item in items_input.split(',') if item.strip()]

        if not items_list:
            raise ValueError("invalid")

        return set(items_list)

    except ValueError as e:
        if str(e) == "empty":
            print("ข้อผิดพลาด: กรุณากรอกรายการสินค้าอย่างน้อยหนึ่งรายการ")
        elif str(e) == "invalid":
            print("ข้อผิดพลาด: กรุณากรอกชื่อรายการสินค้าที่ถูกต้อง")
        return None
    except Exception:
        print("ข้อผิดพลาด: เกิดข้อผิดพลาดที่ไม่ทราบสาเหตุ")
        return None


try:
    # ที่มี
    kitchen_items = None
    while kitchen_items is None:
        kitchen_items = input_items("กรอกรายการสินค้าที่มีอยู่แล้วในครัว: ")

    # ที่ต้องซื้อ
    shopping_items = None
    while shopping_items is None:
        shopping_items = input_items("กรอกรายการสินค้าที่ต้องซื้อ: ")

    print("\nรายการสินค้าทั้งหมดที่ต้องมี:", kitchen_items | shopping_items)
    print("รายการสินค้าที่ซ้ำกัน:", kitchen_items & shopping_items)
    print("รายการสินค้าที่มีอยู่แล้วในครัว ไม่ต้องซื้ออีก:", kitchen_items - shopping_items)
    print("รายการสินค้าที่ต้องซื้อแต่ไม่มีในครัว:", shopping_items - kitchen_items)
    print("รายการสินค้าที่ไม่ซ้ำกัน:", kitchen_items ^ shopping_items)

except Exception:
    print("ข้อผิดพลาด: เกิดข้อผิดพลาดที่ไม่ทราบสาเหตุ")
