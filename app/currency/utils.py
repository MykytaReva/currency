from decimal import Decimal

def to_decimal(value: str, precision: int = 2) -> Decimal:

    return round(Decimal(value), precision)
