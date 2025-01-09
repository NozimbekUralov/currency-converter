API_URL = "https://nbu.uz/uz/exchange-rates/json"

class AVAILABLE_EXCHANGES:
    UZS = "UZS"
    USD = "USD"
    EUR = "EUR"
    KZT = "KZT"
    RUB = "RUB"
    CHF = "CHF"
    GBP = "GBP"
    JPY = "JPY"

AVAILABLE_EXCHANGES_MSG = "Mavjud valyutalar: {available_exchanges}."

WELLCOME_MSG = "Currency Converter dasturiga xush kelibsiz!"

AMOUNT_REQUEST_MSG = "Miqdorni kiriting: "

CONVERSION_FROM_MSG = f"Qaysi valyutadan konvertatsiya qilmoqchisiz. (masalan {AVAILABLE_EXCHANGES.USD}) "
CONVERSION_TO_MSG = f"Qaysi valyutaga konvertatsiya qilmoqchisiz. (masalan {AVAILABLE_EXCHANGES.UZS}) "

ERROR_AMOUNT_MSG = "Invalid amount."
ERROR_CODE_MSG = "Invalid currency codes."