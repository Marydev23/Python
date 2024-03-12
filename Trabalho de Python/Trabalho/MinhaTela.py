import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as mb

class MinhaTela:
    def __init__(self, janela, EmpresasEmpresasDAO, NaturezaJuridicaEmpresasDAO):
        self.EmpresasDAO = EmpresasEmpresasDAO
        self.NaturezaJuridicaDAO = NaturezaJuridicaEmpresasDAO
        janela.configure(bg="lightblue") 
        janela.geometry("800x600")  
        janela.title("Sistema de Cadastro de Empresas") 

        self.quadro = tk.Frame(janela, pady=10)
        self.quadro.pack(fill=tk.BOTH, expand=tk.YES)
        
        self.combobox_cod_natureza = ttk.Combobox(self.quadro) 
        self.combobox_cod_natureza.grid(row=3, column=1)
        
        self.lblcnpj = tk.Label(self.quadro, text="CNPJ: ")
        self.lblcnpj.grid(row=0, column=0) 
        self.etycnpj = tk.Entry(self.quadro)
        self.etycnpj.grid(row=0, column=1)

        self.lblrazao_social = tk.Label(self.quadro, text="Razão Social: ")
        self.lblrazao_social.grid(row=0, column=5) 
        self.etyrazao_social = tk.Entry(self.quadro)
        self.etyrazao_social.grid(row=0, column=6)

        self.lblcod_natureza = tk.Label(self.quadro, text="Código de Natureza: ")
        self.lblcod_natureza.grid(row=3, column=0)   
        self.etycod_natureza = tk.Entry(self.quadro)
        self.combobox_cod_natureza.bind("<<ComboboxSelected>>", self.atualizarDescricaoNatureza)
        self.preencherCodigosNatureza() 


        self.lbldescricao_natureza = tk.Label(self.quadro, text="Descrição de Natureza: ")
        self.lbldescricao_natureza.grid(row=3, column=5) 
        self.etydescricao_natureza = tk.Entry(self.quadro)
        self.etydescricao_natureza.grid(row=3, column=6)    

        self.lblqualificacao = tk.Label(self.quadro, text="Qualificacão: ")
        self.lblqualificacao.grid(row=5, column=0) 
        qualificacao= ["50 ", "49 ", "65 ", "34 "]
        self.combobox_qualificacao = ttk.Combobox(self.quadro, values=qualificacao)
        self.combobox_qualificacao.grid(row=5, column=1)

    
        self.lblcap_social = tk.Label(self.quadro, text="Capital Social: ")
        self.lblcap_social.grid(row=5, column=5) 
        self.etycap_social = tk.Entry(self.quadro)
        self.etycap_social.grid(row=5, column=6) 


        self.lblente_fed = tk.Label(self.quadro, text="Ente Federativo: ")
        self.lblente_fed.grid(row=6, column=0) 
        opcoes_ente_fed = ["0", "1", "3", "5"] 
        self.combobox_ente_fed = ttk.Combobox(self.quadro, values=opcoes_ente_fed) 
        self.combobox_ente_fed.grid(row=6, column=1)

 
        self.lblcod_porte = tk.Label(self.quadro, text="Codigo Porte: ")
        self.lblcod_porte.grid(row=7, column=0) 
        cod_porte = ["00", "01", "03", "05"]
        self.combobox_cod_porte = ttk.Combobox(self.quadro, values=cod_porte)
        self.combobox_cod_porte.grid(row=7, column=1)
        self.combobox_cod_porte.bind("<<ComboboxSelected>>", self.atualizarDescricaoPorte)

        
        self.lbldescricao_porte = tk.Label(self.quadro, text="Descricão de Porte: ")
        self.lbldescricao_porte.grid(row=7, column=5) 
        self.etydescricao_porte = tk.Entry(self.quadro)
        self.etydescricao_porte.grid(row=7, column=6)
 
  
        self.btnInserir = tk.Button(self.quadro, text="Inserir", command=self.inserir)
        self.btnInserir.grid(row=11, column=7)
        self.btnInserir.bind("<Button-1>", self.inserir)

        self.btnDeletar = tk.Button(self.quadro, text="Deletar")
        self.btnDeletar.grid(row=11, column=9)
        self.btnDeletar.bind("<Button-1>", self.Deletar)

        self.btnatualizar = tk.Button(self.quadro, text="Atualizar")
        self.btnatualizar.grid(row=11, column=8)
        self.btnatualizar.bind("<Button-1>", self.atualizar)

        self.btnBuscar = tk.Button(self.quadro, text="Buscar")
        self.btnBuscar.grid(row=0, column=2)
        self.btnBuscar.bind("<Button-1>", self.Buscar)

        
        columns = ('cnpj', 'razao_social', 'cod_natureza', 'descricao_natureza', 'qualificacao', 'cap_social', 'ente_fed', 'cod_porte', 'descricao_porte') 
        self.tree = ttk.Treeview(janela, columns=columns, show='headings')
        

        self.tree.column("cnpj", width=100)  
        self.tree.column("razao_social", width=300)  
        self.tree.column("cod_natureza", width=100)
        self.tree.column("descricao_natureza", width=200)  
        self.tree.column("qualificacao", width=100)  
        self.tree.column("cap_social", width=100)
        self.tree.column("ente_fed", width=100)  
        self.tree.column("cod_porte", width=100)  
        self.tree.column("descricao_porte", width=200)

       
        self.tree.heading('cnpj', text='Cnpj')
        self.tree.heading('razao_social', text='Razão Social')
        self.tree.heading('cod_natureza', text='Codigo de Natureza')
        self.tree.heading('descricao_natureza', text='Descricao de Natureza')
        self.tree.heading('qualificacao', text='Qualificaçao')
        self.tree.heading('cap_social', text='Capital Social')
        self.tree.heading('ente_fed', text='Ente Federativo')
        self.tree.heading('cod_porte', text='Codigo de Porte')
        self.tree.heading('descricao_porte', text='Descricao de Porte')

    
        self.scrollbar = ttk.Scrollbar(janela)
        self.scrollbar.pack( side = tk.RIGHT, fill=tk.Y )

        self.scrollbar.config( command = self.tree.yview )
        self.tree.config(yscrollcommand=self.scrollbar.set)

        self.tree.pack(fill=tk.BOTH, expand=tk.YES)

        self.tree.bind("<Double-1>", self.selecionarLinha)

        #self.atualizarTabela(self.EmpresasDAO.buscar())

    def atualizarTabela(self, registros):
        for item in self.tree.get_children():
            self.tree.delete(item)

        for registro in registros:
            self.tree.insert('', tk.END, values=registro)

    
    def selecionarLinha(self,event):
        item = self.tree.item( self.tree.selection() )
        self.etycnpj.delete(0, tk.END)
        self.etycnpj.insert(0, item['values'][0]) 
        self.etyrazao_social.delete(0, tk.END)
        self.etyrazao_social.insert(0, item['values'][1])
        self.combobox_cod_natureza.delete(0, tk.END)
        self.combobox_cod_natureza.insert(0, item['values'][2])
        self.etydescricao_natureza.delete(0, tk.END)
        self.etydescricao_natureza.insert(0, item['values'][3]) 
        self.combobox_qualificacao.delete(0, tk.END)
        self.combobox_qualificacao.insert(0, item['values'][4])
        self.etycap_social.delete(0, tk.END)
        self.etycap_social.insert(0, item['values'][5])
        self.combobox_ente_fed.delete(0, tk.END)
        self.combobox_ente_fed.insert(0, item['values'][6])
        self.combobox_cod_porte.delete(0, tk.END)
        self.combobox_cod_porte.insert(0, item['values'][7])
        self.etydescricao_porte.delete(0, tk.END)
        self.etydescricao_porte.insert(0, item['values'][8])
   

    def inserir(self, event=None):
        if (self.etycnpj.get() != '' or self.etyrazao_social.get() != '' or self.combobox_cod_natureza.get() != '' or self.etydescricao_natureza.get() != '' or self.etycap_social.get() != '' or self.combobox_qualificacao.get() != '' or self.combobox_ente_fed.get() != '' or self.combobox_cod_porte.get() != '' or self.etydescricao_porte.get() != ''):
            self.EmpresasDAO.inserir(self.etycnpj.get(), self.etyrazao_social.get(), self.combobox_cod_natureza.get(), self.etydescricao_natureza.get(), self.combobox_qualificacao.get(), self.etycap_social.get(), self.combobox_ente_fed.get(), self.combobox_cod_porte.get(), self.etydescricao_porte.get())
            self.atualizarTabela(self.EmpresasDAO.buscarPorCnpj(self.etycnpj.get()))
        else:
            mb.showinfo('Informação', 'É necessário informar CNPJ e Razão Social')



    def Deletar(self, event):
        cnpj = self.etycnpj.get()
        if cnpj != '':
            self.EmpresasDAO.deletar(cnpj)
            self.atualizarTabela(self.EmpresasDAO.buscarPorCnpj(self.etycnpj.get()))
        else:
            mb.showinfo('Informação', 'É necessário informar o CNPJ para excluir')


    def atualizar(self, event):
        if(self.etycnpj.get() != '' or self.etyrazao_social.get() != ''):
            cnpj=self.etycnpj.get()
            self.EmpresasDAO.atualizar(self.etycnpj.get(), self.etyrazao_social.get(), self.combobox_cod_natureza.get(), self.etydescricao_natureza.get(), self.combobox_qualificacao.get(), self.etycap_social.get(), self.combobox_ente_fed.get(), self.combobox_cod_porte.get(), self.etydescricao_porte.get())
            self.atualizarTabela(self.EmpresasDAO.buscarPorCnpj(cnpj))
        else:
            mb.showinfo('Informação', 'É necessário informar código e nome')


    def Buscar(self, event):
        if self.etycnpj.get() != '':
            self.atualizarTabela(self.EmpresasDAO.buscarPorCnpj(self.etycnpj.get()))
        elif self.etyrazao_social.get() != '':
            self.atualizarTabela(self.EmpresasDAO.buscarPorPrimeiroNome(self.etyrazao_social.get()))
        else:
            self.atualizarTabela(self.EmpresasDAO.buscar())
          

    def obterDescricaoPorte(self, codigo_porte):
        descricao_porte = {
            "00": "Porte não informado",
            "01": "Micro empresa",
            "03": "Empresa de pequeno porte",
            "05": "Demais"
        }
        return descricao_porte.get(codigo_porte, "Descrição não encontrada")


    def atualizarDescricaoPorte(self, event):
        codigo_porte = self.combobox_cod_porte.get()
        descricao_porte = self.obterDescricaoPorte(codigo_porte)

        if descricao_porte:
            self.etydescricao_porte.delete(0, tk.END)
            self.etydescricao_porte.insert(0, descricao_porte)

    def abrirOpcoesPorte(self):
        self.combobox_cod_porte.focus_set()
        self.combobox_cod_porte.event_generate('<Down>')
        self.combobox_cod_porte.bind("<<ComboboxSelected>>", self.atualizarDescricaoPorte)


    def atualizarOpcoesEnteFed(self, event):
        opcoes_ente_fed = [" 1 ", " 2 ", " 3","5"]
        self.combobox_ente_fed['values'] = opcoes_ente_fed
        self.etycod_ente_fed.delete(0, tk.END)
        self.etydescricao_ente_fed.delete(0, tk.END)


    def atualizarDescricaoNatureza(self, event):
        codigo_natureza = self.combobox_cod_natureza.get()
        descricao_natureza = self.NaturezaJuridicaDAO.buscarDescricaoNatureza(codigo_natureza)

        if descricao_natureza:
            self.etydescricao_natureza.delete(0, tk.END)
            self.etydescricao_natureza.insert(0, descricao_natureza)



    def preencherCodigosNatureza(self,):
        codigos_natureza = self.NaturezaJuridicaDAO.buscarTodosCodigosNatureza()
        self.combobox_cod_natureza['values'] = codigos_natureza

     

   
