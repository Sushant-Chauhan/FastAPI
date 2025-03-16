from fastapi import FastAPI
from enum import Enum
app = FastAPI()

class AvailableCuisines(str, Enum):
    indian = "indian"
    italian = "italian"
    chinese = "chinese"
    mexican = "mexican"
    japanese = "japanese"

food_items = {
    "indian": ["Samosa", "Dosa-Idli", "Paneer Tikka"],
    "italian": ["Pizza", "Pasta", "Lasagna"],
    "chinese": ["Manchurian", "Fried Rice", "Noodles"],
    "mexican": ["Tacos", "Burritos", "Enchiladas"],
    "japanese": ["Sushi", "Ramen", "Tempura"]
}

coupon_codes = {
    1: "10% off",
    2: "20% off",
    3: "30% off"
}

@app.get("/")
def home():
    return "Welcome to the Food Delivery App!"

@app.get("/about")      
def about():
    return {"data":'about page'}

@app.get("/get_items/{cuisine}")
async def get_items(cuisine: AvailableCuisines ): 
    return food_items.get(cuisine, "Cuisine not found")

@app.get("/get_coupon/{coupon}")
async def get_coupon(coupon: int):
    return {'discount_amount ' : coupon_codes.get(coupon, "Coupon not found")}