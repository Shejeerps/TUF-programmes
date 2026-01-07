class Binarysearch:
    def solution(self,arr,element):
        arr.sort()
        low=0
        upp=len(arr)-1
        is_present=False
        while(low<=upp):
            mid=(low+upp)//2
            if arr[mid]==element:
                is_present=True
                break
            elif element<arr[mid]:
                upp=mid-1
            elif element>arr[mid]:
                low=mid+1
        print(is_present)
b_search_instance=Binarysearch()
arr=[14,16,18,19,20,22]
element=16
b_search_instance.solution(arr,element)

