import json,re
import demjson
from elasticsearch import Elasticsearch,helpers

demjson.decode('{foo:3}')
def fixJson(strjson):
	strjson = re.sub(r"{\s*(\w)", r'{"\1', strjson)
	strjson = re.sub(r",\s*(\w)", r',"\1', strjson)
	strjson = re.sub(r"(\w):", r'\1":', strjson)
	return strjson


#es = Elasticsearch(['http://search-beevagrad-yzavdnk3vgybj33teqgucq7ray.us-east-1.es.amazonaws.com'])
es = Elasticsearch(['http://search-beevagrad-yzavdnk3vgybj33teqgucq7ray.us-east-1.es.amazonaws.com:80'])
#es = Elasticsearch(['https://search-beevagrad-yzavdnk3vgybj33teqgucq7ray.us-east-1.es.amazonaws.com:9200'])
filename = '/home/administradorcito/Descargas/mongo/users.txt'
with open(filename, 'r') as myfile:
	data=myfile.read().replace('\n', '').replace('\t', '')

d = demjson.decode(data)

actions = []
for i in d:
	copy = i
	iddoc = int(copy["_id"])
	del copy["_id"]
	#action = {
	#	"_index": "oswaldo",
	#	"_type": "users",
	#	"_id": iddoc,
	#	"_source": i
	#	}
	#actions.append(action)
	#print(copy)
	res = es.index(index="oswaldo", doc_type='users', id=iddoc, body=copy)
	print(res)
#helpers.bulk(es, actions)