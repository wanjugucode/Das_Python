import csv
from abc import ABC,abstractmethod
from tkinter.font import names

fields = []
rows = []
data=[]

with open('real-estate.csv', 'r') as csvfile:
	csvreader = csv.reader(csvfile)
	fields = next(csvreader)

	for row in csvreader:
		rows.append(row)

	print("Total no. of rows: %d"%(csvreader.line_num))

class CSVSort(ABC):

    @abstractmethod
    def sortData(self):
        pass

class SortData(CSVSort):
    def  __init__(self, data):
        self.data = data
    def sortData(self):
        if len(self.data) >1:
            m = len(self.data)//2
            l =  self.data[1:m]
            r = self.data[m:]

            lSort = SortData(l)
            lSort.sortData()

            rSort = SortData(r)
            rSort.sortData()

            i = j=k=0
            while i < len(l) and j < len(r):
                if l[i][1] < r[j][1]:
                    self.data[k] = l[i]
                    i +=1
                
                else:
                    self.data[k]=r[j]
                    j+=1
                k+=1
            
            while i < len(l):
                self.data[k] = l[i]
                i+=1
                k+=1
            
            while j < len(r):
                self.data[k] = r[j]
                j+=1
                k+=1
        
        print(self.data)

with open('real-estate.csv', 'r') as file:
            reader = csv.reader(file)
            data.extend(list(reader))
sorted = SortData(data)
print(sorted.sortData())


# field names
fieldsnames = ['id', 'price', 'countryCurrency', 'addressStreet','status Type','badgeInfo','hasOpenHouse','relaxed','addressCity','zestimate']

# data rows of csv file
datarows = [ ['265375257', '$330,000','$','1053 Lutheran','FOR_SALE','Null','NULL','FALSE','Atlanta','FALSE'],
		['9844636', '$630,100', '$','153 Black Bear','FOR_SALE','ForSale','TRUE','NULL','Blaine','FALSE'],
		['7468349', '$110,000', '$','1792 12th Street','FOR_SALE','Null','NULL','FALSE','Biloxi','68500'],
		['128749', '$830,500', '$','2513 Swan LN','FOR_SALE','Null','NULL','TRUE','Carson City','342400'],
		['6486438', '$500,900', '$','1104 Old Swanzey','FOR_SALE','ForSale','TRUE','FALSE','Union City','FALSE'],
		['5348347', '$130,000', '$','1153 Oceanfront','FOR_SALE','Null','NULL','FALSE','Missoula','FALSE'],
        ['265375257', '$330,000','$','1053 Lutheran','FOR_SALE','Null','NULL','FALSE','Atlanta','FALSE'],
		['9844636', '$630,100', '$','153 Black Bear','FOR_SALE','ForSale','TRUE','NULL','Blaine','FALSE'],
		['7468349', '$110,000', '$','1792 12th Street','FOR_SALE','Null','NULL','FALSE','Biloxi','68500'],
		['128749', '$830,500', '$','2513 Swan LN','FOR_SALE','Null','NULL','TRUE','Carson City','342400'],
		['6486438', '$500,900', '$','1104 Old Swanzey','FOR_SALE','ForSale','TRUE','FALSE','Union City','FALSE'],
		['5348347', '$130,000', '$','1153 Oceanfront','FOR_SALE','Null','NULL','FALSE','Missoula','FALSE'],
        ['265375257', '$330,000','$','1053 Lutheran','FOR_SALE','Null','NULL','FALSE','Atlanta','FALSE'],
		['9844636', '$630,100', '$','153 Black Bear','FOR_SALE','ForSale','TRUE','NULL','Blaine','FALSE'],
		['7468349', '$110,000', '$','1792 12th Street','FOR_SALE','Null','NULL','FALSE','Biloxi','68500'],
		['128749', '$830,500', '$','2513 Swan LN','FOR_SALE','Null','NULL','TRUE','Carson City','342400'],
		['6486438', '$500,900', '$','1104 Old Swanzey','FOR_SALE','ForSale','TRUE','FALSE','Union City','FALSE'],
		['5348347', '$130,000', '$','1153 Oceanfront','FOR_SALE','Null','NULL','FALSE','Missoula','FALSE'],
        ['265375257', '$330,000','$','1053 Lutheran','FOR_SALE','Null','NULL','FALSE','Atlanta','FALSE'],
		['9844636', '$630,100', '$','153 Black Bear','FOR_SALE','ForSale','TRUE','NULL','Blaine','FALSE'],
		['7468349', '$110,000', '$','1792 12th Street','FOR_SALE','Null','NULL','FALSE','Biloxi','68500'],
		['128749', '$830,500', '$','2513 Swan LN','FOR_SALE','Null','NULL','TRUE','Carson City','342400'],
		['6486438', '$500,900', '$','1104 Old Swanzey','FOR_SALE','ForSale','TRUE','FALSE','Union City','FALSE'],
		['5348347', '$130,000', '$','1153 Oceanfront','FOR_SALE','Null','NULL','FALSE','Missoula','FALSE']]


filename = "agency-real-estate.csv"

with open(filename, 'w') as csvfile:
	csvwriter = csv.writer(csvfile)
	csvwriter.writerow(fields)
	
	csvwriter.writerows(rows)