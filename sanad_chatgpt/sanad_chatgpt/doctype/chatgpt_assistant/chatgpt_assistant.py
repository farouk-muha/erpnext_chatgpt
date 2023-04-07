# Copyright (c) 2023, Farouk Muharram and contributors
# For license information, please see license.txt

import requests

import frappe
from frappe import _
from frappe.model.document import Document

class ChatGPTAssistant(Document):
	pass

@frappe.whitelist()
def get_chat_response(api_key, input_text):
	# Set up the API endpoint and headers
	api_endpoint = "https://api.openai.com/v1/chat/completions"
	api_headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}

	# Set up the API request data
	api_data = {
		"model":"gpt-3.5-turbo",
		"messages":[
		{"role": "system", "content": "You are a helpful assistant."},
		{"role": "user", "content": input_text}
	]
	}

	# Send the API request and get the response
	response = requests.post(api_endpoint, headers=api_headers, json=api_data)

	# Extract the chat response from the API response
	try:
		return response.json()["choices"][0]
	except:
		pass
	try:
		response = response.json()
		frappe.msgprint("Error Code: {}  Message:{}".format(response["error"]["code"], response["error"]["message"]))
	except:
		pass
