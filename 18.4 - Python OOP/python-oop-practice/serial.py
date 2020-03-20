"""Python serial number generator."""


class SerialGenerator:
    """Machine to create unique incrementing serial numbers.

    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start=0):
        """Make a new generator, starting at start."""
        self.start = start  # Keeps original start
        self.next = start   # Will increment from start

    def __repr__(self):
        """Shows representation"""
        return f"<SerialGenerator start={self.start} next={self.next}>"

    def generate(self):
        """First return is original start, then self.next increments"""
        self.next += 1  # Increment self.next
        # Returns self.next - 1 to make sure start number is returned first
        return self.next - 1

    def reset(self):
        """Reset count to original or new start"""
        self.next = self.start
