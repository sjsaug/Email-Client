import requests
import configparser

def read_config():
	config = configparser.RawConfigParser()
	config.read("./mailgun.cfg")
	required_vars = dict(config.items("Required"))
	return {"API_KEY": required_vars["api_key"], "DOMAIN_NAME": required_vars["domain_name"]}
	

def send_simple_message():
	return requests.post(
	    "https://api.mailgun.net/v3/" + read_config()["DOMAIN_NAME"] + "/messages",
		auth=("api", read_config()["API_KEY"]),
		data={"from": "sjsaugTest <mailgun@" + read_config()["DOMAIN_NAME"] + ">",
			"to": ["sjsaug@gmail.com"],
			"subject": "Hello",
			"text": "Test!"})

def main():
	send_simple_message()
	
main()