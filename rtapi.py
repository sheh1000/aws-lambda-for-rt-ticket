import requests
requests.packages.urllib3.disable_warnings()

class RequestTrackerApi:
	def __init__(self, baseUrl):
		self.baseUrl=baseUrl
		self.session=requests.Session()

	def login(self, login, passwd):
		login = {
			'method': 'Login',
			'params': {
				'name': login,
				'password': passwd
			}
		}
		r = self.session.post('%sUser' % self.baseUrl, json=login, verify=False).json()
		if r['error'] is None:
			return r['result']
		else:
			return r['error']

	def correspond(self, ticketID, text, creator):
		request = {
			'method': 'Correspond',
			'params': {
				'id': ticketID,
				'Text': text,
				'Creator': creator
			}
		}
		r = self.session.post('%sTicket' % self.baseUrl, json=request, verify=False).json()
		if r['error'] is None:
			return r['result']
		else:
			return r['error']

	def createTicket(self, supportCode, requestor, severity, subject, product, RTmessage, cc, queue):
		creator = {
				'FirstName': 'Odin',
				'LastName': 'Monitoring',
				'PhoneNumber': '70000000000',
				'Email': 'noreply@odin.com'}
		request = {
			'method': 'Create',
			'params': {
				'Queue': queue,
				'Severity': severity,  # 1 - is urgent, 2 - high, 3 - normal
				'Subject': subject,
				'Product': product,
				'Creator': creator,
				'Requestor': requestor,
				'Cc': cc,
				'SupportCode': supportCode
			}
		}
		r = self.session.post('%sTicket' % self.baseUrl, json=request, verify=False).json()
		if r['error'] is None:
			self.setCustomFieldValue(r['result'], 'Zabbix', ['checked'])
			self.correspond(r['result'], RTmessage, creator)
			return r['result']
		else:
			return r['error']

	def setCustomFieldValue(self, ticketID, CustomField, arrayValues):
		request = {
			'method': 'SetCustomFieldValuesAsArray',
			'params': {
				'id': ticketID,
				'CustomFieldName': CustomField,
				'Values': arrayValues
			}
		}
		r = self.session.post('%sTicket' % self.baseUrl, json=request, verify=False).json()
		if r['error'] is None:
			return r['result']
		else:
			return r['error']

	def attach(self, ticketID, filename, description, content_type, filedata):
		request = {
			'method': 'addBase64EncodedAttachment',
			'params': {
				'id': ticketID,
				'fileName': filename,
				'description': description,
				'content-type': content_type,
				'base64EncodedAttachmentData': filedata
			}
		}
		r = self.session.post('%sTicket' % self.baseUrl, json=request, verify=False).json()
		if r['error'] is None:
			return r['result']
		else:
			return r['error']