
import duckdb
# Helper for DuckDB access

duckdbconn='KlimaPi.duckdb'
    
def ExecuteDuckDBQuery(query):
    try:
        conn = duckdb.connect(duckdbconn)
        cur = conn.cursor()
        cur.execute(query)
        res = cur.fetch_df()
        cur.close()
        conn.close()
    except Exception as e:
        res = -1
        print(e.message)
    finally:
        return res
    
def InsertOrUpdateDuckDB(insertquery):
    try:
        conn = duckdb.connect(duckdbconn)
        cur = conn.cursor()
        cur.execute(insertquery)
        res = 1
        cur.close()
        conn.close()
    except Exception as e:
        res = -1
        print(e.message)
    finally:
        return res
    