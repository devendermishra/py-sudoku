import sys
import random
from base_sudoku import *

def generate_sudoku():
  random.seed()
  puzzle = [['.' for x in range(0,9)] for x in range(0,9)]
  numclues = random.randint(9,17)
  i = 1
  while i<= numclues:
    x = random.randint(0,8)
    y = random.randint(0,8)
    print str(x)+", "+str(y)
    if puzzle[x][y] !='.':
      continue
    start_num = random.randint(1,9)
    num = start_num
    while num <=9:
      puzzle[x][y] = str(num)
      if validate_puzzle(puzzle):
        break
      puzzle[x][y] = '.'
      num +=1
    num = 1
    while num<start_num:
      puzzle[x][y] = str(num)
      if validate_puzzle(puzzle):
        break
      puzzle[x][y] = '.'
      num +=1
    i +=1
  return puzzle

def write_puzzle(puzzle, filename):
  file = open(filename, "w")
  for row in puzzle:
    for col in row:
      file.write(col)
    file.write('\n')
  file.close()
  return

def main():
  if len(sys.argv) <2:
    print 'Usage: generate_sudoku.py <filename>'
  
  filename = sys.argv[1]
  puzzle = generate_sudoku()
  if not validate_puzzle(puzzle):
    print 'Puzzle generated is not valid'
    #return
  write_puzzle(puzzle, filename)

# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()