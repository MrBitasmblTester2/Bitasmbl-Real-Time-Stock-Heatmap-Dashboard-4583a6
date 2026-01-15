async def stream_updates():
    while True:
        yield {"symbol": "AAPL", "price": 0.0}
