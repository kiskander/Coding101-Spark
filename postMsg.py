import pyCiscoSpark as Spark
import pprint


auth = 'INSERT AUTH HERE'
roomId = 'Y2lzY29zcGFyazovL3VzL1JPT00vNTZmOGM4ZjAtMTI4Ny0xMWU4LWI2MzYtYjcwOGNjMzRmMzE4'
pp = pprint.PrettyPrinter(indent=4)

resp = Spark.post_message(auth, roomId, "Hello World")
pp.pprint(resp)