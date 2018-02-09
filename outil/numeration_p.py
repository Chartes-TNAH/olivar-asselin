# placer le script dans le dossier avec les documents dans lesquels ont veut inclure la numérotation
def numerotation(fichier_xml):

	with open (fichier_xml) as xml :
		texte = xml.read()
		mots = texte.split("<")
	i = 1
	texte_numerote = ""
	for mot in mots : 

		if mot.startswith('p>'):

			mot = mot.replace('p>', 'p n="' + str(i) + '">') 
			i+=1
		texte_numerote += "<"+mot
		texte_numerote = texte_numerote.replace("<<", "<")

	with open (fichier_xml, "w" ) as xml :
		xml.write(texte_numerote)


for i in range(14, 16): #noter ici (numero_premiere_lettre, numero_derniere_lettre+1) 
	numerotation("wikidQ3350623.wikid2.wikid" + str(i) + ".xml")
