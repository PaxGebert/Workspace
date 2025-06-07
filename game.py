class Entity:
    def __init__(self, x, y, width=1, height=1):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def move(self, dx, dy, bounds=None):
        """Move the entity by dx and dy. If bounds is provided as
        (max_x, max_y), the entity's position is clamped so that it
        remains within [0, max_x - width] and [0, max_y - height]."""
        new_x = self.x + dx
        new_y = self.y + dy
        if bounds:
            max_x, max_y = bounds
            new_x = max(0, min(new_x, max_x - self.width))
            new_y = max(0, min(new_y, max_y - self.height))
        self.x = new_x
        self.y = new_y

    def collides_with(self, other):
        """Return True if this entity collides with another."""
        return not (
            self.x + self.width <= other.x or
            self.x >= other.x + other.width or
            self.y + self.height <= other.y or
            self.y >= other.y + other.height
        )
