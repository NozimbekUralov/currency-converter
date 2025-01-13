import json
from datetime import date

import constants

import requests

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
        amount: float,
        list_of_currencies: list[dict],
        to_code: str = "UZS", 
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
    

def load_data():
    try: 
        with open(constants.DB_URL, "r") as db:
            
            db = json.load(fp=db)

            current_date = date.today()
            saved_date = db["date"]["date"]
            
            if saved_date != str(current_date):
                return requests.get(constants.API_URL).json()
            else: 
                return db["response"]
            
    except FileNotFoundError:
        with open(constants.DB_URL, "w") as db :
            current_date = str(date.today())
            response = requests.get(constants.API_URL).json()
            db.write(
                json.dumps(
                    {
                        "date": {"date": current_date}, 
                        "response": response
                    }, 
                    indent=4
                )
            ) 
            exit()