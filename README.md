# SMTPSpoofDetector
This is a script that will examine SMTP headers using Google's Gmail API and determine if an email was sent with spoofed SMTP fields. Currently it runs as a python script, but the end goal is to have this code run automatically in a Chrome extension. 

# Current State
Python script returns a dump of a hardcoded message's raw MIME data. 

# Current Goals
* Setup a testing gmail account so we can use that instead of Sruthi's
* Isolate the SMTP headers from the MIME data that is being returned
* Dynamically select most recent message ID

# Future Goals
* Look into packaging code as a Chrome extension. Can it stay python, or will we need to refactor into javascript?
* Figure out how to trigger code. On email receipt? On email opening/viewing? Click a button to trigger?
* Determine best method to store/compare SMTP fields. Compare return path to smtp.mailfrom value? Create dictionary of contacts and smtp.mail pairs and compare recieved values to cached ones?


