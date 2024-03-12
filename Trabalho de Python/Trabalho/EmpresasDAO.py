import sqlite3

class EmpresasDAO:
    def abrirConexao(self):
        try:
            self.conexao = sqlite3.connect("trabalho.db")
            self.cursor = self.conexao.cursor()

            return True
        except sqlite3.DatabaseError as error:
            print("Erro na conexao:", error)
            return False
        
    def fecharConexao(self):
        if(self.conexao):
            self.cursor.close()
            self.conexao.close()

    def buscar(self):
        if(self.abrirConexao()):
            self.cursor.execute("select * from Empresas")
            resultado = self.cursor.fetchall()
            self.fecharConexao() 
            return resultado
        else:
            return None
        
    
    def buscarPorPrimeiroNome(self, primeiro_nome):
        if(self.abrirConexao()):
            self.cursor.execute("SELECT * FROM Empresas WHERE SUBSTR(razao_social, 1, INSTR(razao_social, ' ') - 1) = ?", (primeiro_nome,))
            resultado = self.cursor.fetchall()
            self.fecharConexao()
            return resultado
        else:
            return None



    def buscarPorCnpj(self, cnpj):
        if self.abrirConexao():
            self.cursor.execute("SELECT * FROM Empresas WHERE cnpj = ?", (cnpj,))
            resultado = self.cursor.fetchall()
            self.fecharConexao()
            return resultado
        else:
            return None

        
    def inserir(self,cnpj, razao_social, cod_natureza, descricao_natureza, qualificacao, cap_social, ente_fed, cod_porte, descricao_porte):
         if(self.abrirConexao()):
            try:
                self.cursor.execute("INSERT INTO Empresas (cnpj, razao_social, cod_natureza, descricao_natureza, qualificacao, cap_social, ente_fed, cod_porte, descricao_porte) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
                               (cnpj, razao_social, cod_natureza, descricao_natureza, qualificacao, cap_social, ente_fed, cod_porte, descricao_porte))
                self.conexao.commit()
                self.fecharConexao()
            except sqlite3.DatabaseError as erro:
                print(erro) 
 

        
    def deletar(self, cnpj):
         if(self.abrirConexao()):
            try:
                self.cursor.execute("DELETE FROM Empresas WHERE cnpj  = ?", (cnpj,))          
                self.conexao.commit()
                self.fecharConexao()
            except sqlite3.DatabaseError as erro:
                print(erro) 
    

    def atualizar(self, cnpj, novo_nome, novo_cod_natureza, nova_descricao_natureza, nova_qualificacao, novo_cap_social, novo_ente_fed, novo_cod_porte, nova_descricao_porte):
        if(self.abrirConexao()):
            try:
                self.cursor.execute("UPDATE Empresas SET cnpj =?, razao_social = ?, cod_natureza = ?, descricao_natureza = ?, qualificacao = ?, cap_social = ?, ente_fed = ?, cod_porte = ?, descricao_porte = ? WHERE cnpj = ?", 
                                (cnpj,novo_nome, novo_cod_natureza, nova_descricao_natureza, nova_qualificacao, novo_cap_social, novo_ente_fed, novo_cod_porte, nova_descricao_porte, cnpj))
                self.conexao.commit()
                self.fecharConexao()
            except sqlite3.DatabaseError as erro:
                print(erro)



    def buscarPorte(self):
        cursor = self.conexao.cursor()
        cursor.execute("SELECT * FROM Porte")
        return cursor.fetchall()

    def inserirPorte(self, cod_porte, descricao_porte):
        cursor = self.conexao.cursor()
        cursor.execute("INSERT INTO Porte (cod_porte, descricao_porte) VALUES (?, ?)", (cod_porte, descricao_porte))
        self.conexao.commit()

    def atualizarPorte(self, cod_porte, descricao_porte):
        cursor = self.conexao.cursor()
        cursor.execute("UPDATE Porte SET descricao_porte = ? WHERE cod_porte = ?", (cod_porte, descricao_porte,))
        self.conexao.commit()

    def deletarPorte(self, cod_porte, descricao_porte):
        cursor = self.conexao.cursor()
        cursor.execute("DELETE FROM Porte WHERE cod_porte = ?", (cod_porte, descricao_porte))
        self.conexao.commit()


    def inserircod_natureza(self):
        cnpj = self.etycnpj.get()
        razao_social = self.etyrazao_social.get()
        cod_natureza = self.etycod_natureza.get()
        qualificacao = self.etyqualificacao.get()
        cap_social = self.etycap_social.get()
        ente_fed = self.etyente_fed.get()
        cod_porte = self.etycod_porte.get()
        
        self.EmpresasDAO.inserirComDescricaoNatureza(cnpj, razao_social, cod_natureza, qualificacao, cap_social, ente_fed, cod_porte)
 


        
