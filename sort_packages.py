def sort(width, height, length, mass):
    """
    Classifies the package into one of the following stacks:
    - "STANDARD": for packages that are neither bulky nor heavy
    - "SPECIAL": for packages that are either bulky or heavy
    - "REJECTED": for packages that are both bulky and heavy

    Parameters:
    - width: The width of the package in cm.
    - height: The height of the package in cm.
    - length: The length of the package in cm.
    - mass (float): The mass of the package in kgs.

    Returns:
    - str: The stack classification ("STANDARD", "SPECIAL", "REJECTED")
    """
    
    # Calculate volume
    volume = width * height * length
    
    # Determine if the package is bulky
    is_bulky = volume >= 1000000 or width >= 150 or height >= 150 or length >= 150
    
    # Determine if the package is heavy
    is_heavy = mass >= 20
    
    # Decide stack based on the conditions
    if is_bulky and is_heavy:
        return "REJECTED"
    elif is_bulky or is_heavy:
        return "SPECIAL"
    else:
        return "STANDARD"
