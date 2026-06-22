from graphics import Canvas
import math

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 300

CLOUD_WIDTH = 120
CLOUD_HEIGHT = 80

TRUNK_HEIGHT = 80
TRUNK_WIDTH = 20
LEAVES_SIZE = 60

TREE_BOTTOM_Y = CANVAS_HEIGHT - 20


def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)

    # Clouds
    draw_cloud(canvas, 20, 20, "pink")
    draw_cloud(canvas, 140, 10, "salmon")
    draw_cloud(canvas, 260, 20, "purple")

    # Trees
    draw_tree(canvas, 70, "green")
    draw_tree(canvas, 170, "red")
    draw_tree(canvas, 310, "orange")


def draw_cloud(canvas, x, y, color):
    """
    Draws one cloud.
    """
    cloud_bottom_start_y = y + (1 / 3) * CLOUD_HEIGHT
    cloud_bottom_end_y = y + CLOUD_HEIGHT
    cloud_top_start_x = x + (1 / 4) * CLOUD_WIDTH
    cloud_top_end_x = x + (3 / 4) * CLOUD_WIDTH

    # Bottom left puff
    canvas.create_oval(
        x,
        cloud_bottom_start_y,
        x + (3 / 4) * CLOUD_WIDTH,
        cloud_bottom_end_y,
        color
    )

    # Bottom right puff
    canvas.create_oval(
        x + (1 / 4) * CLOUD_WIDTH,
        cloud_bottom_start_y,
        x + CLOUD_WIDTH,
        cloud_bottom_end_y,
        color
    )

    # Top puff
    canvas.create_oval(
        cloud_top_start_x,
        y,
        cloud_top_end_x,
        y + (2 / 3) * CLOUD_HEIGHT,
        color
    )


def draw_tree(canvas, x, leaves_color):
    """
    Draws one tree.
    x = center position of trunk
    """

    # Trunk
    canvas.create_rectangle(
        x,
        TREE_BOTTOM_Y - TRUNK_HEIGHT,
        x + TRUNK_WIDTH,
        TREE_BOTTOM_Y,
        "brown"
    )

    # Leaves
    canvas.create_oval(
        x - 20,
        TREE_BOTTOM_Y - TRUNK_HEIGHT - LEAVES_SIZE + 10,
        x + TRUNK_WIDTH + 20,
        TREE_BOTTOM_Y - TRUNK_HEIGHT + 10,
        leaves_color
    )


if __name__ == '__main__':
    main()