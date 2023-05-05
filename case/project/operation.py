# -*- coding:utf-8 -*-



def create_project(username: str, password: str):
	"""
	@api {post} /create_project 第一个造数模块
	@apiGroup 项目
	@apiName create_project
	@apiDescription  第一个造数模块
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

# if __name__ == "__main__":
# 	create_project(username = "long", password = "123")