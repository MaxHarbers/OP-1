
from random import *
import string

def artikelnummer():
  artikelnummeronderdeel1 = str(randint(0, 9)) + str(randint(0, 9)) + str(randint(0, 9)) + str(randint(0, 9))
  artikelnummeronderdeel2 = str("".join(choice(string.ascii_lowercase) for y in range(3)))
  artikelnummeronderdeel3 = "".join(choice(string.ascii_lowercase) for y in range(3))
  artikelnummeronderdeel4=str(randint(0,9))+str(randint(0,9))+str(randint(0,9))+str(randint(0,9))
  x = ord(artikelnummeronderdeel2[0])

  if  x <= 102 : 
      print("het nieuwe artikel nummer is : {}-{}-{}-{} microconroller ".format(artikelnummeronderdeel1, artikelnummeronderdeel2,
                                                                 artikelnummeronderdeel3, artikelnummeronderdeel4))
  elif x <= 108:
      print("het nieuwe artikel nummer is : {}-{}-{}-{} Mini-pc ".format(artikelnummeronderdeel1,
                                                                                artikelnummeronderdeel2,
                                                                                artikelnummeronderdeel3,
                                                                                artikelnummeronderdeel4))
  elif x <=114 :
      print("het nieuwe artikel nummer is : {}-{}-{}-{} homeautomation ".format(artikelnummeronderdeel1,
                                                                         artikelnummeronderdeel2,
                                                                         artikelnummeronderdeel3,
                                                                         artikelnummeronderdeel4))
  else:
      print("het nieuwe artikel nummer is : {}-{}-{}-{} accessoires ".format(artikelnummeronderdeel1,
                                                                                artikelnummeronderdeel2,
                                                                                artikelnummeronderdeel3,
                                                                                artikelnummeronderdeel4))




  return(artikelnummeronderdeel2,artikelnummeronderdeel3,artikelnummeronderdeel1,artikelnummeronderdeel4)


i=""


