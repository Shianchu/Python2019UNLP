import time
ahora=time.time()
while True:
	if time.time()-ahora<10:
		print (time.time()-ahora)
		time.sleep(0.5)
	else:
		ahora=time.time()
	
