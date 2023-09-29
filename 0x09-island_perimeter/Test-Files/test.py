def island_perimeter(grid):
  """Calculates the perimeter of the island described in grid.

  Args:
    grid: A list of lists of integers, where 0 represents water and 1 represents land.

  Returns:
    The perimeter of the island.
  """

  perimeter = 0
  for i in range(len(grid)):
    for j in range(len(grid[0])):
      if grid[i][j] == 1:
        # Check if the cell is on the edge of the grid.
        if i == 0 or i == len(grid) - 1 or j == 0 or j == len(grid[0]) - 1:
          perimeter += 1
        else:
          # Check if the cell is adjacent to any water cells.
          if grid[i - 1][j] == 0 or grid[i + 1][j] == 0 or grid[i][j - 1] == 0 or grid[i][j + 1] == 0:
            perimeter += 1

  return perimeter
