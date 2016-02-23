import psycopg2

ip_start = ['192.168.0.','10' ]
ip_join = ip_start[0] + ip_start[1]  
try:
    conn = psycopg2.connect("dbname='test' user='postgres' host='localhost' password='1234' port='5432'")
except:
    print ("błąd")
cur = conn.cursor()
cur.execute("""SELECT ip from ip_test""")

rows = cur.fetchall()
for row in rows:
    if row[0] == ip_join:
        a = int(ip_start[1]) + 1
        ip_start[1] = str(a)
        ip_join = ip_start[0] + ip_start[1]
        
   
        
        
cur.execute("INSERT INTO ip_test(ip) VALUES ('{0}')".format(ip_join))
conn.commit()

for row in rows:
    print (row)
cur.close()
conn.close()        

