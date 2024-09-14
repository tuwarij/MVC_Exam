import csv

csv_path = "Model/Cow_infomation.csv"

#อ่านข้อมูลจากไฟล์ csv
def readCSV():
    with open(csv_path,mode='r') as file:
        csv_reader = csv.reader(file)
        data = []
        next(csv_reader)
        for row in csv_reader:
            data.append(row)
        return data