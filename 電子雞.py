#回合目前只能做一件事
#更多顏文字
import random,webbrowser

# 類別專區 ------------------------------------------------------------------------
class Condition():#寵物狀態
    def __init__(self,名字,飽足,好感,衛生,體脂,摳摳,):
        self.名字 = 名字
        self.飽足 = 飽足
        self.好感 = 好感
        self.衛生 = 衛生
        self.體脂 = 體脂
        self.摳摳 = 摳摳
        
    def list_Condition(self): #狀態顯示
        print('吾乃',self.名字+
              '\nFood   ：'+str(self.飽足)+'%'+
              '\nMood   ：'+str(self.好感)+'%'+
              '\nHygiene：'+str(self.衛生)+'%'+
              '\nFat    ：'+str(self.體脂)+'%'+
              '\nMoney  ：'+str(self.摳摳)+'$')
        
    def 改名(self,new_name): #改名吃免錢鮭魚
        self.名字 = new_name +'鮭魚'
        print('好耶  吃免錢鮭魚囉 ✧٩(ˊωˋ*)و✧')
        input()

    def 端火鍋(self):
        webbrowser.open('https://www.youtube.com/watch?v=072tU1tamd0')


        
class Food(): #食物     ★只有火鍋跟鮭魚，我的豆花30塊
    food_list={}
    def __init__(self,選號,名字,價錢,飽足,脂肪):#營養標示
        self.選號 = 選號
        self.名字 = 名字
        self.價錢 = 價錢
        self.飽足 = 飽足
        self.脂肪 = 脂肪
        Food.food_list[self.選號] = [self.名字,self.價錢,self.飽足,self.脂肪]
                                     #缺點是改動要改選單而非屬性

    @classmethod
    def list_選項(cls): #列出選單
        
        print('要吃啥？')
        for 選號,food in Food.food_list.items():
            print(選號+'.',food[0],
                  '\n ','價格： '+str(food[1])+'$',
                  '\n ','飽足： +'+str(food[2]),
                  '\n ','脂肪： +'+str(food[3]),'\n')
        while 1:
            try:
                EF = input('輸入選號：')
                
                if Food.food_list.get(EF) == None:
                    raise list_Exception()
            except list_Exception:  
                print('\n  沒有',EF,'這個選項呦\n    再試一次吧')
            except:
                print('\n  輸入錯誤\n    再試一次吧')
            else:
                eat_food(EF)#在下面函式專區
                break



        

class Move():#動作選項
    list_move = {} 
    def __init__(self,選號,movement):
        self.選號 = 選號
        self.movement = movement
        Move.list_move[選號] = movement #產生物件順便產生選單
                                             
        
    @classmethod 
    def run_move(cls,choise): #執行動作
        if Move.list_move[choise] =='吃飯': #列食物 #選食物
            Food.list_選項()#在上面

            
        elif Move.list_move[choise] =='摸摸':
            #加好感
            if random.randint(0,1):
                pet.好感+=10
                print('(´,,•ω•,,)♡\n 好感+10')
                input('zZZ')
            else:
                pet.好感-=5
                print('摸三小(／‵Д′)／~ ╧╧\n好感-5')
                input('zZZ')
            
        elif Move.list_move[choise] =='洗澡':
            #加衛生
            Response.select('洗澡')
            
        elif Move.list_move[choise] =='運動':
            #減體脂
            Response.select('運動')
            
        elif Move.list_move[choise] =='兼差端火鍋':
            #40%會釣魚
            #賺錢
            Response.select('兼差端火鍋')
            if random.randrange(1,101)>60:
                pet.端火鍋()
            
        elif Move.list_move[choise] =='改名':
            while 1:
                try:
                    new_N = input('新名字是  ')
                    if len(new_N) ==0:
                        raise list_Exception()
                except list_Exception:  
                    print('\n  key something')
                except:
                    print('\n  輸入錯誤\n    再試一次吧')
                else:
                    pet.改名(new_N)
                    break
            
        else:
            pet.端火鍋()
        
    @classmethod 
    def list_選項(cls): #列出選單
        for 選號,movement in Move.list_move.items():
            print(選號,movement)



