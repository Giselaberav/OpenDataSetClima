from sqlalchemy import create_engine
import urllib
from sqlalchemy import text


def connect_with_sqlalchemy():
    servervar = 'svrtfmtrafficdb.database.windows.net'
    database1 = 'Traffic_Congestion'
    username = 'admintfm'
    password = 'TfmAdmin25*'
    
    # Create connection string
    params = urllib.parse.quote_plus(
        f"Driver={{ODBC Driver 17 for SQL Server}};"
        f"Server={servervar};"
        f"Database={database1};"
        f"Uid={username};"
        f"Pwd={password};"
        f"Encrypt=yes;"
        f"TrustServerCertificate=yes;"
        f"CertificateFile=/tmp/BaltimoreCyberTrustRoot.crt.pem;"
        f"Connection Timeout=90;"
    )
    connection_url = f"mssql+pyodbc:///?odbc_connect={params}"
    
    try:
        engine = create_engine(connection_url)
        connection = engine.connect()
        print("Connected using SQLAlchemy!")
        
        # Execute query
        
        query = text("SELECT count(*) as count from autos_traffic")
        result = connection.execute(query)

       # result = connection.execute("SELECT count(*) from autos_traffic")
        print("\nSQL Server Result from autos_traffic table:")
        for row in result:
            print(row.count)
            
    except Exception as e:
        print(f"Connection error: {e}")
      
    finally:
        if 'connection' in locals():
            connection.close()
            print("\nConnection closed.")
            return engine
            
            
def savedftosql(df):
    #servervar = 'localhost'
    #database1 = 'Traffic_Congestion'
    #username = 'sa'
    #password = 'Gitanilla77*'
    
    servervar = 'svrtfmtrafficdb.database.windows.net'
    database1 = 'Traffic_Congestion'
    username = 'admintfm'
    password = 'TfmAdmin25*'
    
    # Create connection string
    params = urllib.parse.quote_plus(
        f"Driver={{ODBC Driver 17 for SQL Server}};"
        f"Server={servervar};"
        f"Database={database1};"
        f"Uid={username};"
        f"Pwd={password};"
        f"Encrypt=yes;"
        f"TrustServerCertificate=yes;"
        f"CertificateFile=/tmp/BaltimoreCyberTrustRoot.crt.pem;"
        f"Connection Timeout=120;"
    )
    
    connection_url = f"mssql+pyodbc:///?odbc_connect={params}"
    
    try:
        engine = create_engine(connection_url, isolation_level="AUTOCOMMIT")
        connection = engine.connect()
        #conn_str = f"DRIVER={driversql};SERVER={servervar};DATABASE={database1};UID={username};PWD={password}"
        #onnection = pyodbc.connect(conn_str)

        print('conectado a la bd y traido el engine, subiendo data a la bd')
        if connection.in_transaction():
            connection.rollback()
       
        with engine.connect() as fresh_connection:
            df.to_sql('DATOS_CLIMA', con=fresh_connection, if_exists='append', index=False)
            
        connection.close()
        print("data importada successfully")
            
    except Exception as e:
        print(f"Connection error: {e}")
        
    finally:
        if 'connection' in locals():
            connection.close()
            print("\nConnection closed.")