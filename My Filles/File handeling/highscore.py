def game():
    return 9
score = game()
with open("highscore.txt") as f:
    highscoree = f.read()
if int(highscoree)<score:
    with open("highscore.txt","w") as f:
            f.write(str(score))


# def game():
#     return 44677

# score = game()
# with open("hiscore.txt") as f:
#     hiScoreStr = f.read()
# if int(hiScoreStr)<score :
#     with open("hiscore.txt", "w") as f:
#         f.write(str(score))

