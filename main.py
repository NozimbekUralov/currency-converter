import json, os

import requests
from colorama import Fore, Style

import formats, constants

response = requests.get(constants.API_URL)

def filt(l: list[dict]) -> list:
 return [obj["code"] for obj in l if obj["nbu_buy_price"] and obj["nbu_cell_price"] != ""]

def converter(from_code: str, to_code: str, amount: float) -> None:
    pass

def main() -> None:

    os.system("clear")
    codes = filt(response.json())
    print()
    available_exchanges = ", ".join(codes)

    print( Style.DIM, Fore.CYAN, constants.WELLCOME_MSG, Style.RESET_ALL, sep="", end="\n\n")
    print(
        Fore.YELLOW,
        constants.AVAILABLE_EXCHANGES_MSG.format(available_exchanges=available_exchanges),
        Style.RESET_ALL,
        sep="",
    )

    while True:
        print()
        amount = input(constants.AMOUNT_REQUEST_MSG)
        
        try:
            amount = float(amount)

            from_code = input(constants.CONVERSION_FROM_MSG)
            to_code = input(constants.CONVERSION_TO_MSG)
            
            if from_code and to_code in codes:
                pass 
            
            print(Fore.RED, constants.ERROR_CODE_MSG, Fore.RESET)
            
        except ValueError:
            print(Fore.RED, constants.ERROR_AMOUNT_MSG, Fore.RESET)



if __name__ == "__main__":
    main()