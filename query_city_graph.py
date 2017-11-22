from neo4j.v1 import GraphDatabase


def print_friends_of(driver, city_name):
    with driver.session() as session:
        with session.begin_transaction() as tx:
            query_str = 'MATCH p=(my_city:City)-[:KNOWS*1..2]-(friend_city) WHERE my_city.name = "%s"  ' \
                        'RETURN my_city,friend_city,relationships(p)' % city_name
            for record in tx.run(query_str):
                print(record['friend_city'].properties['name'])
                for rel in (record['relationships(p)']):
                    print("\t%s -> %s" % (get_node_name_by_id(tx, rel.start), get_node_name_by_id(tx, rel.end)))


def get_node_name_by_id(tx, id_str):
    query_str = 'MATCH (n) WHERE ID(n) = %s RETURN n' % id_str
    rec = tx.run(query_str)
    for record in rec:
        return record['n'].properties['name']


if __name__ == '__main__':
    uri = "bolt://localhost:7687"
    neo4j_driver = GraphDatabase.driver(uri, auth=("", ""))
    print_friends_of(neo4j_driver, "shanghai")
