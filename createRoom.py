import pyCiscoSpark as Spark
import pprint


auth = 'INSERT AUTH HERE'
pp = pprint.PrettyPrinter(indent=4)

resp = Spark.post_createroom(auth,"TestRoom")
pp.pprint(resp)