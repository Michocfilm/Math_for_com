from pymongo import MongoClient
import requests
import time
from tqdm import tqdm

# ตั้งค่า MongoDB
client = MongoClient("mongodb://xxx.x.x.x/")
db = client["mydata"]
collection = db["workorders"]

# ฟังก์ชันหา lat,long จาก location ด้วย Nominatim พร้อม retry
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
        # เว้น 2 วินาทีระหว่าง retry
        time.sleep(2)
    return None, None

# ฟังก์ชันกำหนด region ตามจังหวัด (เหมือนเดิม)
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

# ดึงเอกสารทั้งหมด
docs = list(collection.find())

# วนอัปเดต document พร้อม progress bar
for doc in tqdm(docs, desc="Updating documents"):
    address = f"{doc.get('customerName','')} {doc.get('location','')}"
    latlong, province = get_latlong(address)

    if latlong and province:
        region = get_region(province)
        collection.update_one(
            {"_id": doc["_id"]},
            {"$set": {"latlong": latlong, "region": region}}
        )
    # เว้น 2 วินาทีระหว่าง document เพื่อ respect rate limit
    time.sleep(2)
