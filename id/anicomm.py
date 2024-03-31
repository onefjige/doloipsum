def intToDecimal(amount, decimals):
    """Converts an integer to a decimal with the specified number of decimals.

    Args:
        amount: The integer to convert.
        decimals: The number of decimal places to use.

    Returns:
        A decimal with the specified number of decimal places.
    """

    if decimals < 0:
        raise ValueError("Decimals must be non-negative.")

    factor = 10 ** decimals
    return amount / factor
