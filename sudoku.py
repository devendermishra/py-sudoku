import sys
from base_sudoku import *

def parse_puzzle(filename):
  #To be implemented.
  puzzle = [['.' for x in range(0,9)] for x in range(0,9)]
  file = open(filename, 'r')
  if not file:
    print 'File cannot be opened'
    sys.exit(1)
  for row in range(0,9):
    for col in range(0,9):
      c = file.read(1)
      puzzle[row][col] = c
    #Discard newline character
    c = file.read(1)
  return puzzle

def print_soln(puzzle):
  for row in puzzle:
    for col in row:
      print col+' ',
    print ''
  return

def write_puzzle(puzzle, filename):
  file = open(filename, "w")
  for row in puzzle:
    for col in row:
      file.write(col)
    file.write('\n')
  file.close()
  return

def main():
  if len(sys.argv) <3:
    print 'Usage: sudoku.py <filename> <soln-file>'
  
  filename = sys.argv[1]
  soln  = sys.argv[2]
  puzzle = parse_puzzle(filename)
  #print 'Puzzle is'
  #print puzzle
  if not validate_puzzle(puzzle):
    print 'Invalid puzzle'
    return
  if not solve_puzzle(puzzle):
    print 'Puzzle is not solved'
    return
  if not validate_puzzle(puzzle):
    print 'Solution is not valid.'
    return
  print_soln(puzzle)
  write_puzzle(puzzle, soln)

# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()
