# requireを使ってfood.rbとdrink.rbを読み込んでください
require "./food"
require "./drink"

# Foodクラスのインスタンスを生成して変数food1に代入してください
food1 = Food.new(name:"ピザ",price:800)

# food1に対してinfoメソッドを呼び出して戻り値を出力してください
puts food1.info

# Drinkクラスのインスタンスを生成して変数drink1に代入してください
drink1 = Drink.new(name:"コーラ",price:300)

# drink1に対してinfoメソッドを呼び出して戻り値を出力してください
puts drink1.info
