import pygame  #importa la libreria pygame

NERO = (255, 255, 255)     #definisco il colore nero per il disegno
BIANCO = (0, 0, 0)         #definisco il colore bianco per il disegno

def drawgrid(QRcode):       #definisco la funzione
    a=0   #veriabile ausiliara
    b=0   #variabile ausiliario
    dim = 200
    for x in range(0, DIMEN[0], dim):  #iterzaione di un ciclo for
        for y in range(0, DIMEN[1], dim):  #iterzaione di un ciclo for
         if QRcode[a][b] == 0:
                vuoto = pygame.Rect(x, y, dim, dim)  #creo la variabile per disegnare un "pixel" del QRcode
                pygame.draw.rect(finestra, BIANCO, vuoto, 0)  #disegno il pixel colorato di bianco
        else:
            pieno = pygame.Rect(x, y, dim, dim)  #creo la variabile per disegnare un "pixel" del QRcode    
            pygame.draw.rect(finestra, NERO, pieno, 1)   #disegno il pixel colorato di nero
        a=a+1
        a=0
        b=b+1


def main():
    stringa = input("inserisci una stringa(max 12 caratteri)")
    stringa
    diz = {}
    dizionario=['a', 'b', 'c', 'd', 'e' ,'f', 'g', 'h', 'i', 'm', 'n', 'l', 'o', 'p', 'q',
                'r', 's', 't', 'u', 'v', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ' ']
    c = 0
    for key, val[] in diz.items()
        key=dizionario[c]
        for i in range(5):
            val[i]=random(0,1)        
    matrice = []    

if __name__=="__main__":
    main():
