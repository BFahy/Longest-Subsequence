#Comparison between two strings to find the longest common subsequence.

dna_1 = "ACCGTT"
dna_2 = "CCAGCA"

#Function defined with two parameters for comparison.
def longest_common_subsequence(string_1, string_2):
  print("Finding longest common subsequence of {0} and {1}".format(string_1, string_2))
  #Defining grid layout where the column represents each character from one string
  #Row will represent each character from the other string, extra column/row is added to represent empty character.
  grid = [[0 for col in range(len(string_1) + 1)] for row in range(len(string_2) + 1)]
  #Nested for loop to compare each letter with each letter from the other.
  for row in range(1, len(string_2) + 1):
    print("Comparing: {0}".format(string_2[row - 1]))
    for col in range(1, len(string_1) + 1):
      print("Against: {0}".format(string_1[col - 1]))
      #If statement to check column against row.
      if string_1[col - 1] == string_2[row - 1]:
        grid[row][col] = grid[row - 1][col - 1] + 1
      else:
        grid[row][col] = max(grid[row - 1][col], grid[row][col - 1])
  #To display grid at the end.
  #for row_line in grid:
    #print(row_line)

#string_1 is col and string_2 is row
  result = []

  while row > 0 and col > 0:
    if string_1[col - 1] == string_2[row - 1]:
      result.append(string_1[col - 1])
      row -= 1
      col -= 1
  #Checking if the value at the prior row is greater than the value at the prior col.
    elif grid[row - 1][col] > grid[row][col - 1]:
      row -= 1
  #If it isn't greater, decrement col and leave row the same.
    else:
      col -= 1
  result.reverse()
  return "".join(result)



print("Result: ", longest_common_subsequence(dna_1, dna_2))