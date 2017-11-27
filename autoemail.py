import subprocess

subprocess.call("sqlite3 database.db \"SELECT * FROM email\" > result.txt",shell=True)

f = open("result.txt","r")
emails = f.readlines()
print emails
for email in emails:
	com = "echo \"This is a test.\" | mail -s \"test message\" "+email
	subprocess.call(com,shell=True)