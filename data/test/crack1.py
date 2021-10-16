#!/usr/bin/python3
# -*- coding: utf-8 -*-

import xml.etree.ElementTree as ET
import os
lang=1;



nameDic={}


BUTS='''
	 <button onclick="ShowLag01()">EN_CN</button>
	 <button onclick="ShowLag0()">EN</button>
	 <button onclick="ShowLag1()">CNS</button>
	 <button onclick="ShowLag2()">CNT</button>
	<script>
	function ShowLag0(){
		$('.laguage0').show();
		$('.laguage1').hide();
		$('.laguage2').hide();
	}
		function ShowLag1(){
		$('.laguage1').show();
		$('.laguage0').hide();
		$('.laguage2').hide();
	}
		function ShowLag2(){
		$('.laguage2').show();
		$('.laguage1').hide();
		$('.laguage0').hide();
	}
	function ShowLag01(){
		$('.laguage2').hide();
		$('.laguage1').show();
		$('.laguage0').show();
	}
	</script>'''


def writePage(lag,f,root):

	f.write("<head><meta charset=\"UTF-8\"></head>")


	link= "<link href=\"style.css\" rel=\"stylesheet\">"
	link= "<link href=\"../../style.css\" rel=\"stylesheet\">"

	link+="""<head>
		<script src="../../jquery-3.6.0.min.js"></script>
		</head>"""

	link+=BUTS

	# f.write("<div class=\"mainLeft\" ></div>")
	# f.write("<div ></div>")
	# f.write("<div class=\"mainMid\" >")

	f.write(link)
	
	pubdate=root.find('pubdate').text
	title0=root.find('headline').findall('title')[0].text
	title1=root.find('headline').findall('title')[1].text
	title2=root.find('headline').findall('title')[2].text
	fly_title0=root.find('headline').findall('fly_title')[0].text
	fly_title1=root.find('headline').findall('fly_title')[1].text
	fly_title2=root.find('headline').findall('fly_title')[2].text
	rubric0=root.find('body').findall('rubric')[0].text
	rubric1=root.find('body').findall('rubric')[1].text
	rubric2=root.find('body').findall('rubric')[2].text



	f.write("<p class=\"pubdate\" >"+ pubdate +"</p>")
	f.write("<p class=\"fly_title laguage0\"  >"+ fly_title0 +"</p>")
	f.write("<p class=\"fly_title laguage1\"  >"+ fly_title1 +"</p>")
	f.write("<p class=\"fly_title laguage2\"  >"+ fly_title2 +"</p>")
	f.write("<p class=\"title laguage0\" >"+ title0 +"</p>")
	f.write("<p class=\"title laguage1\" >"+ title1 +"</p>")
	f.write("<p class=\"title laguage2\" >"+ title2 +"</p>")
	f.write("<p class=\"rubric laguage0\"  >"+ rubric0 +"</p>")
	f.write("<p class=\"rubric laguage1\"  >"+ rubric1 +"</p>")
	f.write("<p class=\"rubric laguage2\"  >"+ rubric2 +"</p>")



	for child in  root.find('body').find('content'):
		##print(child.text, child.attrib)
		# print (child.text)
		img=child.findall('url')
		pag=child.findall('copy')
		if img!=None :
			if  len(img)==3:
				# print (img[lag].text)
				if img[lag].text!=None:
					text="<img class=\"laguage0\" src=\""+ img[0].text+"\" ></img>"
					f.write(text)
					text="<img class=\"laguage0\"  src=\""+ img[1].text+"\" ></img>"
					f.write(text)
					text="<img class=\"laguage0\"  src=\""+ img[2].text+"\" ></img>"
					f.write(text)
		if pag!=None :
			if len(pag)==3:
				# print (pag)
				if pag[lag].text!=None:
					# pag[lag].text
					# encode(encoding='UTF-8',errors='strict')
					pag0=ET.tostring(pag[0], encoding='unicode').replace("</copy>","").replace("<copy lang=\"en_GB\">","").replace("<copy lang=\"zh_CN\">","").replace("<copy lang=\"zh_TW\">","")
					pag1=ET.tostring(pag[1], encoding='unicode').replace("</copy>","").replace("<copy lang=\"en_GB\">","").replace("<copy lang=\"zh_CN\">","").replace("<copy lang=\"zh_TW\">","")
					pag2=ET.tostring(pag[2], encoding='unicode').replace("</copy>","").replace("<copy lang=\"en_GB\">","").replace("<copy lang=\"zh_CN\">","").replace("<copy lang=\"zh_TW\">","")
					f.write(u"<p class=\"mainpage laguage0\">" + pag0+u"</p>")
					f.write(u"<p class=\"mainpage laguage1\">" + pag1+u"</p>")
					f.write(u"<p class=\"mainpage laguage2\">" + pag2+u"</p>")

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
	title0=root.find('headline').findall('title')[0].text
	title1=root.find('headline').findall('title')[1].text
	title2=root.find('headline').findall('title')[2].text
	fly_title0=root.find('headline').findall('fly_title')[0].text
	fly_title1=root.find('headline').findall('fly_title')[1].text
	fly_title2=root.find('headline').findall('fly_title')[2].text
	rubric0=root.find('body').findall('rubric')[0].text
	rubric1=root.find('body').findall('rubric')[1].text
	rubric2=root.find('body').findall('rubric')[1].text

	
	f.write("<p class=\"pubdateIndex \" >"+ pubdate +"</p>")
	f.write("<p class=\"fly_titleIndex laguage0\"  >"+ fly_title0 +"</p>")
	f.write("<p class=\"fly_titleIndex laguage1\"  >"+ fly_title1 +"</p>")
	f.write("<p class=\"fly_titleIndex laguage2\"  >"+ fly_title2 +"</p>")
	f.write(("<p class=\"titleIndex laguage0\" ><a href=\""+floder+"article.html\" class=\"titleIndex\" >"+ title0 +"</a></p>").replace('\\',"/"))
	f.write(("<p class=\"titleIndex laguage1\" ><a href=\""+floder+"article.html\" class=\"titleIndex\" >"+ title1 +"</a></p>").replace('\\',"/"))
	f.write(("<p class=\"titleIndex laguage2\" ><a href=\""+floder+"article.html\" class=\"titleIndex\" >"+ title2 +"</a></p>").replace('\\',"/"))
	f.write("<p class=\"rubricIndex laguage0\"  >"+ rubric0 +"</p>")
	f.write("<p class=\"rubricIndex laguage1\"  >"+ rubric1 +"</p>")
	f.write("<p class=\"rubricIndex laguage2\"  >"+ rubric2 +"</p>")

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

	link+="""<head>
		<script src="jquery-3.6.0.min.js"></script>
		</head>"""
	link+=BUTS
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
	# findex.write("<p class=\"line\"  ></p>")

	# for (root, dirs, files) in os.walk(filePath):
	# 	for f in files:
	# 		(shotname, extension) = os.path.splitext(f)
	# 		old_path = os.path.join(root, f)
	# 		if  "article.xml" in f and "._article.xml" not in f and "images" not in root: 
	# 			print (old_path)
	# 			createPageLag(old_path,filePath,findex,filePath+"_index.html",0)
	# findex.write("<p class=\"line\"  ></p>")
	# for (root, dirs, files) in os.walk(filePath):
	# 	for f in files:
	# 		(shotname, extension) = os.path.splitext(f)
	# 		old_path = os.path.join(root, f)
	# 		if  "article.xml" in f and "._article.xml" not in f and "images" not in root: 
	# 			print (old_path)
	# 			createPageLag(old_path,filePath,findex,filePath+"_index.html",2)
	findex.close()



def BatchConvent():
	main_index=open("main_#index.html",'w',encoding='utf-8');
	main_index.write("<link href=\"style.css\" rel=\"stylesheet\">")
	main_index.write("<head><meta charset=\"UTF-8\"></head>")

	link="""<head>
		<script src="jquery-3.6.0.min.js"></script>
		</head>"""

	link+=BUTS
	main_index.write(link)

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


