import csv 
import json

csv_file_path = './Data/twcs.csv'
jsonl_file = "./Data/twcs.jsonl"

with open(csv_file_path , "r" , encoding ="utf-8") as infile, \
     open(jsonl_file , "w" , encoding="utf-8") as outfile:


     reader = csv.DictReader(infile)

     for row in reader:
          item = {
               "instruction" : row.get("instruction" , ""),
               "input" : row.get("input",""),
               "output": row.get("output", "")
          }

          outfile.write(json.dumps(item,ensure_ascii=False) + "\n")

print("JSONL created!")
