import os

import requests
from colorama import Fore, Style

import formats, constants, utils

response = requests.get(constants.API_URL).json()

def main() -> None:

    os.system("clear")

    codes = utils.filt(response)
    codes.append("UZS")

    print()
    available_exchanges = ", ".join(codes)

    print( Style.DIM, Fore.CYAN, constants.WELLCOME_MSG, Style.RESET_ALL, sep="", end="\n\n")
    print(
        Fore.YELLOW,
        formats.AVAILABLE_EXCHANGES_MSG.format(available_exchanges=available_exchanges),
        Style.RESET_ALL,
        sep="",
    )

    while True:
        print()
        amount = input(constants.AMOUNT_REQUEST_MSG)

        if amount == "-1":
            print(
                Fore.RED,
                constants.STOP_MSG,
                Fore.RESET,
                sep=""
            )
            exit()
        
        try:
            amount = round(abs(float(amount)), 2)

            from_code = input(constants.CONVERSION_FROM_MSG).upper()
            to_code = input(constants.CONVERSION_TO_MSG).upper()

            if from_code in codes and to_code in codes:
                
                res = utils.converter(
                    from_code=from_code,
                    to_code=to_code,
                    amount=amount,
                    list_of_currencies=response
                )

                res = utils.format_num(res)
                amount = utils.format_num(amount)

                print("\n",
                    Style.BRIGHT,
                    Fore.GREEN,
                    formats.RESULT_MSG.format(
                        from_amount=amount,
                        from_code=from_code,
                        to_amount=res,
                        to_code=to_code
                    ),
                    Style.RESET_ALL,
                    sep=""
                )

            else:
                print(
                    Fore.RED, 
                    constants.ERROR_CODE_MSG, 
                    Fore.RESET,
                    sep=""
                )  
                  
        except ValueError:
            print(Fore.RED, constants.ERROR_AMOUNT_MSG, Fore.RESET)



if __name__ == "__main__":
    main()