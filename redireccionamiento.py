import webapp
import random

class randServ(webapp.webApp):
	def process(self, parsedRequest):
		return ("301 Moved Permanently" + "\n"
						+ "Location: http://localhost:1234/"
						+ str(random.randrange(999999)), "")

if __name__ == "__main__":
	randserver = randServ("localhost", 1234)
