class Login:
    def __init__(self) :
        self.login = '1'#login padrao 
        self.senha = '1'#login padrao
        self.valido = False
    def menuLogin(self,login,senha):
           
        if self.login == login and self.senha == senha :
            
            self.validado = True
            return self.validado 
        else:
            
            print("Login Invalido...")          
            self.validado = False
            return self.validado

    
    def cadastrarlogin(self):
        
        

            self.login = str (input("Digite seu novo login\n"))
            self.senha = str (input(" Digite uma nova Senha"))
            print("Cadastro Efetuado com Sucesso!")
                                    
        
