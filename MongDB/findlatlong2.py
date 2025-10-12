from pymongo import MongoClient
import requests
import time
from tqdm import tqdm

client = MongoClient("mongodb://xx.x.x.x")
db = client["mydata"]
collection = db["workorders"]

def get_latlong(address, max_retries=3):
    url = "https://nominatim.openstreetmap.org/search"
    params = {
        "q": address,
        "format": "json",
        "addressdetails": 1,
        "limit": 1
    }
    for attempt in range(max_retries):
        try:
            response = requests.get(url, params=params, headers={"User-Agent": "Mozilla/5.0"}, timeout=10).json()
            if response:
                lat = response[0]["lat"]
                lon = response[0]["lon"]
                province = response[0]["address"].get("state")
                return f"{lat},{lon}", province
        except Exception as e:
            print(f"Attempt {attempt+1} failed for address '{address}': {e}")
        time.sleep(2)
    return None, None

def get_region(province_name):
    central = ["กรุงเทพมหานคร","นนทบุรี","ปทุมธานี","สมุทรปราการ","อยุธยา"]
    north = ["เชียงใหม่","เชียงราย","ลำพูน","ลำปาง"]
    northeast = ["ขอนแก่น","อุดรธานี","นครราชสีมา"]
    south = ["ภูเก็ต","สงขลา","สุราษฎร์ธานี"]
    east = ["ชลบุรี","ระยอง"]
    west = ["กาญจนบุรี","ราชบุรี"]

    if province_name in central:
        return "ภาคกลาง"
    elif province_name in north:
        return "ภาคเหนือ"
    elif province_name in northeast:
        return "ภาคตะวันออกเฉียงเหนือ"
    elif province_name in south:
        return "ภาคใต้"
    elif province_name in east:
        return "ภาคตะวันออก"
    elif province_name in west:
        return "ภาคตะวันตก"
    elif province_name == "กรุงเทพมหานคร":
        return "กรุงเทพและปริมณฑล"
    else:
        return "ไม่ทราบ"

docs = list(collection.find())

success_count = 0
fail_count = 0
fail_reasons = []

for doc in tqdm(docs, desc="Updating documents"):
    address = f"{doc.get('customerName','')} {doc.get('location','')}".strip()

    if not address:
        fail_count += 1
        fail_reasons.append((doc["_id"], "ไม่มีข้อมูล customerName/location"))
        continue

    latlong, province = get_latlong(address)
    if latlong and province:
        region = get_region(province)
        collection.update_one(
            {"_id": doc["_id"]},
            {"$set": {"latlong": latlong, "region": region}}
        )
        success_count += 1
    else:
        fail_count += 1
        fail_reasons.append((doc["_id"], "API หาไม่เจอ"))

    time.sleep(2)

# สรุปผล
print(f"เพิ่ม field สำเร็จ: {success_count} document")
print(f"ไม่สามารถเพิ่ม field: {fail_count} document")
for doc_id, reason in fail_reasons:
    print(f"Document ID {doc_id} ไม่สามารถเพิ่ม field: {reason}")
