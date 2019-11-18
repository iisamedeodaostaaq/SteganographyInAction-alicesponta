widthImg=500;
heightImg=400;
j=100;
#Variabile di appoggio
app=0
def setup():
    global i, img, app,answer, widthImg, heightImg, lett
    #Messaggio mostrato a video appena viene eseguito lo script
    messaggio=input ("Inserisci la tua frase")
    println( str(messaggio))
    #lett prende la prima lettera della parola
    lett=messaggio[0]
    print(lett)
    size(500, 400)
    #Creo l'immagione
    img=createImage(widthImg,heightImg,RGB)
    disegno()
#Funzione per la visualizzazione della finestra per l'inserimento del testo
def input(message=""):
    from javax.swing import JOptionPane 
    return JOptionPane.showInputDialog (frame,message)
    disegno()

    
def disegno():
    global img,esa,lett,j
    #esa contiene la conversione esadecimale di lett
    esa=unhex(lett)
    print(esa)
    for i in range(50):
        for j in range (50):
            img.loadPixels()
            img.pixels[i]= color(234,23,45)
            img.updatePixels()
            image(img,0,0)
