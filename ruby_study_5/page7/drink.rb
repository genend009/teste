require "./menu"

class Drink < Menu
  attr_accessor :amount
  
  # infoメソッドを定義してください
  def info
  return "#{self.name} #{self.price}円(#{self.amount}mL)"
  end
end
