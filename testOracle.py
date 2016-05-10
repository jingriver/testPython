import cx_Oracle

# connect via SQL*Net string or by each segment in a separate argument
#connection = cx_Oracle.connect("user/password@TNS")
connection = cx_Oracle.connect("bexschema", "bex", "BEXQA")

cursor = connection.cursor()

with open("c:\\assignments\\savedsearch\qds.txt") as f:
    cnt = 0
    lasttype = 'CQD'
    for line in f:
        line = line.strip()
        if len(line)==0:
            continue
        (searchtype, name) = line.split("\t")        
        
        if searchtype!=lasttype:
            cnt+=20
        else:
            cnt+=1
        
        print cnt, searchtype, name
        lasttype = searchtype
        
#        cursor.execute("""
#            insert into saved_searches_cfg (cfg_id, search_type, parameter_name)
#            values (:id, :type, :para_name)
#            """,
#            {'id':cnt,
#             'type':searchtype,
#             'para_name':name}
#            )
#        
#connection.commit()
cursor.execute("""
        select cfg_id, search_type, parameter_name
        from saved_searches_cfg
        """)
for col_1, col_2, col_3 in cursor:
    print "Values:", col_1, col_2, col_3

cursor.close()    
connection.close()

