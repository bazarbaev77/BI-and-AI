from __future__ import annotations
from math import sqrt

class Vector:
    def __init__(self, x: float, y: float, z: float = 0):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return f"Vector({self.x}, {self.y}, {self.z})"

    def __bool__(self):
        return not (self.x == 0 and self.y == 0 and self.z == 0)

    def __len__(self):
        return 3 

    def __getitem__(self, index: int):
        if index == 0:
            return self.x
        elif index == 1:
            return self.y
        elif index == 2:
            return self.z
        else:
            raise IndexError("Index out of range")

    def __setitem__(self, index: int, value: float):
        if index == 0:
            self.x = value
        elif index == 1:
            self.y = value
        elif index == 2:
            self.z = value
        else:
            raise IndexError("Index out of range")

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x * other.x, self.y * other.y, self.z * other.z)
        else:
            return Vector(self.x * other, self.y * other, self.z * other)

    def __truediv__(self, scalar: float) -> Vector:
        return Vector(self.x / scalar, self.y / scalar, self.z / scalar)

    def __eq__(self, other: Vector) -> bool:
        return self.x == other.x and self.y == other.y and self.z == other.z

    def __neg__(self) -> Vector:
        return Vector(-self.x, -self.y, -self.z)

    def __abs__(self) -> float:
        return sqrt(self.x**2 + self.y**2 + self.z**2)