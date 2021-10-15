#!/usr/bin/python3
# -*- coding: utf-8 -*-

import xml.etree.ElementTree as ET
import os
lang=1;



nameDic={}


def writePage(lag,f,root):

	f.write("<head><meta charset=\"UTF-8\"></head>")
	link= "<link href=\"style.css\" rel=\"stylesheet\">"
	link= "<link href=\"../../style.css\" rel=\"stylesheet\">"


	# f.write("<div class=\"mainLeft\" ></div>")
	# f.write("<div ></div>")
	# f.write("<div class=\"mainMid\" >")

	f.write(link)
	pubdate=root.find('pubdate').text
	title=root.find('headline').findall('title')[lag].text
	fly_title=root.find('headline').findall('fly_title')[lag].text
	rubric=root.find('body').findall('rubric')[lag].text

	head="<p class=\"pubdate\" >"+ pubdate +"</p>"
	f.write(head)


	head="<p class=\"fly_title\"  >"+ fly_title +"</p>"

	f.write(head)

	head="<p class=\"title\" >"+ title +"</p>"

	f.write(head)

	head="<p class=\"rubric\"  >"+ rubric +"</p>"

	f.write(head)



	for child in  root.find('body').find('content'):
		##print(child.text, child.attrib)
		# print (child.text)
		img=child.findall('url')
		pag=child.findall('copy')
		if img!=None :
			if  len(img)==3:
				# print (img[lag].text)
				if img[lag].text!=None:
					text="<img src=\""+ img[lag].text+"\" ></img>"
					f.write(text)
		if pag!=None :
			if len(pag)==3:
				# print (pag)
				if pag[lag].text!=None:
					# print(ET.tostring(child, encoding='unicode'))
					# pag[lag].text
					# encode(encoding='UTF-8',errors='strict')
					# print("===="+pag[lag].text)
					text=u"<p class=\"mainpage\">" + pag[lag].text+u"</p>"
					f.write(text)

	line="<p class=\"line\"  ></p>"
	f.write(line)

	# f.write("</div>")
	# f.write("<div class=\"mainLeft\" ></div>")
	# f.write("<div ></div>")

def writePageHead(lag,f,root,floder,mainName):

	f.write("<head><meta charset=\"UTF-8\"></head>")



	# f.write("<div class=\"mainLeft\" ></div>")
	# f.write("<div ></div>")
	# f.write("<div class=\"mainMid\" >")

	f.write("<div class=\"titlePro\">")


	f.write("<div class=\"titleL\">")
	
	if root.find('body').find('content').find('image')!=None:
		img=root.find('body').find('content').find('image').findall('url')
		text="<img  class=\"imgIndex\"  src=\""+ floder+img[lag].text+"\" ></img>"
		f.write(text.replace('\\',"/"))
	f.write("</div>")

		


	f.write("<div class=\"titleR\">")
	pubdate=root.find('pubdate').text
	title=root.find('headline').findall('title')[lag].text
	fly_title=root.find('headline').findall('fly_title')[lag].text
	rubric=root.find('body').findall('rubric')[lag].text

	head="<p class=\"pubdateIndex\" >"+ pubdate +"</p>"
	f.write(head)


	head="<p class=\"fly_titleIndex\"  >"+ fly_title +"</p>"

	f.write(head)

	head="<p class=\"titleIndex\" ><a href=\""+floder+"article.html\" class=\"titleIndex\" >"+ title +"</a></p>"

	f.write(head.replace('\\',"/"))

	head="<p class=\"rubricIndex\"  >"+ rubric +"</p>"

	f.write(head)

	f.write("</div>")


	f.write("</div>")

	

	line="<p class=\"lineIndex\"  ></p>"


	f.write(line)


	nameDic[mainName]=pubdate

	# f.write("</div>")
	# f.write("<div class=\"mainLeft\" ></div>")
	# f.write("<div ></div>")

