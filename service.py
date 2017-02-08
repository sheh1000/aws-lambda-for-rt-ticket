# -*- coding: utf-8 -*-
from __future__ import print_function

import sys
import os
import json
import base64
import ast
import rtapi

print('Loading function')


def returnCode(code, message):
	return {
		"statusCode": code,
		"headers": {"Content-Type": "application/json"},
		"body": {
			"message": message
		}
	}

def handler(event, context):
	print(event)
	print(event['body'])
	
	body = ast.literal_eval(event['body'])
	headers = event['headers']
	message = ""

	''' ============================================'''
	''' Checking the content before ticket creation '''
	try:
		RT_API_USERNAME = os.environ['RT_API_USERNAME']
		RT_API_PASSWORD = os.environ['RT_API_PASSWORD']
		RT_API_URL = os.environ['RT_API_URL']
	except KeyError:
		raise KeyError('RT_API_USERNAME, RT_API_PASSWORD, RT_API_URL environment variales must be defined')
		returnCode(200, "Required environment variable is missing. Please specify it in AWS Lambda settings")
		sys.exit("-1")

	try:
		subject = body['condition_name']
	except KeyError:
		raise KeyError("Unexpected payload. No such attribute in json object")
		returnCode(200, "Unexpected payload. No such attribute in json object")
		sys.exit("-1")

	try:
		support_code = headers['support_code']
		queue = headers['queue']
		requestors = headers['requestors'].split(" ")
	except KeyError:
		raise KeyError('Please define support_code, queue, requestors in New Relic webhook settings')
		returnCode(200, "Please define support_code, queue, requestors in New Relic webhook settings")
		sys.exit("-1")
	''' -------------------------------------------'''

	# save targets value to exclude it from message
	targets = body.get('targets', None)
	if 'targets' in body:
		del body['targets']

	for key, value in body.iteritems():
		message += "{}: {}\n".format(key,value)

	cc = headers.get('cc', ' ').split(" ")
	product = headers.get('product', "Operations Automation")
	severity = headers.get('severity', 3)

	# Creating ticket in RT via API
	rt = rtapi.RequestTrackerApi(RT_API_URL)
	rt.login(RT_API_USERNAME, RT_API_PASSWORD)

	result = rt.createTicket(support_code, requestors, severity, subject, product, message, cc, queue)
	returnCode(200, result)
	sys.exit(1)

