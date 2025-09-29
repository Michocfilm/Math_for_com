import pandas as pd
from pymongo import MongoClient
from datetime import datetime

# โหลดไฟล์ Excel
df = pd.read_excel('TaskReportmmm.xlsx')

# เลือกเฉพาะ column ที่ต้องการ
df = df[["customer", "colA", "colB", "job", "employ", "categor", "workOrder",
         "serviceTeam","inspectorCheck","workDate","dayWeek","timeWork"]] 

# รวม colA และ colB เป็น location
df["location"] = df["colA"].astype(str) + " " + df["colB"].astype(str)

# แปลง staffList
df["staffList"] = df.apply(lambda row: [{"name": row["employ"], "category": row["categor"]}], axis=1)

# แปลงเวลาเป็น timeStart / timeEnd
df[["timeStart","timeEnd"]] = df["timeWork"].str.split(" - ", expand=True)

# แปลง serviceTeam / inspectorCheck / dayWeek เป็น list
df["serviceTeamChecklistItems"] = df["serviceTeam"].apply(lambda x: [i.strip() for i in str(x).split(",") if i.strip()])
df["inspectorChecklistItems"] = df["inspectorCheck"].apply(lambda x: [i.strip() for i in str(x).split(",") if i.strip()])
df["workingDays"] = df["dayWeek"].apply(lambda x: [i.strip() for i in str(x).split(",") if i.strip()])

# rename column workOrder
df.rename(columns={"customer": "customerName",
                   "job": "jobType",
                   "workOrder": "workOrderNoExternal"}, inplace=True)

df["statusCount"] = "1"

columns_to_save = ["customerName","jobType","statusCount","location",
                   "staffList","workOrderNoExternal",
                   "serviceTeamChecklistItems","inspectorChecklistItems",
                   "workingDays","timeStart","timeEnd"]

# แปลง DataFrame เป็น list ของ dictionary
data = df[columns_to_save].to_dict(orient="records")

# เชื่อมต่อ MongoDB
client = MongoClient("mongodb://tests")
db = client["myBestAppDb"]
collection = db["workorders"]

for record in data:
    work_order = record["workOrderNoExternal"]
    
    # สร้าง workOrderNoSystem
    work_date = pd.to_datetime(record.get("workDate", datetime.today())).strftime("%y%m%d")
    # หาเลขต่อท้าย XXX
    existing_systems = collection.find({"workOrderNoSystem": {"$regex": f"WO{work_date}"}})
    max_suffix = 0
    for doc in existing_systems:
        suffix = int(doc["workOrderNoSystem"][-3:])
        if suffix > max_suffix:
            max_suffix = suffix
    new_suffix = f"{max_suffix+1:03d}"
    record["workOrderNoSystem"] = f"WO{work_date}{new_suffix}"

    # เช็คว่า workOrderNoExternal มีอยู่แล้วไหม
    existing_doc = collection.find_one({"workOrderNoExternal": work_order})
    
    if existing_doc:
        # ถ้ามีซ้ำ ให้เพิ่ม staffList ของ row นี้เข้าไปใน document เดิม
        collection.update_one(
            {"_id": existing_doc["_id"]},
            {"$push": {"staffList": {"$each": record["staffList"]}}}
        )
    else:
        # ถ้าไม่มีซ้ำ ให้ insert document ใหม่
        collection.insert_one(record)
