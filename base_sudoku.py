
def validate_columns(puzzle):
  i = 0
  while i<9:
    num = [0 for x in range(0, 9)]
    j = 0
    while j<9:
      if puzzle[i][j] != '.':
        num[int(puzzle[i][j])-1] += 1
      j+=1

    for n in num:
      if n>1:
        return False
    i +=1
  return True

def validate_rows(puzzle):
  i = 0
  while i<9:
    num = [0 for x in range(0, 9)]
    j = 0
    while j<9:
      if puzzle[j][i] != '.':
        num[int(puzzle[j][i])-1] +=1
      j+=1

    for n in num:
      if n>1:
        return False
    i +=1
  return True

def validate_grids(puzzle):
  i = 0
  while i<9:
    k = 0
    while k<9:
      num = [0 for x in range(0, 9)]
      r = 0+i
      
      while r<3+i:
        c = 0+k
        while c<3+k:
          if puzzle[r][c]!='.':
            num[int(puzzle[r][c])-1] +=1
          c +=1
        r +=1
      for n in num:
        if n>1:
          return False
      k +=3
    i +=3
  return True

def validate_puzzle(puzzle):
  if not validate_columns(puzzle):
    return False
  if not validate_rows(puzzle):
    return False
  if not validate_grids(puzzle):
    return False
  return True

def find_unassigned(puzzle):
  i = 0
  while i<9:
    j = 0
    while j<9:
      if puzzle[i][j]=='.':
        return (i,j)
      j+=1
    i+=1
  return (-1,-1)

def ispresent(puzzle, row, col, num):
  i = 0
  while i<9:
    if not puzzle[i][col] == '.':
      if int(puzzle[i][col])==num:
        return True
    if not puzzle[row][i] == '.':
      if int(puzzle[row][i])==num:
        return True
    i +=1
  
  i = 0
  while i<3:
    j = 0
    while j<3:
      if not puzzle[i+row-row%3][j+col-col%3] == '.':
        if int(puzzle[i+row-row%3][j+col-col%3])==num:
          return True
      j +=1
    i +=1
  return False

def solve_puzzle(puzzle):
  (row,col) = find_unassigned(puzzle)
  if row==-1:
    #It is solved as no unassigned position.
    print 'Solved'
    return True

  i = 1
  while i<=9:
    if not ispresent(puzzle, row, col, i):
      puzzle[row][col] = str(i)
      if solve_puzzle(puzzle):
        return True
      puzzle[row][col]  = '.'
    i +=1

  return False

def main():
  return

# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()