class list_Exception(Exception): #亂選BUG
    def __init__(self):
        super().__init__(self)


class Response():
    list_回饋 = {}
    def __init__(self,move,回應,狀態組): #{move:[ [回應...],[狀態組...] ],...}
        self.move = move #key                             #狀態組=[狀態,...]
        self.回應   = 回應 #value #用串列  #一個回應對應一組狀態
        self.狀態組 = 狀態組 #狀態變化值 #用串列套串列 #all component
        Response.list_回饋[move] = [回應,狀態組]
        
    @classmethod
    def select(cls,move): #隨機事件 #狀態變化及印出
        n = random.randrange(len(Response.list_回饋[move][0]))
        print(Response.list_回饋[move][0][n])
        pet.飽足 += Response.list_回饋[move][1][n][0]
        pet.好感 += Response.list_回饋[move][1][n][1]
        pet.衛生 += Response.list_回饋[move][1][n][2]
        pet.體脂 += Response.list_回饋[move][1][n][3]
        pet.摳摳 += Response.list_回饋[move][1][n][4]
        
        if Response.list_回饋[move][1][n][0]>0:
            print('飽足 +',Response.list_回饋[move][1][n][0])
        elif Response.list_回饋[move][1][n][0]<0:
            print('飽足 ',Response.list_回饋[move][1][n][0])
            
        if Response.list_回饋[move][1][n][1]>0:
            print('好感 +',Response.list_回饋[move][1][n][1])
        elif Response.list_回饋[move][1][n][1]<0:
            print('好感 ',Response.list_回饋[move][1][n][1])
            
        if Response.list_回饋[move][1][n][2]>0:
            print('衛生 +',Response.list_回饋[move][1][n][2])
        elif Response.list_回饋[move][1][n][2]<0:
            print('衛生 ',Response.list_回饋[move][1][n][2])

        if Response.list_回饋[move][1][n][3]>0:
            print('體脂 +',Response.list_回饋[move][1][n][3])
        elif Response.list_回饋[move][1][n][3]<0:
            print('體脂 ',Response.list_回饋[move][1][n][3])

        if Response.list_回饋[move][1][n][4]>0:
            print('摳摳 +',Response.list_回饋[move][1][n][4])
        elif Response.list_回饋[move][1][n][4]<0:
            print('摳摳 ',Response.list_回饋[move][1][n][4])

        input('\nzZZ')
            

# 函式專區 ------------------------------------------------------------------------
def eat_food(選號): #吃食物
    if  pet.摳摳-Food.food_list[選號][1] < 0:
        print('錢不夠  去賺錢')
        input('press enter to continue')
    else :#要顯示加多少
        pet.摳摳 -= Food.food_list[選號][1]
        pet.飽足 += Food.food_list[選號][2]
        pet.體脂 += Food.food_list[選號][3]
        print('吃飽睡 睡飽吃 _(:3 」∠ )_')
        input('zZZ')



# 物件專區 ------------------------------------------------------------------------
吃飯 = Move('1','吃飯')##接選食物
摸摸 = Move('2','摸摸')#加好感
洗澡 = Move('3','洗澡')#加衛生
運動 = Move('4','運動')#減體脂
端火鍋 = Move('5','兼差端火鍋')#加摳摳
改名 = Move('6','改名')


火鍋 = Food('1','火鍋',100,100,15)
鮭魚 = Food('2','鮭魚',50,50,5)
豆花 = Food('3','豆花',30,10,1)


#[飽足,好感,衛生,體脂,摳摳]
洗洗 = Response('洗澡',['主人，要一起洗嗎  (*ˇωˇ*人)~♥','洗香香～(*´∀`)']
              ,[[0,50,100,0,0],[0,0,100,0,0]])
