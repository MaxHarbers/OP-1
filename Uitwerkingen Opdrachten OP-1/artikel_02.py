
def artikelnummers_genereren():
        import random
        import string
        
        cijfers_01 = random.randrange(999, 10000)
        cijfers_02 = random.randrange(999,10000)
        letters_01 = ''

        for y in range( 6 ):
                letters_01 += (random.choice(string.ascii_lowercase) )
                print( letters_01)

        eerste_letter = ( ord ( letters_01 [0] ) )
        print( eerste_letter )
        
        if( eerste_letter >= 97 and eerste_letter <= 102  ):
                klassen = "microcontroller"

        if( eerste_letter >= 103 and eerste_letter <= 108  ):
                klassen = "mini-PC"

        if( eerste_letter >= 109 and eerste_letter <= 114  ):
                klassen = "home automation"

        if( eerste_letter >= 115 and eerste_letter <= 122  ):
                klassen = "accessoires"        
                     

        print( "{0}-{1}-{2}-{3} " "{4}".format( cijfers_01, ( letters_01 [:3 ] ), ( letters_01 [3:] ), cijfers_02, klassen, ) )


