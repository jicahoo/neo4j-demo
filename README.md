# neo4j-demo
Some common tasks can be done by neo4j

# Query City Graph
## Step of Demo (on Windows)
1. Install neo4j and start server.
  * Download: https://neo4j.com/download/ You will get a exe: neo4j-desktop-1.0.4-setup.exe.
  * Just install exe. It may require you to login with some SNS account (like google account)
  * Use the neo desktop to create a LOCAL database. LOCAL database don't need username/password. And start the database server.
2. Prepare data using below statements.
  * Open created database and click `manage->Open Browser`. 
  ![screenshot](asssets/All_Cities.svg "Logo Title Text 1")

```cypher
CREATE (beijing: City {name:"beijing"} ),
(shanghai: City {name:"shanghai"} ),
(qingdao: City {name:"qingdao"} ), 
(zhengzhou: City {name:"zhengzhou"} ), 
(xining: City {name:"xining"} ),
(xian: City {name:"xian"} ),
(xiamen: City {name:"xiamen"} ),
(guangzhou: City {name:"guangzhou"} ),
(zhuhai: City {name:"zhuhai"} ),
(guilin: City {name:"guilin"} ),
(kunming: City {name:"kunming"} ),
(chengdu: City {name:"chengdu"} ),
(xizang: City {name:"xizang"} ),
(beijing)-[:KNOWS]->(qingdao),
(shanghai)-[:KNOWS]->(guangzhou),
(guangzhou)-[:KNOWS]->(xiamen),
(shanghai)-[:KNOWS]->(zhengzhou),
(zhengzhou)-[:KNOWS]->(qingdao),
(beijing)-[:KNOWS]->(xian),
(xining)-[:KNOWS]->(xian),
(xian)-[:KNOWS]->(chengdu),
(chengdu)-[:KNOWS]->(xizang),
(zhengzhou)-[:KNOWS]->(kunming),
(guangzhou)-[:KNOWS]->(zhuhai),
(zhuhai)-[:KNOWS]->(guilin),
(beijing)-[:KNOWS]->(guangzhou)
```

2. Install python driver (http://neo4j.com/docs/api/python-driver/current/)
```bash
pip install neo4j-driver
```
3. Just run Python script:
