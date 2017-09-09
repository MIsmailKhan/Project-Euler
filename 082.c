int[,] grid = readInput(filename);
int gridSize = grid.GetLength(0);
 
//calculate the solution for bottom and right
for (int i = gridSize - 2; i >= 0; i--) {
    grid[gridSize - 1, i] += grid[gridSize - 1, i+1];
    grid[i,gridSize - 1] += grid[i+1, gridSize - 1];
}
 
for (int i = gridSize - 2; i >= 0; i--) {
    for (int j = gridSize - 2; j >= 0; j--) {
        grid[i, j] += Math.Min(grid[i + 1, j], grid[i, j + 1]);
    }
}
