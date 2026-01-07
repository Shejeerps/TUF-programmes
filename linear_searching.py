"""
program for linear searching

"""
class linearsearching:
    def solution(self,arr,element):
        i=0
        is_present=False
        while(i<len(arr)):
            if arr[i] == element:   
                is_present=True
                break
            i+=1
        print(is_present)
Lsearch_instance=linearsearching()
arr=[12,14,17,18,16]
element=17
Lsearch_instance.solution(arr,element)        

        