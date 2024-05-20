from PySide6.QtSql import QSqlDatabase, QSqlQueryModel
from PySide6.QtCore import Qt
import pandas as pd
import sqlite3



#con = sqlite3.connect(r"\\nas01.via.varejo.corp\gremio01\OPER_LOGISTICA\JUNDIAI\19_CONTROLE\00_Arquivos diversos\Luiz Henrique\controleAtivos.db")
con = sqlite3.connect('controleAtivos.db')       
sqlString = f'''
                SELECT tblControle.Matricula, tblColaboradores.Nome, tblColaboradores.Turno, tblEmpresas.Empresa, tblControle.DtEntrada,tblControle.HrEntrada , tblControle.DtSaida, tblControle.HrSaida   FROM tblControle
                LEFT JOIN tblColaboradores ON tblControle.Matricula = tblColaboradores.Matricula
                LEFT JOIN tblEmpresas ON tblColaboradores.idEmpresa = tblEmpresas.idEmpresa
            '''

df = pd.read_sql(sqlString,con=con)





print(df)
