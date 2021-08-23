from os import write
import urllib.request as request
import json
def get_web():
    src = "https://www.ntu.edu.tw"
    with request.urlopen(src) as response:
        data = response.read().decode("utf-8")
    print(data)
def get_data_by_json():
    src = "https://data.taipei/api/v1/dataset/296acfa2-5d93-4706-ad58-e83cc951863c?scope=resourceAquire"
    with request.urlopen(src) as response:
        data = json.load(response)
        data = data["result"]["results"]
        with open("company.txt",mode = "w", encoding = "utf-8") as file:
            for company in data:
                file.write(company["公司名稱"])
                file.write("\n")
                print(company["公司名稱"])
    return 
    
if __name__ == "__main__":
    print(get_web())
    get_data_by_json()