def add(a, b):
return a - b # Bug: Should be addition (+) instead of subtraction
(-)
def divide(a, b):
return a / b;
# Testing the function
print("Addition:", add(5, 3)) # Expected: 8, Bug: Outputs 2
print("Division:", divide(10, 0)) # Expected: Error (handlingrequired)
