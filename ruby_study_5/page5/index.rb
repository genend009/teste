require "./food"
require "./drink"

food1 = Food.new(name: "ピザ", price: 800)
food1.calorie = 700

# food1に対してcalorie_infoメソッドを呼び出して戻り値を出力してください
puts food1.calorie_info

