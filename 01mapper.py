import sys

for line in sys.stdin:  
    dataList = line.strip().split(",") 
    
    if (len(dataList) == 8) :
        BGGId,Name,Description,YearPublished,GameWeight,AvgRating,BayesAvgRating,StdDev= dataList 
        print (Name,"\t", StdDev)
