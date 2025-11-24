"""
Package Sorting System for Thoughtful Automation
This coding challenge sorts packages into STANDARD, SPECIAL, or REJECTED stacks based on volume and mass.
"""

def sort(width: float, height: float, length: float, mass: float) -> str:
    """
    Sort packages based on their dimensions and mass.
    
    Args:
        width: Width in centimeters
        height: Height in centimeters
        length: Length in centimeters
        mass: Mass in kilograms
    
    Returns:
        str: Stack name - "STANDARD", "SPECIAL", or "REJECTED"
    
    Raises:
        ValueError: If any dimension or mass is negative
    """
    # Validate inputs
    if width < 0 or height < 0 or length < 0 or mass < 0:
        raise ValueError("Dimensions and mass must be non-negative")
    
    # Calculate volume
    volume = width * height * length
    
    # Determine if package is bulky
    isBulky = volume >= 1_000_000 or width >= 150 or height >= 150 or length >= 150
    
    # Determine if package is heavy
    isHeavy = mass >= 20
    
    # Dispatch to appropriate stack
    if isBulky and isHeavy:
        return "REJECTED"
    elif isBulky or isHeavy:
        return "SPECIAL"
    else:
        return "STANDARD"


if __name__ == "__main__":
    # Example usage
    print("Example Package Sorting:")
    print("-" * 50)
    
    test_cases = [
        (50, 50, 50, 10, "Small standard package"),
        (100, 100, 100, 15, "Bulky by volume (1,000,000 cm³)"),
        (200, 50, 50, 10, "Bulky by dimension (200 >= 150 cm)"),
        (50, 50, 50, 25, "Heavy package (25 kg)"),
        (150, 150, 150, 25, "Both bulky and heavy - REJECTED"),
        (100, 100, 100, 19.9, "Bulky but not heavy (19.9 kg)"),
        (99, 99, 99, 15, "Just under bulky threshold (970,299 cm³)"),
    ]
    
    for width, height, length, mass, description in test_cases:
        result = sort(width, height, length, mass)
        print(f"{description}:")
        print(f"  Dimensions: {width}x{height}x{length} cm, Mass: {mass} kg")
        print(f"  Result: {result}")
        print()