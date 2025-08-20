import customtkinter as ctk
#aparencia
ctk.set_appearance_mode('dark')
#funcionalidades
def Validar_login():
   usuario = Campo_usuario.get()
   senha = Campo_Senha.get()

   #verificar-se-está-correto
   if usuario == 'Admin' and senha == '12345':
      Resultado_login.configure(text='Login feito com sucesso!',text_color='green')

   else:
      Resultado_login.configure(text='Usuario ou senha incorretos',text_color='red')
#janela-principal
app = ctk.CTk()
app.title('Tela de login')
app.geometry('300x300')
#campos
#label
Label_usuario = ctk.CTkLabel(app,text='Usuario')
Label_usuario.pack(pady=10)
#entry
Campo_usuario = ctk.CTkEntry(app,placeholder_text='Digite o nome de usuario')
Campo_usuario.pack(pady=10)
#label
Label_Senha = ctk.CTkLabel(app,text='Senha')
Label_Senha.pack(pady=10)
#entry
Campo_Senha = ctk.CTkEntry(app,placeholder_text='Digite Sua Senha',show='*')
Campo_Senha.pack(pady=10)
#button
botao_login = ctk.CTkButton(app,text='Login',command=Validar_login)
botao_login.pack(pady=10)
#campo-feedback
Resultado_login = ctk.CTkLabel(app,text='')
Resultado_login.pack(pady=10)
#inicialização
app.mainloop()