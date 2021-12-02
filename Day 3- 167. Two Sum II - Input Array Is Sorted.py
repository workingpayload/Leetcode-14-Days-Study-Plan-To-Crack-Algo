class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i=0
        j=len(numbers)-1
        list = []
        while(i<j):
            if numbers[i]+numbers[j]==target:
                list.append(i)
                list.append(j)
                list2 = [n+1 for n in list] 
                return list2
            elif numbers[i]+numbers[j]<target:
                i+=1
            else:
                j-=1
