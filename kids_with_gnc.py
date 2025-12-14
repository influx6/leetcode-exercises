def solution(candles: list[int], extra_candles: int) -> List[bool]:
    max_candle = max(candles)
    return [extra_candles + candle >= max_candle for candle in candles]