def createPage(p,filePath,findex,mainName):
	with open(p, 'r',encoding='utf-8') as xml_file:
		tree = ET.parse(xml_file)

		# tree = ET.parse(p)
		roott = tree.getroot()

		ff=open(p.replace("xml","html"),'w',encoding='utf-8');
		writePage(1,ff,roott)
		writePage(0,ff,roott)
		writePage(2,ff,roott)
		# floder="articles/"+os.path.split(p)[0].replace(filePath,"")+"/"
		floder=os.path.split(p)[0]+"/"
		print(floder)
		# writePageHead(1,findex,roott,floder,mainName)
		ff.close()


def createPageLag(p,filePath,findex,mainName,lag):
	with open(p, 'r',encoding='utf-8') as xml_file:
		tree = ET.parse(xml_file)

		# tree = ET.parse(p)
		roott = tree.getroot()

		# floder="articles/"+os.path.split(p)[0].replace(filePath,"")+"/"
		floder=os.path.split(p)[0]+"/"
		print(floder)
		writePageHead(lag,findex,roott,floder,mainName)


def convent(filePath,main_index):
	findex=open(""+filePath+"_index.html",'w',encoding='utf-8');
	link= "<link href=\"style.css\" rel=\"stylesheet\">"
	findex.write(link)


	# filePath="/Users/fengx/Desktop/New folder/articles/"
	# filePath="E:/fengx/EconomicsPages/articles/"
	for (root, dirs, files) in os.walk(filePath):
		for f in files:
			(shotname, extension) = os.path.splitext(f)
			old_path = os.path.join(root, f)
			if  "article.xml" in f and "._article.xml" not in f and "images" not in root: 
				print (old_path)
				createPage(old_path,filePath,findex,filePath+"_index.html")

	for (root, dirs, files) in os.walk(filePath):
		for f in files:
			(shotname, extension) = os.path.splitext(f)
			old_path = os.path.join(root, f)
			if  "article.xml" in f and "._article.xml" not in f and "images" not in root: 
				print (old_path)
				createPageLag(old_path,filePath,findex,filePath+"_index.html",1)
	findex.write("<p class=\"line\"  ></p>")

	for (root, dirs, files) in os.walk(filePath):
		for f in files:
			(shotname, extension) = os.path.splitext(f)
			old_path = os.path.join(root, f)
			if  "article.xml" in f and "._article.xml" not in f and "images" not in root: 
				print (old_path)
				createPageLag(old_path,filePath,findex,filePath+"_index.html",0)
	findex.write("<p class=\"line\"  ></p>")
	for (root, dirs, files) in os.walk(filePath):
		for f in files:
			(shotname, extension) = os.path.splitext(f)
			old_path = os.path.join(root, f)
			if  "article.xml" in f and "._article.xml" not in f and "images" not in root: 
				print (old_path)
				createPageLag(old_path,filePath,findex,filePath+"_index.html",2)
	findex.close()



def BatchConvent():
	main_index=open("main_#index.html",'w',encoding='utf-8');
	main_index.write("<link href=\"style.css\" rel=\"stylesheet\">")
	main_index.write("<head><meta charset=\"UTF-8\"></head>")



	for s in os.listdir("."):
		if len(s)>20 and os.path.isdir(s):
			convent(s,main_index)

	print(nameDic.keys())
	for s in os.listdir("."):
		if "_index.html" in s and os.path.isfile(s) and "#" not in s:
			print(s)
			newName="x"
			sp=nameDic[s].split("-")
			datename=sp[0]+"-"+sp[1]
			try:
				os.remove(datename+"#"+s)
			except Exception as e:
				print("xx")
			else:
				print("xx")
			finally:
				print("xx")
			os.rename(s,datename+"#"+s)

			#main index
			main_index.write("<a href=\""+datename+"%23"+s+"\">")
			text="<img  class=\"imgIndex\"  src=\""+ s.replace('_index.html','')+"/cover.jpg\" ></img>"
			main_index.write(text.replace('\\',"/"))
			main_index.write("<p class=\"fly_titleIndex\"  >"+ datename +"</p>")
			main_index.write("</a>")


	main_index.close()	
						
BatchConvent()


