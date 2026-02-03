def validate_order(symbol: str, side: str, order_type: str, quantity: float, price: float = None):
    if not symbol.endswith("USDT"):
        raise ValueError("Only USDT-M pairs are supported.")
    if side not in ["BUY", "SELL"]:
        raise ValueError("Side must be BUY or SELL.")
    if order_type not in ["MARKET", "LIMIT"]:
        raise ValueError("Order type must be MARKET or LIMIT.")
    if quantity <= 0:
        raise ValueError("Quantity must be greater than zero.")
    if order_type == "LIMIT" and (price is None or price <= 0):
        raise ValueError("Price must be provided and > 0 for LIMIT orders.")
    return True