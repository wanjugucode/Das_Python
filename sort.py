from re import X
from Abstract import CSVSort

class MergeSort(CSVSort):
   
    
    def  __init__(self, data):
        self.data = data
    
    def sortData(self):
        if len(self.data) >1:
            middle = len(self.data)//2
            left =  self.data[:middle]
            right = self.data[middle:]

            leftSort = MergeSort(left)
            leftSort.sortData()

            rigthSort = MergeSort(right)
            rigthSort.sortData()            

            b = x=z=0
            while b < len(left) and x < len(right):
                if left[b][1] < right[x][1]:
                    self.data[z] = left[b]
                    b +=1
                
                else:
                    self.data[z]=right[x]
                    x+=1
                z+=1
            
            while b < len(left):
                self.data[z] = left[b]
                b+=1
                z+=1
            
            while x < len(right):
                self.data[z] = right[x]
                x+=1
                z+=1
        
        print(self.data)