SET MATRIX ZEROS------PROBLEM NUM 73
row=[0]*len(mat)
col=[0]*len(mat[0])
for i in range(len(mat)):
  for j in range(len(mat[0])):
    if matrix[i][j]==0:
      row[i]=1
      col[j]=1
for i in range(len(mat)):
  for j in range(len(mat[0])):
    if row[i]=1 or col[j]=1 :
      matrix[i][j]=0
return matrix
    
