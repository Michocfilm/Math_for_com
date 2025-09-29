from pymongo import MongoClient

# เชื่อมต่อ MongoDB
client = MongoClient("mongodb://test")
db = client["myBestAppDb"]

employee_col = db["employees"]
workorders_col = db["workorders"]

# ดึง workorders ทั้งหมด
workorders = workorders_col.find({})

for workorder in workorders:
    staff_list = workorder.get("staffList", [])

    updated_staff_list = []
    for staff in staff_list:
        full_name = staff.get("name", "").strip()
        if not full_name:
            updated_staff_list.append(staff)
            continue

        # แยกชื่อ (เอาคำแรกเป็น firstname ที่เหลือเป็น lastname)
        parts = full_name.split()
        firstname = parts[0]
        lastname = " ".join(parts[1:]) if len(parts) > 1 else ""

        # ค้นหาใน employee
        employee = employee_col.find_one({"firstName": firstname, "lastName": lastname})
        if employee:
            staff["id_employee"] = str(employee["_id"])

        updated_staff_list.append(staff)

    # อัปเดตกลับไปที่ workorders
    workorders_col.update_one(
        {"_id": workorder["_id"]},
        {"$set": {"staffList": updated_staff_list}}
    )

print("Update success!")
