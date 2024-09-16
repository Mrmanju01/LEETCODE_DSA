342. Power of Four
for i in range(16):
  k=4**i
  if n==k:
    return True
  elif k>n:
    return False
else:
  return False
