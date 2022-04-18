from collections import Counter
import random
# 試行回数
num_iterations = 100000
# カードを引く枚数
cardsseen = 8  #後手3ターン目
card2turn = 10 #後手3ターン目
cardsseen3 = 9 #後手2ターン目
# デッキリスト
decklist = {
    'W':0, # 白のカード
    'U':4, # 青のカード
    'B':4, # 黒のカード
    'R':9, # 赤のカード
    'G':12, # 緑のカード
    'RG':3,# 赤緑のカード
    'UB':3,# 青黒のカード
    'UG':1,# 青緑のカード
    'UBG':4,# 青黒緑のカード
    'X':0, # 無色のカード 
    }
# デッキを作成する
deck = []
for card in decklist.keys():
    deck += [card] * decklist[card]

#20200326編集ここまで
 
countW = 0
countU = 0
countB = 0 
countWU =0
countUB =0
countWB =0
countWUB=0
countm = 0
countv = 0
countvm = 0
count_four_plus = 0
count_four_plus2 = 0
count_four_plus3 = 0
countU2 = 0
countU3 = 0

d_need2 = 1  
# 必要なカード枚数
need_land = 5 # 土地は最低でも5枚必要
c_need = 2 # 土地色その1は2枚必要
d_need = 2 # 土地色その2は2枚必要
e_need = 2 #土地3は2枚必要
m_need = 1 # 全体除去は1枚必要
v_need = 1 #侮辱は1枚必要
for _ in range(num_iterations):
    # cards_seen枚のドローカードの中身(12枚ドロー(5ターン目))
    draw = Counter(random.sample(deck, cardsseen))
    # CCDD の色と必要土地枚数が揃うかどうか、引けたらカウントを増やす
    c_color_keep = c_need <= (draw['C'] + draw['CD'] + draw['CE'])
    d_color_keep = d_need <= (draw['D'] + draw['CD'] + draw['DE'])
    e_color_keep = e_need <= (draw['E'] + draw['CE'] + draw['DE'])
    countW  += (c_color_keep)
    countU  += (d_color_keep)
    countB  += (e_color_keep)
    countWU += (c_color_keep and d_color_keep)
    countUB += (d_color_keep and e_color_keep)
    countWB += (c_color_keep and e_color_keep)
    countWUB += (c_color_keep and d_color_keep and e_color_keep)
    
need_land2 = 3
for _ in range(num_iterations):
    # cards_seen2枚のドローカードの中身(3ターン目(10枚ドロー))
    draw = Counter(random.sample(deck, card2turn))
    # 必要な土地を引けてるかどうか、引けたらカウントを増やす
    land2 = draw['C'] + draw['D'] + draw['E'] + draw['CD'] + draw['CE'] + draw['DE'] + draw['X']
    land_keep2 = need_land2 <= land2
    count_four_plus2 += land_keep2
    # CCDD の色と必要土地枚数が揃うかどうか、引けたらカウントを増やす
    d_color_keep2 = d_need <= (draw['D'] + draw['CD'] + draw['DE'])
    countU2  += (d_color_keep2 and land_keep2)
    
need_land3 = 2
for _ in range(num_iterations):
    # cards_seen2枚のドローカードの中身(2ターン目(9枚ドロー))
    draw = Counter(random.sample(deck, cardsseen3))
    # 必要な土地を引けてるかどうか、引けたらカウントを増やす
    land3 = draw['C'] + draw['D'] + draw['E'] + draw['CD'] + draw['CE'] + draw['DE'] + draw['X']
    land_keep3 = need_land3 <= land3
    count_four_plus3 += land_keep3
    # CCDD の色と必要土地枚数が揃うかどうか、引けたらカウントを増やす
    d_color_keep3 = d_need2 <= (draw['D'] + draw['CD'] + draw['DE'])
    countU3  += (d_color_keep3 and land_keep3)
# デッキリストを出力
print('decklist:'+str(decklist))
# 各色を2枚構えられる確率
print('fraction of draws with W:\t' + str(round(countW / num_iterations,3)))
print('fraction of draws with U:\t' + str(round(countU / num_iterations,3)))
print('fraction of draws with B:\t' + str(round(countB / num_iterations,3)))
print('fraction of draws with WU:\t' + str(round(countWU / num_iterations,3)))
print('fraction of draws with UB:\t' + str(round(countUB / num_iterations,3)))
print('fraction of draws with WB:\t' + str(round(countWB / num_iterations,3)))
print('fraction of draws with WUB:\t' + str(round(countWUB / num_iterations,3)))
# 土地を5枚引く確率
print('5 if more lands:            \t' + str(round(count_four_plus / num_iterations,3)))
# 全体除去を打てる確率
print('Can Cast MD:                \t'+str(round(countm/num_iterations,3)))
#侮辱を打てる確率
print('Can Cast contempt:          \t'+str(round(countv/num_iterations,3)))
#侮辱または全体除去
print('Can Cast contempt or MD:     \t'+str(round(countvm/num_iterations,3)))
#土地が5枚揃ったときにCCDDFFが構えられる確率
print('WWUUBB giben 5 or more lands: \t' + str(round(countWUB / count_four_plus,3)))
#土地が3枚の時にDDが揃う確立
print('UU giben 3 or more lands: \t' + str(round(countU2 / num_iterations,3)))
#土地が2枚の時にDが揃う確立
print('U giben 2 or more lands: \t' + str(round(countU3 / num_iterations,3)))

