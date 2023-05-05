# -*- coding:utf-8 -*-

import pymysql

def create_project_v2(username: str, password: str):
	"""
	@api {post} /create_project_v2 第二个造数模块
	@apiGroup 项目
	@apiName create_project_v2
	@apiDescription  第二个造数模块
	@apiPermission long
	@apiParam {String} username=tester 用户名修改
	@apiParam {String} password=tester 用户密码修改
	@apiParamExample {json} 请求示例:
	{
	     "username": "tester",
	     "password": "tester"
	  }
	@apiSuccess (200) {Number} code=200 服务器码
	@apiSuccess (200) {Object} data 造数成功返回相关的数据
	@apiSuccess (200) {String} data.project_name="demo_1664550976" 项目名称
	@apiSuccess (200) {String} msg="造数成功" 提示语
	@apiSuccessExample {json} 返回示例:
	{
	    "code": 0,
	    "msg": "请求成功",
	    "data": {
	    "project_name": "demo_1664550976"
	    }
	}	
	"""
	msg = f"用户创建成功:{username}"
	return {"code": 200, "message": "测试成功", "data": {"var": msg}}


def create_db_record(host: str, username: str, password: str, db: str, sql: str):
	"""
	@api {post} /create_db_record 第三个造数模块
	@apiGroup 项目
	@apiName create_db_record
	@apiDescription  插入sql
	@apiPermission long
	@apiParam {String} host=127.0.0.1 连接IP
	@apiParam {String} username=tester 连接用户名-xiu
	@apiParam {String} password=tester 连接密码
	@apiParam {String} db=db 要连接的数据库
	@apiParam {String} sql=insert into .... 要执行的sql

	@apiParamExample {json} 请求示例:
	{
		 "host": "localhost",
	     "username": "tester",
	     "password": "tester",
	     "db": "test_db",
	     "sql": "insert into..."
	  }
	@apiSuccess (200) {Number} code=200 服务器码
	@apiSuccess (200) {Object} data 造数成功返回相关的数据
	@apiSuccess (200) {String} data.project_name="demo_1664550976" 项目名称
	@apiSuccess (200) {String} msg="造数成功" 提示语
	@apiSuccessExample {json} 返回示例:
	{
	    "code": 0,
	    "msg": "请求成功",
	    "data": {
	    "project_name": "demo_1664550976"
	    }
	}	
	"""
	# 打开数据库连接
	db = pymysql.connect(host=host,
	                     user=username,
	                     password=password,
	                     database=db	                     
	                     )
	 
	# 使用cursor()方法获取操作游标 
	cursor = db.cursor()
	 
	msg = f"SQL插入成功"

	try:
	   # 执行sql语句
	   cursor.execute(sql)
	   # 提交到数据库执行
	   db.commit()
	except:
	   msg = f"插入失败"
	   # 如果发生错误则回滚
	   db.rollback()
	 
	# 关闭数据库连接
	db.close()	
	
	return {"code": 200, "message": "测试成功", "data": {"result": msg}}

if __name__ == "__main__":
	create_db_record(
		host = "10.192.31.93",
		username = "root",
		password = "root",
		db = "xp_magic_key_test",
		sql = """INSERT INTO account(`authority`, `username`,`password`, `is_deleted`) VALUES('user', 'long2', 'longpassword2', 1);"""
		)