運動 = Response('運動',['周X隆：年紀到了都是90公斤啦','早八體育 ｡･ﾟ･(ﾉД`)ヽ(ﾟДﾟ )'],
                [[-10,+5,0,10,0],[0,-20,-10,-10,0]])
火鍋 = Response('兼差端火鍋',['阿一代一代一代  (ﾟд⊙)','我就社畜 _(´ཀ`」 ∠)_ '],
                [[0,0,0,0,200],[0,-10,0,0,100]])


# 遊戲開始 ------------------------------------------------------------------------
print('             GAME BY PYTHON\n\n')
print('                MADE BY')
print('        張凱翔','陳允泓','羅道筠\n\n')
print('                WARNING\n')
print('    遊戲內容純屬虛構  若有雷同純屬巧合\n')
print('    遊戲內容若有釣魚成分絕無營利之意圖\n')
print('             未滿18歲者請勿遊玩')
print(' 若遊戲過程中遭遇不測  製作團隊一蓋不負責\n\n')
print('='*50)

while 1:
    pet = Condition(input('幫你的寵物取個名字吧   '),100,100,100,50,100)#寵物取名、出生

    print('你確定要叫',pet.名字,'嗎？')
    while 1:
        print('  1. Yes','\n  2. No')
        確定名字 = input()
        if 確定名字 == '1':
            break
        elif 確定名字 == '2':
            break
        else :
            print('就問你Yes or No  (ﾒ ﾟ皿ﾟ)ﾒ')
    if 確定名字 == '1':
        break

print('-'*50)  #分隔線

print('Game Start','\n出世了',pet.名字,'_(:△」∠)_')


day = 0 #回合數

while 1:
    day += 1
    #狀態變化
    if day != 1:
        x飽足 = random.randrange(21)
        x好感 = random.randrange(-20,21)
        x衛生 = random.randrange(21)
    
        pet.飽足 -= x飽足 
        pet.好感 += x好感
        pet.衛生 -= x衛生
        pet.體脂 += 1
        if x好感<0:
            print('飽足 -',x飽足,'\n'+
                  '好感 ',x好感,'\n'+
                  '衛生 -',x衛生,'\n'+
                  '體脂 +1',sep='')
        else:
            print('飽足 -',x飽足,'\n'+
                  '好感 +',x好感,'\n'+
                  '衛生 -',x衛生,'\n'+
                  '體脂 +1',sep='')

    print('')
    print('《 Day',str(day)+' 》')                #print回和數
    
    if pet.名字.find('鮭魚')+1:                   #免錢鮭魚判定
        Food.food_list[鮭魚.選號][1] = 0
        Food.food_list[鮭魚.選號][2] = 100
    else:
        Food.food_list[鮭魚.選號][1] = 50
        Food.food_list[鮭魚.選號][2] = 50



        
    if pet.飽足>100:    #限制最大最小值
        pet.飽足 = 100                  #錢沒有上限 下限在食物那
    if pet.好感>100:
        pet.好感 = 100
    if pet.衛生>100:
        pet.衛生 = 100
    if pet.體脂< 0:
        pet.體脂 = 0

    pet.list_Condition()  #狀態欄
    
    if pet.飽足<= 0 or pet.好感<= 0 or pet.衛生<= 0 or pet.體脂>= 100: #game over判定
        pet.端火鍋()
        break

            
    print('-'*30) #回合分隔線
    print('今晚我想來點：')
    Move.list_選項()
    while 1:
        try:  #用try加字典的get  debug
            choise = input('輸入選號：')             
            if Move.list_move.get(choise) == None:      
                raise list_Exception()      
        except list_Exception:  
            print('\n  沒有',choise,'這個選項呦\n    再試一次吧')
        except:
            print('\n  輸入錯誤\n    再試一次吧')
        else:
            print('') #空一行
            Move.run_move(choise) #進行所選動作
            print('='*50)  #回合分隔線
            break


print('\n啊一代一代一代\n','GAME OVER')
input()
