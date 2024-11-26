class RoboPainter:
    def __init__(self):
        self.canvas = None  # Initialize with no canvas
        self.brush_color = (0, 0, 0)  # Default color: black

    def activate(self):
        print("RoboPainter activated!")

    def set_canvas(self, width, height):
        self.canvas = np.zeros((height, width, 3), dtype=np.uint8)  # Black canvas
        print(f"Canvas set to {width}x{height}")

    def change_brush_color(self, color):
        self.brush_color = color
        print(f"Brush color changed to {color}")

    def draw_point(self, x, y):
        if self.canvas is not None:
            cv2.circle(self.canvas, (x, y), radius=5, color=self.brush_color, thickness=-1)
            print(f"Drew point at ({x},{y})")

    def display_canvas(self):
        if self.canvas is not None:
            cv2.imshow("RoboPainter Canvas", self.canvas)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        else:
            print("No canvas to display.")
