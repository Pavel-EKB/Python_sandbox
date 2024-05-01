import random
def quicksort(nums):
   if len(nums) <= 1:
       return nums
   else:
       q = nums[int(len(nums)/2)]
       #q = random.choice(nums)
   l_nums = [n for n in nums if n < q]

   e_nums = [q] * nums.count(q)
   b_nums = [n for n in nums if n > q]
   return quicksort(l_nums) + e_nums + quicksort(b_nums)

print (quicksort([3,7,9,2,4,6,1,8,0,5,4,7,8,3,1,6,]))

#С использованием генераторов:
def qsort(L):
  if L: return qsort([x for x in L[1:] if x<L[0]]) + L[0:1] + qsort([x for x in L[1:] if x>=L[0]])
  return []

print (qsort([3,7,9,2,4,6,1,8,0,5,4,7,8,3,1,6,]))