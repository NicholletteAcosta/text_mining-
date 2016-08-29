import mechanize

def getHtmlText(links):
	links_dict ={}
	for i in links:
		url = i
		br = mechanize.Browser()
		htmltext = br.open(url).read()
		links_dict[url] = htmltext
		#print htmltext
	return links_dict
	
def getHtmlFile(url):
	br = mechanize.Browser()
	htmlfile = br.open(url)
	return htmlfile