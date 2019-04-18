# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.decorators import csrf
import thulac
 
import sys
sys.path.append("..")
from toolkit.pre_load import neo_con
# from toolkit.pre_load import wv_model, tree ,predict_labels
# from toolkit.NER import get_explain,get_detail_explain

# 接收GET请求数据
def showdetail(request):
	ctx = {}
	if 'title' in request.GET:
		# 连接数据库
		db = neo_con
		
		title = request.GET['title']
		answer = db.matchFilmbyTitle(title)
		if answer == None:
			return render(request, "404.html", ctx) 

		if len(answer) > 0:
			answer = answer[0]['n']
		else:
			ctx['title'] = '实体条目出现未知错误'
			return
		
		ctx['title'] = answer['title']
		ctx['image'] = '<img src=/static/img/pic/' + answer['title'] + '.jpg alt="该条目无图片" height="100%" width="100%" >'
		ctx['baseInfoKeyList'] = []                     #条目名
		ctx['baseInfoKeyList'].append('类型')
		ctx['baseInfoKeyList'].append('评分')
		ctx['baseInfoKeyList'].append('发行时间')
		ctx['baseInfoKeyList'].append('评分人数')
		ctx['baseInfoKeyList'].append('主演')

		ctx['baseInfoValueList'] = []                   #条目内容
		
		type_of_film = db.findOtherEntities(answer['title'],"type of film")
		casts_of_film = db.findOtherEntities(answer['title'],"casts of film")
		p1 = ""
		p5 = ""
		for dic in type_of_film:
			p1 += str(dic['n2']['title'])
			p1 += " "
		p2 = answer['score']
		p3 = answer['release_year']
		p4 = answer['vote_count']
		for dic in casts_of_film:
			p5 += str(dic['n2']['title'])
			p5 += " "
		
		ctx['baseInfoValueList'].append(p1)
		ctx['baseInfoValueList'].append(p2)
		ctx['baseInfoValueList'].append(p3)
		ctx['baseInfoValueList'].append(p4)
		ctx['baseInfoValueList'].append(p5)

		text = '<table class="table table-striped table-advance table-hover"> <tbody>'
		keyList = ctx['baseInfoKeyList']
		valueList = ctx['baseInfoValueList']

		i = 0
		while i < len(keyList) :
			value = " "
			if i < len(valueList):
				value = valueList[i]
			text += "<tr>"
			text += '<td><strong>' + keyList[i] + '</strong></td>'
			text += '<td>' + value + '</td>'
			i += 1
			
			if i < len(valueList):
				value = valueList[i]
			if i < len(keyList) :
				text += '<td><strong>' + keyList[i] + '</strong></td>'
				text += '<td>' + value + '</td>'
			else :
				text += '<td><strong>' + '</strong></td>'
				text += '<td>' + '</td>'
			i += 1
			text += "</tr>"
		text += " </tbody> </table>"
		ctx['baseInfoTable'] = text 
		
# 		tagcloud = ""
# 		taglist = wv_model.get_simi_top(answer['title'], 10)
# 		for tag in taglist:
# 			tagcloud += '<a href= "./detail.html?title=' + str(tag) + '"> '
# 			tagcloud += str(tag) + "</a>"
# #			print(tag)
# 		ctx['tagcloud'] = tagcloud
		
		# movie_type = ""
		# ansList = tree.get_path(answer['title'], True)
		# for List in ansList:
		# 	agri_type += '<p >'
		# 	flag = 1
		# 	for p in List:
		# 		if flag == 1:
		# 			flag = 0
		# 		else:
		# 			agri_type += ' / '
		# 		agri_type += str(p)
				
		# 	agri_type += '</p>'	
		# if len(ansList) == 0:
		# 	agri_type = '<p > 暂无电影类型</p>'
		# ctx['agri_type'] = agri_type	
		
		# entity_type = ""
		# explain = get_explain(predict_labels[answer['title']])
		# detail_explain = get_detail_explain(predict_labels[answer['title']])
		# entity_type += '<p > [' + explain + "]: "
		# entity_type += detail_explain + "</p>"
		# ctx['entity_type'] = entity_type	
			
	else:
		return render(request, "404.html", ctx) 		
			
	return render(request, "detail.html", ctx)
	
#	
## -*- coding: utf-8 -*-
#from django.http import HttpResponse
#from django.shortcuts import render_to_response
#import thulac
# 
#import sys
#sys.path.append("..")
#from neo4jModel.models import Neo4j
#
#def search_detail(request):
#	return render_to_response('detail.html')
#
## 接收GET请求数据
#def showdetail(request):
#	request.encoding = 'utf-8'
#	if 'title' in request.GET:
#		# 连接数据库
#		db = Neo4j()
#		db.connectDB()
#		title = request.GET['title']
#		answer = db.matchItembyTitle(title)
#		message = answer['detail']
#				
#	return HttpResponse(message)