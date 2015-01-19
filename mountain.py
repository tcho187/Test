mountain= {

	"Mount Everest":{"height":8848,"Range":"Mahalangur Himalaya"},
	"Kangchenjunga":{"height":8586,"Range":"Kangchenjunga Himalaya"},
	"Makalu":{"height":8485,"Range":"Mahalangur Himalaya"},
	"Dhaulagiri I":{"height":8167,"Range":"Dhaulagiri Himalaya"},
	"Nanga Parbat":{"height":8126,"Range":"Nanga Parbat Himalaya"},
	"Annapurna I":{"height":8091,"Range":"Annapurna Himalaya"},
	"Manaslu":{"height":8163,"Range":"Manaslu Himalaya"},
	"Cho Oyu":{"height":8188,"Range":"Mahalangur Himalaya"},
	"Lhotse":{"height":8516,"Range":"Mahalangur Himalaya"},
	"K2":{"height":8611,"Range":"Baltoro Karakoram"}
}
print "Do you want to know the height of the tallest mountains in alphabetical order?:"
user_input=raw_input().lower()

if user_input == "yes" or user_input == "y":
	#sorts out alphabetically mountain dictionary becomes a sorted list by the first value of the tuple
	
	for x,mountain[x] in sorted(mountain.items(), key=lambda tup: tup[0]):
		print x +" is " + str(mountain[x]['height'])+ " meters tall and is in the " + str(mountain[x]["Range"]) + " range."
		"\n"
	print "Do you also want to know the height of the mountains from tallest to shortest?"
	temp=raw_input().lower()
	if temp == "yes" or temp == "y":
		#sorts from tallest to shortest by the second value of the tuple, reverse from tallest to shortest
		for x,mountain[x] in sorted(mountain.items(), key=lambda tup: tup[1],reverse=True):
			print x +" is " + str(mountain[x]["height"])+ " meters."
	else:
		print "ok"
else:
	print "ok"






