import requests
import configparser

def read_config():
	configParser = configparser.RawConfigParser()
	configFilePath = r'./mailgun.cfg'
	configParser.read(configFilePath)
	required_vars = dict(configParser.items("Required"))
	return {"API_KEY": required_vars["API_KEY"], "DOMAIN_NAME": required_vars["DOMAIN_NAME"]}
	

def send_simple_message():
	return requests.post(
	    "https://api.mailgun.net/v3/" + read_config()["DOMAIN_NAME"] + "/messages",
		auth=("api", read_config()["API_KEY"]),
		data={"from": "sjsaugTest <mailgun@" + read_config()["DOMAIN_NAME"] + ">",
			"to": ["sjsaug@gmail.com"],
			"subject": "Hello",
			"text": "Test!"})

def main():
	print(str(read_config()["DOMAIN_NAME"]))
	
main()