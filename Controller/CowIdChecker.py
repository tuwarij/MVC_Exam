from Controller.csvReader import readCSV

#เช็คว่า Cow ID ที่ผู้ใช้ใส่เข้ามาถูกต้องหรือไม่
def CheckCowId(cowId):
    isvalid = True
    if not cowId.isdigit():
        isvalid = False
        print("Cow ID must be a number")
        
    if len(cowId) != 8:
        isvalid = False
        print("Cow ID must have 8 digits")
        
    if cowId.startswith("0"):
        isvalid = False
        print("Cow ID cannot start with 0")
        
    return isvalid
#เช็คว่ามีข้อมูลของวัวตัวนั้นไหม
def checkCowData(cowId):
    cowData = readCSV()
    for cow in cowData:
        if cow[0] == cowId:
            return True
    return False