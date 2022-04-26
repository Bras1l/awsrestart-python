import csv
import copy
myVehicle = {
    "vin" : "<empty>",
    "make" : "<empty>" ,
    "model" : "<empty>" ,
    "year" : 0,
    "range" : 0,
    "topSpeed" : 0,
    "zeroSixty" : 0.0,
    "mileage" : 0
}
myInventoryList = []
with open('car_fleet.csv') as csvFile: 
 csvReader = csv.reader(csvFile, delimiter=',')
 lineCount = 0  
 for row in csvReader:
    if lineCount == 0:
        print(f'Column names are: {", ".join(row)}')  
        lineCount += 1  
 else:  
         print(
                f'vin: {row[0]}\n'
                f'make: {row[1]}\n'
                f'make: {row[1]}\n'
                f'model: {row[2]}\n'
                f'year: {row[3]}\n'
                f'range: {row[4]}\n'
                f'topSpeed: {row[5]}\n'
                f'zeroSixty: {row[6]}\n' 
                f'mileage: {row[7]}\n'
            )
currentVehicle = copy.deepcopy(myVehicle)
currentVehicle["vin"] = row[0]  
currentVehicle["make"] = row[1]  
currentVehicle["model"] = row[2]  
currentVehicle["year"] = row[3]  
currentVehicle["range"] = row[4]  
currentVehicle["topSpeed"] = row[5]  
currentVehicle["zeroSixty"] = row[6]  
currentVehicle["mileage"] = row[7]
myInventoryList.append(currentVehicle)
lineCount += 1
print(f'Processed {lineCount} lines.')
    #
print('---- my inventory ----')
with open('car_fleet.csv') as csvFile:
    
 for myCarProperties in myInventoryList:
  for key, value in myCarProperties.items():
        print("{} : {}".format(key,value))
        print("-----")
        