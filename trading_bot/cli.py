import argparse
from bot.client import get_client
from bot.orders import place_order
from bot.validators import validate_order
from bot.logging_config import setup_logger

def main():
    parser = argparse.ArgumentParser(description="Binance Futures Trading Bot (Testnet)")
    parser.add_argument("--symbol", required=True, help="Trading pair, e.g., BTCUSDT")
    parser.add_argument("--side", required=True, choices=["BUY", "SELL"])
    parser.add_argument("--order_type", required=True, choices=["MARKET", "LIMIT"])
    parser.add_argument("--quantity", type=float, required=True)
    parser.add_argument("--price", type=float, help="Required for LIMIT orders")

    args = parser.parse_args()
    logger = setup_logger()

    try:
        validate_order(args.symbol, args.side, args.order_type, args.quantity, args.price)
        client = get_client()
        response = place_order(client, logger, args.symbol, args.side, args.order_type, args.quantity, args.price)
        print("✅ Order placed successfully!")
        print(f"OrderId: {response['orderId']}, Status: {response['status']}, ExecutedQty: {response.get('executedQty')}, AvgPrice: {response.get('avgPrice')}")
    except Exception as e:
        print(f"❌ Failed: {e}")

if __name__ == "__main__":
    main()