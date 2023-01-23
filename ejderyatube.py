import tkinter
import customtkinter
from pytube import YouTube, Stream
from threading import Thread
import string
from PIL import Image
from io import BytesIO
import base64

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")




class Ejderyatube:
    english = {"app_title": "Pytube Video Download" ,"title": "Enter Youtube link", 
               "hghst_down": "Download Highest Resolution", "res_down": "Download By Resolution",
               "audio_down": "Download By Audio", "lbl_downldd": "Downloaded", "invld_url": "Invalid URL",
               "author": """Pytube Video Downloader Test by TarikBurhan.\n Application might freeze while downloading.""",
               "res_sel": "Resolution Select", "resltns": "Resolutions", "sttngs": "Settings",
               "sel_ur_res": "Select Your Resolution", "select": "Select", "hghst_res": "Highest_Resolution",
               "audio": "Audio", "langs": "Languages"
               }

    turkish = {"app_title": "Pytube Video İndirme" ,"title": "Youtube linkini giriniz", 
               "hghst_down": "En Yüksek Çözünürlükte İndirme", "res_down": "Çözünürlüğe Göre İndirme",
               "audio_down": "Sadece Ses İndir", "lbl_downldd": "İndirildi", "invld_url": "Yanlış URL",
               "author": """TarıkBurhan tarafından Pytube Video İndirici.\n İndirme yaparken uygulamada donmalar olabilir.""",
               "res_sel": "Çözünürlük Seçme", "resltns": "Çözünürlükler", "sttngs": "Ayarlar",
               "sel_ur_res": "Çözünürlüğünüzü Seçiniz", "select": "Seç", "hghst_res": "En_Yuksek_Cozunurluk",
               "audio": "Ses", "langs": "Diller"
               }

    def __init__(self):
        self.icon = """
            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
            """
        self.settings_icon = """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"""
        self.folder_icon = """iVBORw0KGgoAAAANSUhEUgAAAB4AAAAeCAYAAAA7MK6iAAAACXBIWXMAAAsTAAALEwEAmpwYAAABh
            0lEQVR4nO3Sy0oCURzH8ekReoA2LSNduHJpRkSzyBwQwo0YkgtFKHDRIqpVvUGLFq3qAaLrKrEGYsykgTEV7ZTYTc1Lzs2m
            /Ifb4i8onlb+4LMaOF/OcBhmsMH+YzXRPawkXNdKwgW/yQlXrP2dSrghOLflmBMwjZjz4ONqdkwTuNFuqIJjBIAZQsPVKJu
            tXbBAx8wuGi4d20jpxAao0wmoRh1Qu+S6NAfls8kHNFzYs5CnfQtglMQCQHGjJ9pdUEXDjzvj+eLhFJSOpv+o8fPQelvvWZ
            OEDTSs3Pq11usa0KBnl/Gwng4ZrZdVoEFPh/CwlgoY388rQIOWCuBhNek3vgphoEFN+juEJZ9h5JeABlXydXhcosf4JEGgQ
            RE9nW7sqTRzi0CDKnkqaFjPeIme8QIlBP/VkpuoSTfQoEhuPCyLHFFEDmiQRQ4PN+IsadywQEWcxcN1wU7qgh0oIWi4wlvv
            q7wVaKjw1hwaLp+bt8oRk/EeMUM/tc8sR0ybaHiwwZg+7gcje6NKTyJJbgAAAABJRU5ErkJggg==">"""

        self.download_path = ".\YoutubeVideos"

        self.lang_dict = self.english

        
        self.app = customtkinter.CTk()
        self.app_height = 350
        self.app_width = 600
        self.app.minsize(self.app_width, self.app_height)
        self.app.maxsize(self.app_width, self.app_height)
        self.screen_height = self.app.winfo_screenheight() 
        self.screen_width = self.app.winfo_screenwidth()
        self.x = self.screen_width / 2 - self.app_width / 2
        self.y = self.screen_height / 2 - self.app_height / 2
        self.app.geometry(f"{self.app_width}x{self.app_height}+{int(self.x)}+{int(self.y)}")

        self.img = tkinter.PhotoImage(data=self.icon)
        self.app.iconphoto(False, self.img)
        tk_set_img = Image.open(BytesIO(base64.b64decode(self.settings_icon)))
        tk_fold_img = Image.open(BytesIO(base64.b64decode(self.folder_icon)))

        self.settings_image = customtkinter.CTkImage(light_image=tk_set_img, dark_image=tk_set_img, size=(15,15))
        self.folder_image = customtkinter.CTkImage(light_image=tk_fold_img, dark_image=tk_fold_img, size=(15,15))
        
        self.app.title(self.lang_dict["app_title"])

        self.title = customtkinter.CTkLabel(self.app, text=self.lang_dict["title"])
        self.title.pack(padx=10, pady=5)

        self.url = tkinter.StringVar()
        self.link_section = customtkinter.CTkEntry(self.app, width=350, height=40, textvariable=self.url)
        self.link_section.pack()

        # Error/Downloaded Label
        self.finish_label = customtkinter.CTkLabel(self.app, text="")
        self.finish_label.pack(padx=10, pady=10)

        # Download Buttons
        self.download_button = customtkinter.CTkButton(self.app, text=self.lang_dict["hghst_down"], 
                                                        command=self.download_thread, width=200)
        self.download_button.pack(padx=10, pady=5)

        self.download_by_res_button = customtkinter.CTkButton(self.app, text=self.lang_dict["res_down"], 
                                                                command=self.download_by_res_thread, width=165)
        self.download_by_res_button.pack(padx=10, pady=5)

        self.download_audio_button = customtkinter.CTkButton(self.app, text=self.lang_dict["audio_down"], 
                                                                command=self.download_audio_thread, width=140)
        self.download_audio_button.pack(padx=10, pady=5)

        # Watermark
        self.author_label = customtkinter.CTkLabel(self.app, text=self.lang_dict["author"], text_color="orange")
        self.author_label.pack(padx=10, pady=40)

        # UI Settings
        self.settings_button = customtkinter.CTkButton(self.app, image=self.settings_image, text="", height=20, width=20,
                                                        command=self.settings)
        self.settings_button.place(relx=0.93, rely=0.02)

        self.path_select_button = customtkinter.CTkButton(self.app, image=self.folder_image, text="", height=20, width=20,
                                                            command=self.select_path)
        self.path_select_button.place(relx=0.93, rely=0.1)


        self.app.mainloop()


    def button_disable(self):
        self.download_button.configure(state="disabled")
        self.download_by_res_button.configure(state="disabled")
        self.download_audio_button.configure(state="disabled")

    # Enable buttons
    def button_enable(self):
        self.download_button.configure(state="normal")
        self.download_by_res_button.configure(state="normal")
        self.download_audio_button.configure(state="normal")

    # Downlaod function for highest resolution
    def download_function(self):   
        self.button_disable()
        try:
            ytLink = self.link_section.get()
            ytObj = YouTube(ytLink)
            video = ytObj.streams.get_highest_resolution()
            self.title.configure(text=ytObj.title, text_color="white")
            download_title = ytObj.title.translate(str.maketrans('', '', string.punctuation))
            video.download(filename=f'{download_title}_{self.lang_dict["hghst_res"]}.mp4', output_path=self.download_path)
            self.finish_label.configure(text=self.lang_dict["lbl_downldd"], text_color="green")

        except:
            self.finish_label.configure(text=self.lang_dict["invld_url"], text_color="red")
        self.link_section.delete(0, customtkinter.END)
        self.button_enable()

    # Download function for resolution selection
    def download_by_res(self):
        self.button_disable()
        try:
            ytLink = self.link_section.get()
            ytObj = YouTube(ytLink)
            video = ytObj.streams
            resolutions = []
            for stream in video.filter(progressive=True):
                resolutions.append(stream.resolution)
            selected_resolution = [""]

            new_window = customtkinter.CTkToplevel()
            new_window.title(self.lang_dict["res_sel"])
            nw_screen_height = new_window.winfo_screenheight() 
            nw_screen_width = new_window.winfo_screenwidth()
            nw_app_width = 300
            nw_app_height = 100
            new_window.minsize(nw_app_width, nw_app_height)
            new_window.maxsize(nw_app_width, nw_app_height)
            nw_x = nw_screen_width / 2 - self.app_width / 2
            nw_y = nw_screen_height / 2 - self.app_height / 2
            new_window.geometry(f"{nw_app_width}x{nw_app_height}+{int(nw_x + nw_app_width / 2)}+{int(nw_y + nw_app_height / 2)}")
            value = customtkinter.StringVar(new_window)
            value.set(self.lang_dict["resltns"])
            download_title = ytObj.title.translate(str.maketrans('', '', string.punctuation))
            def select(vd):
                self.title.configure(text=ytObj.title, text_color="white")
                if selected_resolution[0] == "":
                    vd.get_highest_resolution().download(filename=f'{download_title}_{self.lang_dict["hghst_res"]}.mp4', 
                                                            output_path=self.download_path)
                else:
                    vd.get_by_resolution(selected_resolution[0]).download(filename=f'{download_title}_{selected_resolution[0]}.mp4', 
                                            output_path=self.download_path)
                self.finish_label.configure(text=self.lang_dict["lbl_downldd"], text_color="green")
                new_window.destroy()
            
            def sel(choice):
                selected_resolution[0] = choice

            
            nw_label = customtkinter.CTkLabel(new_window, text=self.lang_dict["sel_ur_res"])
            nw_label.pack()
            drop_down = customtkinter.CTkOptionMenu(new_window, variable=value, values=resolutions, 
                                                    command=sel)
            drop_down.pack(padx=3, pady=3)
            submit = customtkinter.CTkButton(new_window, text=self.lang_dict["select"], command=lambda: select(video))
            submit.pack(padx=3, pady=3)
        except:
            self.finish_label.configure(text=self.lang_dict["invld_url"], text_color="red")
        self.link_section.delete(0, customtkinter.END)
        self.button_enable()

    # Download function for only audio
    def download_audio(self):
        self.button_disable()
        try:
            ytLink = self.link_section.get()
            ytObj = YouTube(ytLink)
            video = ytObj.streams.get_audio_only()
            self.title.configure(text=ytObj.title, text_color="white")
            download_title = ytObj.title.translate(str.maketrans('', '', string.punctuation))
            video.download(filename=f'{download_title}_{self.lang_dict["audio"]}.mp4', output_path=self.download_path)
            self.finish_label.configure(text=self.lang_dict["lbl_downldd"], text_color="green")

        except:
            self.finish_label.configure(text=self.lang_dict["invld_url"], text_color="red")
        self.link_section.delete(0, customtkinter.END)
        self.button_enable()

    # Threads for download function
    def download_by_res_thread(self):
        thread = Thread(target=self.download_by_res)
        thread.daemon = True
        thread.start()

    def download_thread(self):   
        thread = Thread(target=self.download_function)
        thread.daemon = True
        thread.start()

    def download_audio_thread(self):
        thread = Thread(target=self.download_audio)
        thread.daemon = True
        thread.start()

    def lang_tr(self):
        self.lang_dict = self.turkish

    def lang_en(self):
        self.lang_dict = self.english

    def settings(self):
        new_window = customtkinter.CTkToplevel()
        new_window.title(self.lang_dict["sttngs"])
        nw_screen_width = self.screen_width
        nw_screen_height = self.screen_height
        nw_app_width = 250
        nw_app_height = 100
        new_window.minsize(nw_app_width, nw_app_height)
        new_window.maxsize(nw_app_width, nw_app_height)
        nw_x = nw_screen_width / 2 - nw_app_width / 2
        nw_y = nw_screen_height / 2 - nw_app_height / 2
        new_window.geometry(f"{nw_app_width}x{nw_app_height}+{int(nw_x)}+{int(nw_y)}")

        language_label = customtkinter.CTkLabel(new_window, 40, 10, text=self.lang_dict["langs"])
        language_label.place(relx=0.03, rely=0.1)

        tr_button = customtkinter.CTkButton(new_window, 30, 10, text="TR", command=self.lang_tr)
        tr_button.place(relx=0.3, rely = 0.1)

        en_button = customtkinter.CTkButton(new_window, 30, 10, text="EN", command=self.lang_en)
        en_button.place(relx=0.45, rely = 0.1)


    def select_path(self):
        path = customtkinter.filedialog.askdirectory()
        self.download_path = path


window = Ejderyatube()


# Dil değiştirme olmadı???