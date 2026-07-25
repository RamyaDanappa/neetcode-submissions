class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        arr_len =len(arr)
        res =[]
        for i in range(1,arr_len):
            
            max_val =max(arr[i:arr_len])
            res.append(max_val)
        res.append(-1)
        return res