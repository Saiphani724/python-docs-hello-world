from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
	returnText = "Welcome, you are using KeepHerSafe Services... :)\n" + \
		"Sample Request Url: " + \
	"\"http://keephersafe.azurewebsites.net/isEmergency/currentheartrate=92.32&heartratemean=85&heartratestdDev=20&scaleOfElimination=1\"" + \
	"\n\n" 
	return returnText


#sample request
#http://127.0.0.1:5000/isEmergency/currentheartrate=92.32&heartratemean=85&heartratestdDev=20&scaleOfElimination=1
@app.route("/isEmergency/currentheartrate=<hrv>&heartratemean=<mean>&heartratestdDev=<stdDev>&scaleOfElimination=<scaleOfElimination>")
def checkCondition(hrv,mean, stdDev, scaleOfElimination):
	hrv = float(hrv)
	mean = float(mean)
	stdDev = float(stdDev)
	scaleOfElimination = float(scaleOfElimination)

	if not 60 < hrv < 110:
		return { "status" : 200 , "isInputInRange" : False}

	isLessThanLowerBound = hrv < (mean - stdDev* scaleOfElimination);
	isGreaterThanUpperBound = hrv > (mean + stdDev * scaleOfElimination);
	isOutOfBounds = isLessThanLowerBound or isGreaterThanUpperBound;
	return { "status" : 200 , "isInputInRange" : True, "isEmergency" : isOutOfBounds}


