import tkinter as tk
from EmpresasDAO import EmpresasDAO
from naturezaJuridicaDAO import naturezajuridicaDAO
from MinhaTela import MinhaTela  

if __name__ == '__main__':
    janela = tk.Tk()
     

    DAO = EmpresasDAO()
    DAO2 = naturezajuridicaDAO()
    minha_tela = MinhaTela(janela, DAO, DAO2)
    janela.mainloop()




  


    