import sqlite3

class naturezajuridicaDAO:
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
            self.cursor.execute("select * from natureza_juridica")
            resultado = self.cursor.fetchall()
            self.fecharConexao() 
            return resultado
        else:
            return None
        
    def buscarPorcodigo(self, cod_natureza):
        if(self.abrirConexao()):
            self.cursor.execute("select * from natureza_juridica where cod_natureza = ?",(cod_natureza))
            resultado = self.cursor.fetchone()
            self.fecharConexao() 
            return resultado
        else:
            return None
        

    def inserir(self, cod_natureza, descricao_natureza):
         if(self.abrirConexao()):
            try:
                self.cursor.execute("insert into natureza_juridica (cod_natureza, descricao_natureza) values (?,?)",(cod_natureza,descricao_natureza))            
                self.conexao.commit()
                self.fecharConexao()
            except sqlite3.DatabaseError as erro:
                print(erro) 
            


    def deletar(self, cod_natureza):
         if(self.abrirConexao()):
            try:
                self.cursor.execute("DELETE FROM natureza_juridica WHERE cod_natureza = ?",(cod_natureza,))            
                self.conexao.commit()
                self.fecharConexao()
            except sqlite3.DatabaseError as erro:
                print(erro) 
    
    def atualizar(self,cod_natureza, descricao_natureza):
         if(self.abrirConexao()):
            try:
                self.cursor.execute("UPDATE Empresas SET cod_natureza=?, descricao_natureza=? where cnpj = ?",(cod_natureza, descricao_natureza))            
                self.conexao.commit()
                self.fecharConexao()
            except sqlite3.DatabaseError as erro:
                print(erro) 
    

    def buscarTodosCodigosNatureza(self):
        try:
            if self.abrirConexao():
                self.cursor.execute("SELECT cod_natureza FROM Natureza_Juridica")
                codigos = [row[0] for row in self.cursor.fetchall()]
                self.fecharConexao()
                return codigos
            else:
                return []
        except sqlite3.Error as error:
            print("Erro ao buscar todos os códigos de natureza:", error)
            return []



    def buscarDescricaoNatureza(self, descricao_natureza):
        if self.abrirConexao():
            self.cursor.execute("SELECT descricao_natureza FROM Natureza_Juridica WHERE cod_natureza = ?", (descricao_natureza,))
            resultado = self.cursor.fetchone()
            self.fecharConexao()
            if resultado:
                return resultado[0]  
        return None  
   