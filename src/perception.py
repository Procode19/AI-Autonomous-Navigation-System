# Perception module for obstacle detection
# In this simplified version, obstacles are known from the grid
# For advanced version, we can add computer vision for image-based detection

def get_obstacles(grid):
    """
    Returns a list of obstacle positions from the grid.
    """
    obstacles = []
    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            if grid[i, j] == 1:
                obstacles.append((i, j))
    return obstacles

# Future: Add function to detect obstacles from image using OpenCV
# def detect_obstacles_from_image(image):
#     # Convert to grayscale, threshold, find contours, etc.
#     pass