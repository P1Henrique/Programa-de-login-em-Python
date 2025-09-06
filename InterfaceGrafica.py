import customtkinter as ctk
#funções
def validar_login():
    usuario = campo_usuario.get()
    senha = campo_usuario2.get()
#verificar
    if usuario == '123' and senha == '123':
        resultado_login.configure(text='Login feito com sucesso!!!',
        text_color='green')
    else:
        resultado_login.configure(text='Login invalido',
        text_color= 'red')

ctk.set_appearance_mode('dark')
#Criação da janela principal
app = ctk.CTk()
app.title('Sistema de Login')
app.geometry('300x300')

#Criação dos campos
#labell
label_usuario = ctk.CTkLabel(app,text='Usuário')
label_usuario.pack(pady=10)
#entry
campo_usuario=ctk.CTkEntry(app,placeholder_text='Digite seu usuário')
campo_usuario.pack(pady=10)
#label
label_usuario2 = ctk.CTkLabel(app, text='Senha')
label_usuario2.pack(pady=10)
#entry
campo_usuario2 = ctk.CTkEntry(app,placeholder_text='Digite sua senha')
campo_usuario2.pack(pady=10)
#button
botoa_login = ctk.CTkButton(app,text='Login',command=validar_login)
botoa_login.pack(pady=10)
#feddback
resultado_login = ctk.CTkLabel(app, text='')
resultado_login.pack(pady = 10)
app.mainloop()