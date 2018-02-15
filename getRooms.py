import pyCiscoSpark as Spark
import pprint


auth = 'INSERT AUTH HERE'
pp = pprint.PrettyPrinter(indent=4)

resp = Spark.get_rooms(auth)
pp.pprint(resp)