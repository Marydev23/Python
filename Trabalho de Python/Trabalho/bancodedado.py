import sqlite3
import csv  # Importe o módulo csv

conexao = None

try:
    conexao = sqlite3.connect("trabalho.db")
    cursor = conexao.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Natureza_Juridica (
            cod_natureza TEXT PRIMARY KEY,
            descricao_natureza TEXT
        );
    """)

    with open('Trabalho/NaturezaJuridica.csv', 'r', newline='', encoding='latin-1') as csv_file: 
        csv_reader = csv.reader(csv_file, delimiter=';')  
        next(csv_reader) 
        for row in csv_reader:
            cursor.execute("INSERT OR REPLACE INTO  Natureza_Juridica (cod_natureza, descricao_natureza) VALUES (?, ?)", row)


    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Porte (
            cod_porte TEXT PRIMARY KEY,
            descricao_porte TEXT
        );
    """)


    cursor.execute("INSERT OR REPLACE INTO Porte (cod_porte, descricao_porte) VALUES (?, ?)", ('00', 'Porte não informado'))
    cursor.execute("INSERT OR REPLACE INTO Porte (cod_porte, descricao_porte) VALUES (?, ?)", ('01', 'Micro empresa'))
    cursor.execute("INSERT OR REPLACE INTO Porte (cod_porte, descricao_porte) VALUES (?, ?)", ('03', 'Empresa de pequeno porte'))
    cursor.execute("INSERT OR REPLACE INTO Porte (cod_porte, descricao_porte) VALUES (?, ?)", ('05', 'Demais'))

    
    conexao.commit()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Empresas (
            cnpj INTEGER PRIMARY KEY,
            razao_social TEXT NOT NULL,
            cod_natureza TEXT NOT NULL,
            descricao_natureza TEXT NOT NULL,   
            qualificacao TEXT NOT NULL,
            cap_social REAL NOT NULL,
            ente_fed INTEGER,
            cod_porte INTEGER,
            descricao_porte TEXT,
            FOREIGN KEY (cod_natureza) REFERENCES Natureza_Juridica(cod_natureza),
            FOREIGN KEY (cod_porte) REFERENCES Porte(cod_porte)
        );
    """)

    with open('Trabalho/empresas.csv', 'r', newline='', encoding='latin-1') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        next(csv_reader)
        for row in csv_reader:
            while len(row) < 9:
                row.append(None)
            cursor.execute("INSERT OR REPLACE INTO Empresas (cnpj, razao_social, cod_natureza, descricao_natureza, qualificacao, cap_social, ente_fed, cod_porte, descricao_porte) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", row)

        
    cursor.execute("""
        UPDATE Empresas 
                   SET descricao_natureza = (SELECT descricao_natureza FROM Natureza_Juridica WHERE cod_natureza = Empresas.cod_natureza)
    """)

except sqlite3.Error as erro:
    print(f"Erro: {erro}")

finally:
    if conexao:
        conexao.commit()
        conexao.close()
