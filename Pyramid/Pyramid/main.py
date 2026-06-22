from graphics import Canvas
import random

CANVAS_WIDTH = 600      # Width of drawing canvas in pixels
CANVAS_HEIGHT = 300     # Height of drawing canvas in pixels

BRICK_WIDTH = 30        # The width of each brick in pixels
BRICK_HEIGHT = 12       # The height of each brick in pixels
BRICKS_IN_BASE = 14     # The number of bricks in the base

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    
    num_rows = BRICKS_IN_BASE  # Pyramid has same number of rows as base bricks
    
    for row in range(num_rows):
        # Number of bricks in this row (base has most, top has 1)
        bricks_in_row = BRICKS_IN_BASE - row
        
        # Total width of this row
        row_width = bricks_in_row * BRICK_WIDTH
        
        # X start to center the row horizontally
        x_start = (CANVAS_WIDTH - row_width) / 2
        
        # Y position: rows stack from bottom up
        y = CANVAS_HEIGHT - (row + 1) * BRICK_HEIGHT
        
        for col in range(bricks_in_row):
            x = x_start + col * BRICK_WIDTH
            canvas.create_rectangle(
                x, y,
                x + BRICK_WIDTH, y + BRICK_HEIGHT,
                "yellow", "black"
            )

if __name__ == '__main__':
    main()