from random import randint
from time import sleep

gostaria = input("\033[7;40mVocê gostaria de jogar o dado?:")
print("\033[36mJogando o dado...\033[m")
sleep(2)
if(gostaria == "S" or gostaria == "s"):
   dado = randint(0, 6)
   print("O numero que caiu no dado foi de {}{}{}".format("\033[32m",dado,"\033[m"))
else:
    print("Voce quem sabe")