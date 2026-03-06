import os
import cx_Oracle
import pandas as pd

#os.environ["NLS_LANG"] = "JAPANESE_JAPAN.JA16SJISTILDE"

HOST = ""
PORT = 
SVS = ""
USER = ""
PASS = ""

sql_query = """
SELECT * FROM "TKG201"."M_MD_KAMIKOTEI_2_APC"
WHERE ROWNUM <= 10
"""

# dfを初期化（エラー時に備える）
df_db= pd.DataFrame()
conn = None
try:
    # 2. データベース接続
    dsn = cx_Oracle.makedsn(HOST, PORT, service_name=SVS)
    conn = cx_Oracle.connect(USER, PASS, dsn)
    
    # 3. データ読み込み
    df_db = pd.read_sql(sql_query, conn)
    print("データの取得に成功しました。")

except Exception as e:
    print(f"エラーが発生しました: {e}")

finally:
    # 4. 接続を必ず閉じる
    if conn:
        conn.close()

print(df_db)
