class Car:
    def __init__(self, license_plate, make, model, year):
        self.license_plate = license_plate
        self.make = make
        self.model = model
        self.year = year

class Node:
    def __init__(self, car):
        self.car = car
        self.left = None
        self.right = None

class CarInventory:
    def __init__(self):
        self.root = None

    def insert(self, car):
        self.root = self._insert_recursive(self.root, car)

    def _insert_recursive(self, node, car):
        if node is None:
            return Node(car)
        if car.license_plate < node.car.license_plate:
            node.left = self._insert_recursive(node.left, car)
        else:
            node.right = self._insert_recursive(node.right, car)
        return node

    def delete(self, license_plate):
        self.root = self._delete_recursive(self.root, license_plate)

    def _delete_recursive(self, node, license_plate):
        if node is None:
            return node
        if license_plate < node.car.license_plate:
            node.left = self._delete_recursive(node.left, license_plate)
        elif license_plate > node.car.license_plate:
            node.right = self._delete_recursive(node.right, license_plate)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            min_node = self._find_min(node.right)
            node.car = min_node.car
            node.right = self._delete_recursive(node.right, min_node.car.license_plate)
        return node

    def _find_min(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def search(self, license_plate):
        return self._search_recursive(self.root, license_plate)

    def _search_recursive(self, node, license_plate):
        if node is None or node.car.license_plate == license_plate:
            return node
        if license_plate < node.car.license_plate:
            return self._search_recursive(node.left, license_plate)
        return self._search_recursive(node.right, license_plate)

    def print_license_plates(self):
        self._inorder_traversal(self.root)

    def _inorder_traversal(self, node):
        if node:
            self._inorder_traversal(node.left)
            print(node.car.license_plate)
            self._inorder_traversal(node.right)

# Example usage
inventory = CarInventory()

# Insert cars
inventory.insert(Car("1234567", "Toyota", "Corolla", 2020))
inventory.insert(Car("7654321", "Honda", "Civic", 2019))
inventory.insert(Car("2468135", "Ford", "Focus", 2021))

# Print all license plates
print("All license plates:")
inventory.print_license_plates()

# Search for a car
search_result = inventory.search("7654321")
if search_result:
    print(f"\nFound car: {search_result.car.make} {search_result.car.model}")
else:
    print("\nCar not found")

# Delete a car
inventory.delete("2468135")

print("\nAfter deletion:")
inventory.print_license_plates()
