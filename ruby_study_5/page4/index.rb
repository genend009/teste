require "./food"
require "./drink"

food1 = Food.new(name: "ピザ", price: 800)
drink1 = Drink.new(name: "コーラ", price: 300)

# food1.calorieに「700」を代入してください
food1.calorie = 700

# food1.calorieを出力してください
puts food1.calorie

# drink1.amountに「500」を代入してください
drink1.amount = 500

# drink1.amountを出力してください
puts drink1.amount
