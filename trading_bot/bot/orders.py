from binance.exceptions import BinanceAPIException, BinanceRequestException

def place_order(client, logger, symbol, side, order_type, quantity, price=None):
    try:
        params = {
            "symbol": symbol,
            "side": side,
            "type": order_type,
            "quantity": quantity
        }
        if order_type == "LIMIT":
            params["price"] = price
            params["timeInForce"] = "GTC"

        logger.info(f"Order Request: {params}")
        response = client.futures_create_order(**params)
        logger.info(f"Order Response: {response}")
        return response

    except (BinanceAPIException, BinanceRequestException) as e:
        logger.error(f"API Error: {e}")
        raise
    except Exception as e:
        logger.error(f"Unexpected Error: {e}")
        raise