# HINDI PA TAPOS!!
# ok



class Oil:
  def __init__(self, type: string, average price: int, main ingredient/material: str, appearance: str):
    self.type = type: string
    self.average_price = average price: int
    self.main_ingredient = main ingredient/material: str
    self.__appearance = appearance: str

  def buy(self, brand: str):
    return f"You succesfully bought {self.type} oil for {self.average_price}."

  def pour(self, amount_in_liters: int):
    if amount_in_liters > 0:
      print(f"You poured {amount_in_liters} liters of {self.type} oil.")
    else:
      print(f"No more oil left to pour.")

  def read_amount_volume(self, amount_in_milliliters: int):
    return f"This {self.type} oil bottle is {amount_in_milliliters} mL."

  def use_discount_coupon(self, discount_amount: int):
    if discount_amount > 0 and discount_amount < self.average_price:
      self.average_price = self.average_price - discount_amount
      print(f"Successfully used coupon. Price is now {self.average_price}.")
    else:
      print("Can't use coupon: Price is lower than the discount amount.")

