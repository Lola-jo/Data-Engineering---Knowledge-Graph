from py2neo import Graph, Node, Relationship

##连接neo4j数据库，输入地址、用户名、密码
graph = Graph('http://localhost:7474', username='neo4j', password='password')
# graph.delete_all()

# 同一个 label 中，所有节点的颜色是相同的
label_1 = "dnn_1"
label_2 = "dnn_2"
relation_name = "CRIME"

# 节点
node_1 = Node(label_1, name="案件1")
node_2 = Node(label_1, name="案件2")
node_3 = Node(label_1, name="案件3")
node_a = Node(label_2, name="A")
node_b = Node(label_2, name="B")
node_c = Node(label_2, name="C")
node_d = Node(label_2, name="D")
node_e = Node(label_2, name="E")
node_f = Node(label_2, name="F")
node_g = Node(label_2, name="G")
node_h = Node(label_2, name="H")

# 创建节点
graph.create(node_1)
graph.create(node_2)
graph.create(node_3)
graph.create(node_a)
graph.create(node_b)
graph.create(node_c)
graph.create(node_d)
graph.create(node_e)
graph.create(node_f)
graph.create(node_g)
graph.create(node_h)

# 关系
relation_1_a = Relationship(node_1, relation_name, node_a)
relation_1_b = Relationship(node_1, relation_name, node_b)
relation_1_c = Relationship(node_1, relation_name, node_c)
relation_1_d = Relationship(node_1, relation_name, node_d)
relation_2_c = Relationship(node_2, relation_name, node_c)
relation_2_b = Relationship(node_2, relation_name, node_b)
relation_2_e = Relationship(node_2, relation_name, node_e)
relation_3_f = Relationship(node_3, relation_name, node_f)
relation_3_g = Relationship(node_3, relation_name, node_g)
relation_3_h = Relationship(node_3, relation_name, node_h)

# 创建关系
graph.create(relation_1_a)
graph.create(relation_1_b)
graph.create(relation_1_c)
graph.create(relation_1_d)
graph.create(relation_2_c)
graph.create(relation_2_b)
graph.create(relation_2_e)
graph.create(relation_3_f)
graph.create(relation_3_g)
graph.create(relation_3_h)

