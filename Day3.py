118. Pascal's Triangle


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
      fi=[[1]]
      for r in range(numsRow-1):
        t=[0]+fi[-1]+[0]
        row=[]
        for c in range(len(fi[-1]+1)):
          row.append(t[c]+t[c+1])
        fi.append(row)
      return fi
