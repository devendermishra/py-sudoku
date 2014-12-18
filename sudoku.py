def parse_puzzle(filename):
  #To be implemented.
  return []

def validate_columns(puzzle):
  i = 0
  while i<9:
    num = [0 for x in range(0, 9)]
    j = 0
    while j<9:
      if puzzle[i][j] != '.':
        num[int(puzzlen[i][j])-1] += 1
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
      
      while r<3+j:
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
    i +=1
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
    if int(puzzle[i][col])==num or int(puzzle[row][i])==num:
      return True
    i +=1
  
  i = 0
  while i<3:
    j = 0
    while j<3:
      if int(puzzle[i+row-row%2][j+col-col%3])==num:
        return True
      j +=1
    i +=1
  return False


def solve_puzzle(puzzle):
  (row,col) = find_unassigned(puzzle)
  if row==-1:
    #It is solved as no unassigned position.
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

def print_soln(puzzle):
  return

def write_puzzle(puzzle, filename):
  return

import sys

def main():
  if len(sys.argv) <3:
    print 'Usage: sudoku.py <filename> <soln-file>
  
  filename = sys.argv[1]
  soln  = sys.argv[2]
  puzzle = parse_puzzle(filename)
  if not validate_puzzle(puzzle):
    print 'Invalid puzzle'
    return
  if not solve_puzzle(puzzle):
    print 'Puzzle is not solved'
    return
  print_soln(puzzle)
  write_puzzle(puzzle, soln)

