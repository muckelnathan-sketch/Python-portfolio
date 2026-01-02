def USD_EUR(USD:float, str_formated:bool=False) -> float:
    rate = 0.91
    if str_formated:
        return f"{USD*rate:.2f}"
    return USD*rate #return just the number
def USD_GBP(USD:float, str_formated:bool=False) -> float:
    rate = 0.79
    if str_formated:
        return f"{USD*rate:.2f}"
    return USD*rate
def USD_JPY(USD:float, str_formated:bool=False) -> float:
    rate = 141.0
    if str_formated:
        return f"{USD*rate:.2f}"
    return USD*rate
def converter(USD:float,rate:float, str_formatted:bool=True) -> float|str:
    return f"{(answer := USD*rate):.2f}" if str_formatted else answer