
def find_available(list_of_currencies: list[dict]) -> list:
    return [obj["code"] for obj in list_of_currencies if obj["nbu_buy_price"]]

def format_num(num: float) -> str:
    num = f"{num:.2f}"
    num = list(num)
    num.reverse()
    addtion = 0
    for i in range(6, len(num), 3):
        num.insert(i+addtion, ",")
        addtion +=1
        

    num.reverse()

    return "".join(num)

def converter(
        from_code: str, 
        to_code: str, 
        amount: float,
        list_of_currencies: list[dict]
    ) -> float | None:
    
    uzs = "UZS"
    if from_code != uzs and to_code != uzs:
        
        for obj in list_of_currencies:

            if from_code == obj["code"]:
                from_obj = obj
            elif to_code == obj["code"]:
                to_obj = obj

        from_nbu_buy_price = float(from_obj["nbu_buy_price"])
        to_nbu_buy_price = float(to_obj["nbu_buy_price"])
    
        uzb_sum = from_nbu_buy_price * amount
        res_sum = uzb_sum / to_nbu_buy_price

        return res_sum
    
    found_obj = lambda from_code, to_code: [obj for obj in list_of_currencies if from_code == obj["code"] or to_code == obj["code"]][0]
    price = float(found_obj(from_code, to_code)["nbu_buy_price"])
    
    if to_code == uzs:
        return  amount * price
    else:
        return  amount / price