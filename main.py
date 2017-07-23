#coding=utf-8
#这里需要额外导入 request 方法
from pymongo import MongoClient
from bson.code import Code
from bson import ObjectId
db = MongoClient()['data']
lines = [{"is_label":0,"txt":"我是中国人"},
	{"is_label":0,"txt":"我爱我的祖国"},
	{"is_label":0,"txt":"松花江上"},
	{"is_label":0,"txt":"一九八四年,中国"},
	{"is_label":0,"txt":"长江"},
	{"is_label":0,"txt":"黄河水,中国"}]
db.orgin.remove()
[db.orgin.insert(line) for line in lines]
labeled = db.data_labeled
labeled.remove()
from bottle import route, run ,request
from bottle import template


@route('/label')
def login():
	data = db.orgin.find_one({'is_label': 0})
	return template('labeldata',docum=data["txt"],id_text = data[u'_id'])     #login是模板名，这里不需要填写后缀.tpl
@route('/label',method='POST')
def do_login():
        '''
        函数名字随意定，这里是进行POST动作的，所以用了do_login，函数名不能与前后函数有同名
        登陆动作，这里用了post，也就是当访问login页面，同时带了POST请求时，这个函数将响应
        '''
	id_data = request.forms.get('id_data')
	True_s = request.forms.get('input_sentence')
        False_s = request.forms.get('output_sentence')
	if (len(True_s)==len(False_s)) and (True_s!=False_s):
		labeled.insert({"input_sentence":True_s,"output_sentence":False_s})
	db.orgin.update({u'_id': ObjectId(id_data)},{'$set':{u'is_label':1}}, upsert=False, multi=False)
	data = db.orgin.find_one({u'is_label': 0})
	if data==None:
		return '<p>Congratulation! all data has been labelled.</p>'
	print(data["txt"])
	return template('labeldata',docum=data["txt"],id_text = data[u'_id'])
run(host='0.0.0.0', port=8080, debug=True)   #开启服务
