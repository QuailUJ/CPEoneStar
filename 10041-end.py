# python
n = int(input())
for i in range(n):
  adr = list(map(int,input().split()))
  adr.pop(0) #刪掉第一筆
  adr.sort()
  med = adr[len(adr)//2] #取中位數

  ans = 0
  for a in adr:
    ans+= abs(a-med)
  print(ans)

'''
範例輸入:
2          (幾組測資)n
2(有幾筆) 2 4      (測資) 
3(有幾筆) 2 4 6

範例輸出:
2
4
'''