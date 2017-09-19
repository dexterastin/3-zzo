dbfilename = 'test3_2.dat'

def readScoreDB():
	try:
		fH = open(dbfilename)
	except FileNotFoundError as e:
		print("New DB: ", dbfilename)
		return []
	else:
		print("Open DB: ", dbfilename)

	scdb = []
	for line in fH:
		dat = line.strip()
		person = dat.split(",")
		record = {}
		for attr in person:
			kv = attr.split(":")
			record[kv[0]] = kv[1]
		scdb += [record]
	fH.close()
	return scdb


# write the data into person db
def writeScoreDB(scdb):
	fH = open(dbfilename, 'w')
	for p in scdb:
		pinfo = []
		for attr in p:
			pinfo += [attr + ":" + p[attr]]
		line = ','.join(pinfo)
		fH.write(line + '\n')
	fH.close()

def doScoreDB(scdb):
	while(True):
		try:
			inputstr = (input("Score DB > "))
			if inputstr == "": continue
			parse = inputstr.split(" ")
			if parse[0] == 'add':
				try:
					int(parse[2])
					int(parse[3])
					record = {'Name':parse[1], 'Age':parse[2], 'Score':parse[3]}
					scdb += [record]
				except ValueError:
					print("Use to Correct")


			elif parse[0] == 'del':
				count = 0
				for a in range(len(scdb)):
					for b in range(len(scdb)-a):
						for b in scdb:
							if b['Name'] == parse[1]:
								scdb.remove(b)
							else:
								count = count +1
				if count > len(scdb):
					print("No exist Data")
				else:
					pass



			elif parse[0] == 'show':
				sortKey ='Name' if len(parse) == 1 else parse[1]
				showScoreDB(scdb, sortKey)
			elif parse[0] == 'quit':
				break


			elif parse[0] == 'find':
				count =0
				for t in scdb:
					if t['Name'] == parse[1]:
						print("Name :", t['Name'] +" Age :",  t['Age'] + " Score :", t['Score'])
					else:
						count = count +1
				if count == len(scdb):
					print("No exist Data")
				else:
					pass



			elif parse[0] == 'inc':
				count =0
				for s in scdb:
					try:
						if s['Name'] == parse[1]:
							scdb[count]['Score'] = str(int(s['Score'])+int(parse[2]))
							print(scdb[count]['Score'])
						else:
							count = count + 1
					except ValueError:
						print("Use to correct")


			elif parse[0] == 'best':
				Best =0
				for t in range(len(scdb)):
					if int(scdb[t]['Score']) > Best:
						Best = int(scdb[t]['Score'])
					else:
						Best = Best
				print(Best)

			elif parse[0] == 'worst':
				worst = int(scdb[0]['Score'])
				for t in range(len(scdb)):
					if int(scdb[t]['Score']) < worst:
						worst = int(scdb[t]['Score'])
					else:
						worst = worst
				print(worst)
			else:
				print("Invalid command: " + parse[0])
		except IndexError:
			print("Use to correct")
			print("Ex) add Son 20 90")
			print("Ex) del Son")
			print("Ex) find Son")
			print("Ex) inc Son 10")
			

def showScoreDB(scdb, keyname):
	for p in sorted(scdb, key=lambda person: person[keyname]):
		for attr in sorted(p):
			print(attr + "=" + p[attr], end=' ')
		print()
	


scoredb = readScoreDB()
doScoreDB(scoredb)
writeScoreDB(scoredb)

