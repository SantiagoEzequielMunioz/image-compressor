from PIL import Image,ImageTk
from tkinter import Entry, Frame,Label, StringVar,Tk,Menu,Button, filedialog, messagebox, Toplevel

class Aplicacion(Frame):

    def __init__(self,master=None):
        super().__init__(master)
        self.master=master
        self.config(bg='#B0BEC5',padx=10)
        self.pack(expand=1,fill='both',anchor='center')
        img_portada=Image.open('portada2.jpg')
        img_portada=img_portada.resize((800,700))
        self.img=ImageTk.PhotoImage(img_portada)

        ### MENUS ###
        filemenu=Menu(barra_menu,tearoff=0)
        barra_menu.add_cascade(label='Menu',menu=filemenu)
        filemenu.add_command(label='Abrir',command=self.buscar)
        filemenu.add_command(label='Convertir',command=self.conversor)
        filemenu.add_command(label='Cerrar',command=self.destroy)

        aboutmenu=Menu(barra_menu,tearoff=0)
        barra_menu.add_cascade(label='Acerca de',menu=aboutmenu)
        aboutmenu.add_command(label='Acerca de',command=self.about)
        
        self.widgets()

    def widgets(self):
    ### INTERFAZ - LABELS Y ENTRYS ###
        self.campo=StringVar()
        self.ruta_img=None

        self.portada=Label(self,image=self.img,border=0).grid(row=0,column=0,columnspan=3,pady=10,sticky='nsew')
        # Label(self,text='COMPRESOR DE IMÁGENES',font=('Arial Italic',24),justify='center',bg='black',fg='white').place(relx=0.2,rely=0.1,relwidth=0.6)
        self.subtitulo=Label(self,text='Ruta de archivo:',bg='#B0BEC5',font=('Verdana',12)).grid(row=1,column=0,ipady=15,padx=(10,5))
        self.entrada=Entry(self,width=50,font=('Arial',12),textvariable=self.campo,state='readonly').grid(row=1,column=1,ipady=15)
        self.search=Button(self,text='Buscar...',font=('Verdana',12),activebackground='blue',command=self.buscar)
        self.search.grid(row=1,column=2,padx=20)
        self.convertir=Button(self,text='CONVERTIR',font=('Verdana',12),command=self.conversor).grid(row=2,column=0,columnspan=3,pady=10)

        self.grid_rowconfigure(0,weight=3)
        self.grid_rowconfigure((1,2),weight=1)
        self.grid_columnconfigure((0,1,2),weight=1)

    ### BUSCADOR ###
    def buscar(self):
        archivo=filedialog.askopenfilename(title='Buscar imagen',initialdir='/',
        filetypes=(('Archivos de imagen (JPG)','*.jpg'),
                    ('Archivos de imagen (PNG)','*.png'),))
        self.campo.set(archivo)
        self.ruta_img = archivo
        return self.ruta_img
        
    ### CONVERSOR ###
    def conversor(self):
        if self.campo.get()!='':
            try:
                guardado=filedialog.asksaveasfilename(initialdir='/',
                        filetypes=(('Archivos de imagen (JPG)','*.jpg'),))
                imagen = Image.open(self.ruta_img)
                imagen = imagen.convert('RGB')
                guardado=guardado.strip('.jpg')
                imagen.save(str(guardado)+'.jpg',quality=30)
                messagebox.showinfo('Compresor de Imágenes','Imagen guardada y comprimida con éxito!')
            except:
                pass
        else:
            messagebox.showerror('Compresor de Imágenes','Seleccione una imagen.')
        return

    ### ACERCA DE... ###
    def about(self):
        win_instrucciones=Toplevel()
        win_instrucciones.iconbitmap('anclalogo.ico')
        win_instrucciones.title('Acerca de...')
        texto='''
Creado por: TFCDNA Muñoz Santiago

Email: santiagomunioz.armada@gmail.com

Programa creado con Python 3.10.2 64-bit y librería Pillow 9.1.0

AÑO 2022
        '''
        Label(win_instrucciones,font=('Verdana',10),text=texto,justify='left',relief='groove').pack(expand=True,fill='both')

if __name__ == '__main__':
    root=Tk()
    root.title('Compresor de Imágenes')
    barra_menu=Menu(root)
    root.config(menu=barra_menu)
    root.iconbitmap('anclalogo.ico')
    root.geometry('800x750+20+20')
    root.wm_minsize(800,800)
    app=Aplicacion(root)
    app.mainloop()