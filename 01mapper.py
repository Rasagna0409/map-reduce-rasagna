import sys

for line in sys.stdin:  
    dataList = line.strip().split(",") 
    
    if (len(dataList) == 10) :
        Manufacturer,Model,Price,Transmission,Power,EngineCC,Fuel,Male,Female,Total = dataList 
        print (Manufacturer,"\t", Total)
