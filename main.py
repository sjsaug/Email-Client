import requests
import configparser

def read_config():
	config = configparser.RawConfigParser()
	config.read("./mailgun.cfg")
	required_vars = dict(config.items("Required"))
	email_parameters = dict(config.items("Parameters"))
	return { #honestly, could just initialize this at the start and not have to run the function each time i want to return a value, but that's for later
		"API_KEY": required_vars["api_key"], 
		"DOMAIN_NAME": required_vars["domain_name"], 
		"SENDER": email_parameters["sender"], 
		"DOMAIN_PREFIX": email_parameters["domain_prefix"], 
		"RECIPIENT": email_parameters["recipient"], 
		"SUBJECT": email_parameters["subject"], 
		"TEXT": email_parameters["text"], 
		"ATTACHMENT": email_parameters["attachment"]
		}

def send_simple_message():
	return requests.post(
	    "https://api.mailgun.net/v3/" + read_config()["DOMAIN_NAME"] + "/messages",
		auth=("api", read_config()["API_KEY"]),
		data={"from": read_config()["SENDER"] + "<" + read_config()["DOMAIN_PREFIX"] + "@" + read_config()["DOMAIN_NAME"] + ">",
			"to": read_config()["RECIPIENT"],
			"subject": read_config()["SUBJECT"],
			"text": read_config()["TEXT"]})

def send_attachment_message():
	return requests.post(
	    "https://api.mailgun.net/v3/" + read_config()["DOMAIN_NAME"] + "/messages",
		auth=("api", read_config()["API_KEY"]),
		files = [("attachment", (read_config()["ATTACHMENT"], open(read_config()["ATTACHMENT"], "rb").read()))],
		data={"from": read_config()["SENDER"] + "<" + read_config()["DOMAIN_PREFIX"] + "@" + read_config()["DOMAIN_NAME"] + ">",
			"to": read_config()["RECIPIENT"],
			"subject": read_config()["SUBJECT"],
			"text": read_config()["TEXT"]})

def main():
	if read_config()["ATTACHMENT"] != "NONE":
		send_attachment_message()
	else:
		send_simple_message()
	
main()