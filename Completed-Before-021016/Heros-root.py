#Hero's Root
#http://www.codewars.com/kata/heros-root/

def int_rac(n, guess):
    """Integer Square Root of an Integer"""
    iters = list()
    
    while(True):
        iters.append(guess)
        
        new_guess = (guess + n/guess) / 2
        if abs(new_guess - guess) < 1:
            return len(iters)
            break
        else:
            guess = new_guess