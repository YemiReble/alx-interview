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
          perimeter += 4
        else:
          # Check if the cell is adjacent to any water cells.
          if grid[i - 1][j] == 0 or grid[i + 1][j] == 0 or grid[i][j - 1] == 0 or grid[i][j + 1] == 0:
            perimeter += 1

  # If the grid has any "lakes", subtract the perimeter of each lake from the
  # total perimeter.
  for i in range(len(grid)):
    for j in range(len(grid[0])):
      if grid[i][j] == 0:
        # Count the number of adjacent land cells.
        adjacent_land_cells = 0
        if i > 0 and grid[i - 1][j] == 1:
          adjacent_land_cells += 1
        if i < len(grid) - 1 and grid[i + 1][j] == 1:
          adjacent_land_cells += 1
        if j > 0 and grid[i][j - 1] == 1:
          adjacent_land_cells += 1
        if j < len(grid[0]) - 1 and grid[i][j + 1] == 1:
          adjacent_land_cells += 1

        # If the number of adjacent land cells is greater than 0, then this
        # is a lake.
        if adjacent_land_cells > 0:
          perimeter -= 4

  return perimeter

