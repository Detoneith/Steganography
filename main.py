import numpy as np
import PIL.Image, PIL.ImageTk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.dialogs import Messagebox
from tkinter.filedialog import askopenfilename, asksaveasfilename


class Steganographie(ttk.Frame):

    def __init__(self,master):

        super().__init__(master, padding=(20, 10))
        self.pack(fill=BOTH, expand=YES)

        self.message_entry = ttk.StringVar(value='Enter a message')

        self.create_menu()
        self.create_form_entry("No image selected", self.message_entry)
        self.create_canvas()
        self.create_buttonbox()

        #self.create_text_widget("No image selected")
        #self.create_widgets()

    def create_menu(self):

        menubar = ttk.Menu(self.master)


        filemenu = ttk.Menu(menubar, tearoff=0)

        filemenu.add_command(label='Open', command=self.open_file)
        filemenu.add_command(label='Save', command=self.save_file)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.master.quit)


        #editmenu = ttk.Menu(menubar, tearoff=0)
        #editmenu.add_command(label='Cut')
        #editmenu.add_command(label='Copy')
        #editmenu.add_command(label='Paste')


        helpmenu = ttk.Menu(menubar, tearoff=0)
        helpmenu.add_command(label='About')


        menubar.add_cascade(label='File', menu=filemenu)
        #menubar.add_cascade(label='Edit', menu=editmenu)
        menubar.add_cascade(label='Help', menu=helpmenu)
        
        self.master.config(menu=menubar)

    def create_form_entry(self,label, variable):
        """Create and add the widget elements"""
        container = ttk.Frame(self)
        container.pack(fill=X, expand=YES, pady=5)

        self.label = ttk.Label(master=container, text=label.title())
        self.label.pack(side=TOP, padx=5)

        self.entry = ttk.Entry(master=container, textvariable=variable)
        self.entry.pack(side=LEFT, padx=5, fill=X, expand=YES)
        #self.entry.configure(foreground="grey")

        self.entry.bind("<FocusIn>", self.on_entry_click)

    def on_entry_click(self, event):
        """Effacer le contenu de l'entrée si le texte par défaut est présent"""
        entry = event.widget
        if entry.get() == "Enter a message":
            entry.delete(0, "end")

    '''def create_text_widget(self,label):
        """Create and add the widget elements"""
        container = ttk.Frame(self)
        container.pack(fill=X, expand=YES, pady=5)

        self.label = ttk.Label(master=container, text=label.title())
        self.label.pack(side=TOP, padx=5)

        # text widget
        txt = ttk.Text(master=container, height=5, width=50, wrap="none")
        #txt.insert(END, DemoWidgets.ZEN)
        txt.pack(side=LEFT, anchor=NW, pady=5, fill=BOTH, expand=YES)'''

    
    def create_canvas(self):
        container = ttk.Frame(self)
        container.pack(fill=X, expand=YES, pady=5)

        self.canvas = ttk.Canvas(container, width=400, height=400)
        self.canvas.pack()


    def create_buttonbox(self):
        """Create the application buttonbox"""
        container = ttk.Frame(self)
        container.pack(fill=X, expand=YES, pady=(15, 10))

        cnv_btn = ttk.Button(
            master=container,
            text="Encode",
            command=self.encode,
            style="success.TButton",
            width=8,
        )
        cnv_btn.pack(side=LEFT, padx=5)

        cnl_btn = ttk.Button(
            master=container,
            text="Decode",
            command=self.decode,
            style="danger.TButton",
            width=8,
        )
        cnl_btn.pack(side=RIGHT, padx=5)



    def open_file(self):

        filetypes = (('Image files', '*.jpg;*.png'), ('All files (*.*)', '*.*'))
        filepath = askopenfilename(title='Open an Image', filetypes=filetypes)
        if filepath:
            self.label.configure(text=filepath)
            self.image = PIL.Image.open(filepath, 'r')
            
            #self.photo = PIL.ImageTk.PhotoImage(self.image)
            #self.canvas.create_image(0, 0, anchor="nw", image=self.photo)
            #resize with image size:
            #self.photo = PIL.ImageTk.PhotoImage(self.image)
            #self.canvas.config(width=self.image.width, height=self.image.height)
            #self.canvas.create_image(0, 0, anchor="nw", image=self.photo)
            # resize image if it is too large for canvas

            #resize
            max_size = (400, 400)
            if self.image.size > max_size:
                self.image.thumbnail(max_size)

            self.photo = PIL.ImageTk.PhotoImage(self.image)
            self.canvas.config(width=self.image.width, height=self.image.height)
            self.canvas.create_image(0, 0, anchor="nw", image=self.photo)


    def save_file(self):
        #filetypes = (("JPEG files", "*.jpg"), ("PNG files", "*.png"), ("All files", "*.*"))
        #filepath = asksaveasfilename(title="Save the image", filetypes=filetypes, defaultextension=".png")
        if hasattr(self, "image"):

            filetypes = (("PNG files", "*.png"), ("JPEG files", "*.jpg"), ("All files", "*.*"))
            encoded_image_file_path = asksaveasfilename(title="Save the image", filetypes=filetypes, defaultextension=".png")

            if encoded_image_file_path:
                self.encoded_message.save(encoded_image_file_path)

        else:
            Messagebox.show_warning(title='Warning', message='Nothing to save!')

    def encode(self):
        if not hasattr(self, 'image'):
            Messagebox.show_error("No image selected", "Steganographie")
            return
        message_to_encode = self.message_entry.get()
        if not message_to_encode:
            Messagebox.show_warning(title='Warning', message='Please enter a message to encode!')
            return
        width, height = self.image.size
        img_array = np.array(list(self.image.getdata()))

        #calculating nb of channels if they are rgb or rgba
        if self.image.mode == "P":
            Messagebox.show_error("Not supported")
            #exit()

        channels = 4 if self.image.mode == 'RGBA' else 3

        pixels = img_array.size // channels

        # define a stop indicator
        stop_indicator = "$NEURAL$"
        stop_indicator_length = len(stop_indicator)

        message_to_encode += stop_indicator

        #write into bits
        byte_message = ''.join(f"{ord(c):08b}" for c in message_to_encode)
        bits = len(byte_message)

        if bits > pixels:
            Messagebox.show_warning('Warning', 'Message is too big to fit in the selected image!')

        else:
            index = 0
            for i in range(pixels):
                for j in range(0,3):
                    if index < bits:
                        img_array[i][j]=int(bin(img_array[i][j])[2:-1] + byte_message[index], 2)
                        index +=1

        img_array = img_array.reshape((height, width, channels))
        #unsigned integer 8bits
        self.encoded_message = PIL.Image.fromarray(img_array.astype('uint8'), self.image.mode)

    
    def decode(self):

        if not hasattr(self, 'image'):
            Messagebox.show_error("No image selected", "Steganographie")
            return

        img_array = np.array(list(self.image.getdata()))

        channels = 4 if self.image.mode =='RGBA' else 3

        pixels = img_array.size // channels

        secret_bits = [bin(img_array[i][j]) [-1] for i in range(pixels) for j in range(0,3)]
        secret_bits = ''.join(secret_bits)
        secret_bits = [secret_bits[i:i+8] for i in range(0,len(secret_bits),8)]

        secret_message = [chr(int(secret_bits[i], 2)) for i in range(len(secret_bits))]
        secret_message = ''.join(secret_message)

        stop_indicator = "$NEURAL$"

        if stop_indicator in secret_message:
            Messagebox.show_info(title='Decoded message', message=secret_message[:secret_message.index(stop_indicator)])
        else:
            Messagebox.show_error('Warning', 'No encoded message found in the selected image!')


if __name__=='__main__':

    app = ttk.Window(title="Steganographie", themename="cyborg", size=[800,600])
    Steganographie(app)
    app.mainloop()