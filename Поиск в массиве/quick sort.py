import random
from random import randint
N=10
A = [randint(1,10) for i in range(N)]
A1 = A.copy()
A2 = A.copy()
A3 = A.copy()
# процедура сортировки А
def qSort ( A, nStart, nEnd ):
                if nStart >= nEnd: return
                L = nStart; R = nEnd
                X = A[(L+R)//2]
                while L <= R:
                                while A[L] < X: L += 1 # разделение
                                while A[R] > X: R -= 1
                                if L <= R:
                                                A[L], A[R] = A[R], A[L]
                                                L += 1; R -= 1
                qSort ( A, nStart, R ) # рекурсивные вызовы
                qSort ( A, L, nEnd )

print(A)
# вызов процедуры
qSort ( A, 0, N-1 )
print('A= ', A)

# процедура сортировки А1------------------------
def qsort(L):
        if L: return qsort([x for x in L[1:] if x<L[0]]) + L[0:1] + qsort([x for x in L[1:] if x>=L[0]])
        return []
print('A1=', qsort(A1))

# процедура сортировки А2------------------------
def quicksort(nums):
   if len(nums) <= 1:
       return nums
   else:
       q = random.choice(nums)
       s_nums = []
       m_nums = []
       e_nums = []
       for n in nums:
           if n < q:
               s_nums.append(n)
           elif n > q:
               m_nums.append(n)
           else:
               e_nums.append(n)
       print('   ', s_nums, ' ', e_nums, ' ', m_nums)
       return quicksort(s_nums) + e_nums + quicksort(m_nums)
print('A2=', quicksort(A2))

# процедура сортировки А3------------------------
def quicksort_opt(nums):
   if len(nums) <= 1:
       return nums
   else:
       q = random.choice(nums)
   l_nums = [n for n in nums if n < q]

   e_nums = [q] * nums.count(q)
   b_nums = [n for n in nums if n > q]
   return quicksort_opt(l_nums) + e_nums + quicksort_opt(b_nums)

print('A3=', quicksort_opt(A3))