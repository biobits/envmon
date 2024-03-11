
import duckdb
# Helper for DuckDB access

duckdbconn='KlimaPi.duckdb'
    
def ExecuteDuckDBQuery(query,params=None):
    try:
        conn = duckdb.connect(duckdbconn)
        cur = conn.cursor()
        cur.execute(query,params)
        res = cur.fetchall()
        cur.close()
        conn.close()
    except Exception as e:
        res = -1
        print(e.message)
    finally:
        return res
    
def ExecuteDuckDBQueryDf(query,params=None):
    try:
        conn = duckdb.connect(duckdbconn)
        cur = conn.cursor()
        cur.execute(query,params)
        res = cur.fetch_df()
        cur.close()
        conn.close()
    except Exception as e:
        res = -1
        print(e.message)
    finally:
        return res
    
def InsertOrUpdateDuckDB(insertquery,params):
    try:
        conn = duckdb.connect(duckdbconn)
        cur = conn.cursor()
        cur.execute(insertquery,params)
        res = 1
        cur.close()
        conn.close()
    except Exception as e:
        res = -1
        print(e.message)
    finally:
        return res
    