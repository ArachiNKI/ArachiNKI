#ПРИМЕЧАНИЕ ИГРА НАПИСАНА НА ПИТОНЕ В VISUAL STUDIO CODE
    
from time import sleep
import random
from random import randint
global playerCash
global game
global playerSaitStavkiNaSport
playerSaitStavkiNaSport = 100
game = 0
playerCash = 0
print(f"Привет! Это Simulator! v2. \nВаш баланс: {playerCash} евро")

AppleVisionPro = 5000
ApplePhone = 500
AppleWatch = 100
while True:
    keff = randint(1,3)
    print("""
        1) Работать
        2) Идти в Магазин
        3) Выйти из Симулятора (Не рекомендуется!)
        4)играть на деньги!
    """)
    playerAnswer = input("Выберите одно из действий: ")
    if playerAnswer == '1':
        playerCash += 100
        for x in range(20):
            print(f'идет процес работы{x*5}%')
            sleep(0.32)
        print(f"""
Вы поработали на отлично! \nВаш баланс: {playerCash}
""")

    elif playerAnswer == '2':
        print(f"""
Вы пришли в магазин... Ваш баланс: {playerCash}
1). Купить Apple Vision Pro: {AppleVisionPro}
2). Купить Apple Phone: {ApplePhone}
3). Купить Apple Watch: {AppleWatch}
""")
        playerAnswerBuy = input("Выберите что хотите купить:")
        if playerAnswerBuy == '1':
            if playerCash < 5000:
                print("У вас нет столько денег!")
            else:
                print(f"Успешно! Оплата прошла! Ваш чек: {random.random()}")
                playerCash = playerCash- 5000
                print(f"Ваш баланс: {playerCash}")
        if playerAnswerBuy == '2':
             if playerCash < ApplePhone:
                print("У вас нет столько денег!")
            else:
                print(f"Успешно! Оплата прошла! Ваш чек: {random.random()}")
                playerCash = playerCash - 500
                print(f"Ваш баланс: {playerCash}")
                game += 2
        if playerAnswerBuy == '3':
            if playerCash < AppleWatch:
                print("У вас нет столько денег!")
            else:
                print(f"Успешно! Оплата прошла! Ваш чек: {random.random()}")
                playerCash = playerCash - 100
                print(f"Ваш баланс: {playerCash}")
    elif playerAnswer == "3":
        break
    elif playerAnswer == "4":
        if game < 1:
            print("для начала купите ApplePhone!")
        else:
            print(f"Вы попалпи в казино! Предупреждаем! если вы проиграете и не сможет отдать деньгм - мы вас продадим в рабство! Ваш баланс:{playerCash}")
            
            sleep(2)
            if keff == 1:
                print("Колесо показывает белый цвет, ультра биг поздравляю с победой!")
                playerCash *= 5
                print(f'Теперь ваш баланс: {playerCash}')
            elif keff == 2:
                print("Колесо показывает церный цвет! вы проиграли!")
                if playerCash < 100:
                    print("У вас не хватило денег! Мы забираем вас в рабство!")
                    break
                else:
                    playerCash = playerCash - 100
            elif keff == 3:
                print("О нет! Колесо показывает красный цвет! Мы забираем у вас все деньги! :D")
                playerCash -= playerCash
