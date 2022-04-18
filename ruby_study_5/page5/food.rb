require "./menu"

class Food < Menu
  attr_accessor :calorie
  
  # calorie_infoメソッドを定義してください
  def calorie_info
    return "#{self.name}は#{self.calorie}kcalです"
  end
end
