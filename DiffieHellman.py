from random import randint
 
if __name__ == '__main__':
 
    # Both the persons will be agreed upon the
    # public keys G and P
    #mensajes publicos
    P = 23
    G = 9
    
    print('El valor de P es:%d'%(P))
    print('El valor de G es :%d'%(G))
     
    # Alice will choose the private key a
    a = int(input('Ingrese La llave secreta A: \n'))
    print('La llave secreta para A es :%d'%(a))
     
    # gets the generated key
    x = int(pow(G,a,P)) 
     
    # Bob will choose the private key b
    b = int(input('Ingrese la llave secreta B: \n'))
    print('La llave secreta de B es :%d'%(b))
    
    # gets the generated key
    y = int(pow(G,b,P)) 
     
    # Secret key for Alice
    ka = int(pow(y,a,P))
     
    # Secret key for Bob
    kb = int(pow(x,b,P))
     
    print('La llave secreta de A es  : %d'%(ka))
    print('La llave secreta de B es  : %d'%(kb))
