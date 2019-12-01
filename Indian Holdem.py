import random
flag = 0


class Player:
    def __init__(self, name):
        self.name = name
        self.chip = 40
        self.key1 = 0
        self.key2 = 0


red_card = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
blue_card = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def fightres(redc, bluec):
    if redc > bluec:
        return "R"
    elif redc == bluec:
        return "T"
    elif redc < bluec:
        return "B"


while True:
    random.shuffle(red_card)
    random.shuffle(blue_card)
    print("Hello, this is the INDIAL HOLDEM!")
    print("Please write your name!")
    name1 = input("Player1's name: ")
    name2 = input("Player2's name: ")

    redplayer = Player(name1)
    blueplayer = Player(name2)

    print("이 게임은 통신이 안되어서 상대방의 카드를 보는 것에 대한 암호화 과정이 필요합니다...")
    print("상대방의 카드는 암호를 통해 다음과 같이 구현됩니다.")
    print("Ex: 암호는 '2', '23'일 때 카드 '3'은 이러한 과정을 통해 암호로 보여드립니다. ")
    print("3*2+23 = 29")
    order = [redplayer, blueplayer]
    cardorder = [red_card, blue_card]
    redplayer.key1, redplayer.key2 = map(int, input('%s의 암호 두 개를 입력해주세요: ' % order[0].name).split(' '))

    for i in range(40):
        print("===============You can't see!=============")

    blueplayer.key1, blueplayer.key2 = map(int, input('%s의 암호 두 개를 입력해주세요: ' % order[1].name).split(' '))

    for i in range(40):
        print("===============You can't see!=============")

    print("Game Start!")

    while True:
        if flag == 0:
            for i in range(10):
                print("=")*80
                print("%d회차!" % (i+1))
                ps1 = cardorder[1][i] * order[0].key1 + order[0].key2
                ps2 = cardorder[0][i] * order[1].key1 + order[1].key2
                print("%s의 카드: %d" % (order[0].name, ps2))
                print("%s의 카드: %d" % (order[1].name, ps1))
                print(cardorder[0][i])
                print(cardorder[1][i])
                firstdata = input('%s, Do you want to bet? or die?: ' % order[0].name)
                if firstdata == 'die':
                    if cardorder[0][i] == 10:
                        order[0].chip -= 15
                        order[1].chip += 15
                    else:
                        order[0].chip -= 5
                        order[1].chip += 5

                elif firstdata == 'bet':
                    firstcount = int(input('%s의 베팅 칩 개수를 입력하세요.: ' % order[0].name))
                    order[0].chip -= firstcount
                    lastdata = input('%s, Do you want to fight? or die?: ' % order[1].name)
                    if lastdata == 'fight':
                        order[1].chip -= firstcount
                        print("승부 결과: %s의 카드는 '%d', %s의 카드는 '%d'" % (order[0].name, cardorder[0][i], order[1].name, cardorder[1][i]))
                        if fightres(cardorder[0][i], cardorder[1][i]) == "R":
                            order[0].chip += firstcount * 2
                        elif fightres(cardorder[0][i], cardorder[1][i]) == "B":
                            order[1].chip += firstcount * 2
                        else:
                            order[0].chip += firstcount
                            order[1].chip += firstcount

                    elif lastdata == 'die':
                        if cardorder[1][i] == 10:
                            order[0].chip += 15 + firstcount
                            order[1].chip -= 15
                        else:
                            order[0].chip += firstcount + 5
                            order[1].chip -= 5

                if order[0].chip <= 0:
                    print("%s win!" % order[1].name)
                    flag = 1
                    break

                elif order[1].chip <= 0:
                    print("%s win!" % order[0].name)
                    flag = 1
                    break

                print("칩 개수 현황: %s = %d, %s = %d" % (redplayer.name, redplayer.chip, blueplayer.name, blueplayer.chip))

                order.reverse()
                cardorder.reverse()

        if not flag:
            if order[0].chip > order[1].chip:
                print("%s win!" % order[0].name)
                break
            elif order[1].chip > order[0].chip:
                print("%s win!" % order[1].name)
                break
            else:
                print("Tie")
                break

        break
    flag = 0

    rep = input("Repeat? 'Y'/'N': ")
    if rep == 'N':
        break

    # 자신의 칩 개수보다 많은 칩을 베팅하는 것에 대한 오류
    # 자연수를 입력하는 것에 대한 확인 필요 (잘못 입력했으면 오류 메시지 + 다시!)
    # 특정 문자도 마찬가지 (bet, die 외에 다른 것을 입력하면 오류 메시지 + 다시 입력하라!)












