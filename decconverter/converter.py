

def converter(dec):
    pass



while True:
    dec = int(input('Please enter a decimal below 255'))
    if dec < 255:
        converter(dec)
    else:
        dec = int(input('Sorry, BELOW 255, please try again.'))
