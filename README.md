# Thoughtful---Coding-Challenge
Technical screening for Thoughtful.ai
A Python solution for Thoughtful Automation's robotic package sorting challenge.
Overview
This system sorts packages into three stacks based on their physical dimensions and mass:

STANDARD: Normal packages (not bulky or heavy)
SPECIAL: Packages that are either bulky or heavy (require special handling)
REJECTED: Packages that are both bulky and heavy (cannot be processed)

Sorting Rules
Bulky Package
A package is considered bulky if:

Its volume (Width × Height × Length) ≥ 1,000,000 cm³, OR
Any single dimension (width, height, or length) ≥ 150 cm

Heavy Package
A package is considered heavy if:

Its mass ≥ 20 kg

Stack Assignment

REJECTED: Both bulky AND heavy
SPECIAL: Either bulky OR heavy (but not both)
STANDARD: Neither bulky nor heavy

Installation
No external dependencies required. Uses Python 3.6+.

Basic Usage
pythonfrom package_sorter import sort

# Sort a package
result = sort(width=100, height=50, length=50, mass=15)
print(result)  # Output: "STANDARD"

# Bulky package (dimension >= 150cm)
result = sort(width=150, height=50, length=50, mass=10)
print(result)  # Output: "SPECIAL"

# Heavy package
result = sort(width=50, height=50, length=50, mass=25)
print(result)  # Output: "SPECIAL"

# Rejected package (both bulky and heavy)
result = sort(width=150, height=100, length=100, mass=25)
print(result)  # Output: "REJECTED"

## Algorithm Complexity

- **Time Complexity**: O(1) - constant time operations
- **Space Complexity**: O(1) - constant space usage

## Example Output

```
Example Package Sorting:
--------------------------------------------------
Small standard package:
  Dimensions: 50x50x50 cm, Mass: 10 kg
  Result: STANDARD

Large volume but not bulky:
  Dimensions: 100x100x100 cm, Mass: 15 kg
  Result: SPECIAL

One dimension >= 150cm (bulky):
  Dimensions: 200x50x50 cm, Mass: 10 kg
  Result: SPECIAL

Heavy package:
  Dimensions: 100x100x100 cm, Mass: 25 kg
  Result: SPECIAL

Both bulky and heavy:
  Dimensions: 150x150x150 cm, Mass: 25 kg
  Result: REJECTED

Just under heavy threshold:
  Dimensions: 100x100x100 cm, Mass: 19.9 kg
  Result: SPECIAL

Just under bulky threshold:
  Dimensions: 149x149x149 cm, Mass: 10 kg
  Result: STANDARD
```

## Design Decisions

1. **Simple Logic Flow**: The function follows a clear decision tree that matches the business rules
2. **Early Validation**: Input validation happens first to fail fast on invalid data
3. **Clear Boolean Logic**: Separated bulky/heavy checks for readability
4. **Defensive Programming**: Validates all inputs to prevent unexpected behavior
5. **Comprehensive Testing**: Edge cases and thresholds thoroughly tested

## Author

Ryan Rousch  
Senior Software Engineer
