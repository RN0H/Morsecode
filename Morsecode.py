from tkinter import*
import tkinter as tk
from tkinter.ttk import*
from tkinter import ttk
from ttkthemes import ThemedStyle
from random import choices,randint
import random

morse_alphabets = dict(zip(['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'],\
                           ['.-','-...','-.-.','-..','.','..-.','--.','....','..','.---','-.-','.-..','--','-.','---','.--.','--.-','.-.','...','-','..-','...-','.--','-..-','-.--','--..']))
class Morse:
     def __init__ (self,root):
         self.master = root
         self.master.title('Morsecode')
         self.master.geometry('500x200')
         theme = ThemedStyle(self.master)
         theme.set_theme('radiance')

         self.input = StringVar()

         input =  Entry(self.master,textvariable = self.input)
         encode = Button(self.master,text='Encode',command = self.encoder)

         decode = Button(self.master,text='Decode',command = self.decoder)
         quit  = Button(self.master,text='Quit',command = self.master.destroy)
         self.Ans = Label(self.master)

         for i in (input,encode,decode,quit,self.Ans):
                   i.pack()

     def encoder(self):
                text = self.input.get()

                morsecode=[]
                for letter in text.lower():
                       for alphabet,morse in morse_alphabets.items():
                                 if  alphabet==letter:
                                            morsecode.append(morse)

                print(' '.join(morsecode))
                return self.Ans.config(text = ' '.join(morsecode))

     def decoder(self):
               morsecode = self.input.get()
               word = []
               for morse_letter in morsecode.split(' '):
                    for alphabet,morse in morse_alphabets.items():
                            if morse==morse_letter:
                                    word.append(alphabet)

               print(' '.join(word))
               return self.Ans.config(text = ''.join(word))

if __name__ == "__main__":
          root = tk.Tk()
          Morse(root)
          root.mainloop()
