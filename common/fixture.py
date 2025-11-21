from typing import Any

import requests
from jsonpath import jsonpath
from faker import Faker
from common.handle_conf import conf


class RequestHandler:
	@staticmethod
	def send_request(method, url, data=None, headers=None, verify=False):
		method = method.lower()
		headers = headers or {}

		if method == 'get':
			return requests.request(
				method=method,
				url=url,
				params=data,  # GET使用params
				headers=headers,
				verify=verify
			)
		else:
			return requests.request(
				method=method,
				url=url,
				json=data,  # 其他方法使用json
				headers=headers,
				verify=verify
			)



