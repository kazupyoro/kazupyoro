# class
class Item:
    def __init__(self,p_id,p_name, p_price,p_purchase_price):
        self.p_id = p_id
        self.p_name = p_name
        self.p_price = p_price
        self.p_purchase_price = p_purchase_price

    def cost_rate(self):
        rate = self.p_purchase_price/self.p_price
        return rate

Item_1 = Item("A0001","半袖クールTシャツ",5000,2250)
x = Item_1.p_name + "原価率："
s1_rate = Item_1.cost_rate()
print(x,s1_cost)