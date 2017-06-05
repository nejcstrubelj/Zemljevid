import tkinter as tk
import os, sys

VISINA = 640
SIRINA = 800



class Zemljevid:
    def __init__(self, okno):
        self.okno = okno
        self.platno = tk.Canvas(okno,
            width = SIRINA,
            height = VISINA
        )
        self.platno.grid(row = 1, column = 1, columnspan = 2)
        #self.slika = tk.PhotoImage(file = "slike držav/islandija.gif")
        #self.platno.create_image(SIRINA // 2, VISINA // 2, image = self.slika)

        gumb1 = tk.Button(okno, text='1. država')
        gumb1.grid(row=2, column=1)

        gumb2 = tk.Button(okno, text='2. država')
        gumb2.grid(row=2, column=2)

        gumb2 = tk.Button(okno, text='3. država')
        gumb2.grid(row=3, column=1)

        gumb2 = tk.Button(okno, text='4. država')
        gumb2.grid(row=3, column=2)

        self.naslednje_vprasanje()

    def naslednje_vprasanje(self):
        path = "U:/git/Zemljevid/slikedrzav/"
        dirs = os.listdir(path)
        for i in range(len(dirs)):
            dirs[i] = dirs[i][:-4]
        print(dirs)






okno = tk.Tk()
aplikacija = Zemljevid(okno)
okno.mainloop()

#z metodo konfig spreminjas napise na gumbih

#z modulom random, nakljucno izbiras države

# funkcija "naslednje_vprasanje(self):", se bo sprožila takoj ko boš odprl aplikacijo.

#kar bos naslednje uporabil je funkcija "listdir(path='.')", (profesor jo je našel
# na naslovu https://docs.python.org/3/library/os.html) s tem bos nastel vsa imena datotek
#(slik držav) v neki mapi. Nato bosš iz teh imen naključno izbral eno od njih in jo odprl.
#nato bos to ime države se napisal na naključno izbran gumb, na ostale tri gumbe pa napisal neka
#druga 3 nakljucna imena drzav s tistega seznama.
