# HINDI PA TAPOS!!
# ok



class Oil:
  def __init__(self, type: str, average_price: int, main_ingredient: str, appearance: str):
    self.type = type
    self.average_price = average_price
    self.main_ingredient = main_ingredient
    self.__appearance = appearance

  def buy(self, brand: str):
    return f"You succesfully bought {self.type} oil for {self.average_price}."

  def pour(self, amount_in_liters: int):
    if amount_in_liters > 0:
      print(f"You poured {amount_in_liters} liters of {self.type} oil.")
    else:
      print(f"No more oil left to pour.")

  def read_desc(self):
    return f"Type: {self.type}, Average Price: {self.average_price}, Main Ingredient: {self.main_ingredient}, Appearance: {self.__appearance}"

  def use_discount_coupon(self, discount_amount: int):
    if discount_amount > 0 and discount_amount < self.average_price:
      self.average_price = self.average_price - discount_amount
      print(f"Successfully used coupon. Price is now {self.average_price}.")
    else:
      print("Can't use coupon: Price is lower than the discount amount.")




Oil1 = Oil(type="Canola", average_price=150, main_ingredient="Rapeseed", appearance="Yellow")
Oil2 = Oil(type="Coconut", average_price=265, main_ingredient="Coconut", appearance="Transparent")




print(f"Volume: {Oil1.read_desc()}")
print(f"Volume: {Oil2.read_desc()}")
