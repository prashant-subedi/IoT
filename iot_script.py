import requests
import json
import sys
import time
refresh_time=2
req="""http://"""+sys.argv[1] + """/pi"""
print(req)
while True:
	a=time.time()
	response=json.loads(requests.get(req).text)
	print(response)
	for i in response:
		#do action
		pass
	diff=refresh_time-(time.time()-a)
	if diff<0:
		continue
	time.sleep(diff)
