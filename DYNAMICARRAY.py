class ResizableArray:
    def __init__(self):
        self.count = 0               # Number of elements currently in the array
        self.capacity = 4            # Start with a small capacity
        self.storage = [None] * self.capacity  # Initial storage with 'None'

    def _resize(self, new_capacity):
        """Resize the internal storage to the new capacity."""
        if new_capacity <= 0:
            new_capacity = 1  # Ensuring that the array never shrinks below 1 capacity
        new_storage = [None] * new_capacity
        for i in range(self.count):
            new_storage[i] = self.storage[i]
        self.storage = new_storage
        self.capacity = new_capacity

    def add(self, element):
        """Add an element to the array, resizing if necessary."""
        if self.count == self.capacity:
            # Double the size when full
            self._resize(self.capacity * 2)
        self.storage[self.count] = element
        self.count += 1

    def get(self, index):
        """Retrieve the element at the given index."""
        if 0 <= index < self.count:
            return self.storage[index]
        raise IndexError("Index out of range")

    def update(self, index, element):
        """Update an element at a specific index."""
        if 0 <= index < self.count:
            self.storage[index] = element
        else:
            raise IndexError("Index out of range")

    def delete_last(self):
        """Delete the last element from the array."""
        if self.count == 0:
            raise IndexError("Cannot delete from an empty array")
        
        self.count -= 1
        
        # Shrink array if it becomes too sparse
        if self.count <= self.capacity // 4 and self.capacity > 4:
            self._resize(self.capacity // 2)

    def is_empty(self):
        """Check if the array is empty."""
        return self.count == 0

    def size(self):
        """Return the number of elements in the array."""
        return self.count

    def clear(self):
        """Clear the array."""
        self.count = 0
        self._resize(4)  # Reset capacity to initial size of 4

    def __str__(self):
        """Return a string representation of the array."""
        return f"[{', '.join(map(str, self.storage[:self.count]))}]"

# Test cases
if __name__ == "__main__":
    # Initialize array
    resizable_array = ResizableArray()
    print("Initial array:", resizable_array)

    # Add elements
    resizable_array.add(10)
    resizable_array.add(20)
    resizable_array.add(30)
    resizable_array.add(40)
    print("Array after adding 10, 20, 30, 40:", resizable_array)

    # Access elements
    print("Element at index 0:", resizable_array.get(0))
    print("Element at index 2:", resizable_array.get(2))
    print("Element at index 3:", resizable_array.get(3))

    # Update an element
    resizable_array.update(1, 50)
    print("Array after updating index 1 to 50:", resizable_array)

    # Add more elements to trigger resizing
    resizable_array.add(60)
    resizable_array.add(70)
    print("Array after adding 60, 70:", resizable_array)

    # Delete elements
    resizable_array.delete_last()
    print("Array after deleting the last element:", resizable_array)
    resizable_array.delete_last()
    print("Array after deleting another element:", resizable_array)

    # Check if array is empty
    print("Is the array empty?", resizable_array.is_empty())

    # Clear the array
    resizable_array.clear()
    print("Array after clearing:", resizable_array)

    # Final state of the array
    print("Final array:", resizable_array)
