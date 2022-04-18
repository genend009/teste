require "./menu"

class Food < Menu
  attr_accessor :calorie
  
  # infoメソッドを定義してください
  def info
  return "#{self.name} #{self.price}円(#{self.calorie}kcal)"
  end
end
