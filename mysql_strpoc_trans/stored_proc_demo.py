from mysql.connector import Error
from hcl_database_connectivity import MysqlDataConnection
class HclStoredProcedure(MysqlDatabaseConnection):
    def execute_str_procedure(self):
        try:
            self.cursor.callproc("get_cust")
            for r in self.cursor.stored_results():
                print(r.fetchall())
        except Exception as e:
            print(e)
        finally:
            if(self.connection.is_connected()):
                self.cursor.close()
                self.connection.close()
connect_obj=HclPythonTranscation()
connect_obj.connect("localhost","root","Sanjeev123","hcl_vijaywada")
connect_obj.excuete_transcation_query()