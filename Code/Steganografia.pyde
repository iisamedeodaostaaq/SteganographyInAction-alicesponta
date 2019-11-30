#Altezza e lunghezza dell'immagine
widthImg=500
heightImg=500
#Variabili per scorrere l'array
i=0
j=0
f=0
pix=0
#Lunghezza e Larghezza pixel
widthpixel=50
heightpixel=50
def setup():
    global img,widthImg,heightImg,messaggio
    #Messaggio mostrato a video appena viene eseguito lo script
    messaggio=input ("Inserisci la tua frase")
    println( str(messaggio))
    size(500, 500)
    #Creo l'immagione
    img=createImage(widthImg,heightImg,RGB)
    loadPixels()
    disegno()
    
#Funzione per la visualizzazione della finestra per l'inserimento del testo
def input(message=""):
    from javax.swing import JOptionPane 
    return JOptionPane.showInputDialog (frame,message)

    
def disegno():
    global img,r,g,b, messaggio,i,j,pix,f
    img.loadPixels()
    #Contiene la lunghezza del messaggio
    lenghtext=len(messaggio)
    #Finchè l'indice è minore della lunghezza del messaggio
    while f < lenghtext:
        #Effettuo un secondo controllo
        if (f<lenghtext):
            r=ord(messaggio[f])
        else:
            r=255
        if (f+1<lenghtext):
            g=ord(messaggio[f+1])
        else:
            g=255
        if (f+2<lenghtext):
            b=ord(messaggio[f+2])
        else:
            b=255
        f=f+3
        #Ciclo per inserire i colori nell'immagine
        for i in range(widthpixel):
            for j in range (heightpixel):
                img.pixels[pix+j+(widthImg*i)]=color(r,g,b)
        pix=pix+widthpixel
        
        
        
        print r
        print g
        print b
    img.updatePixels()
    image(img,0,0)
