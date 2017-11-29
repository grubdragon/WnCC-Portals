import subprocess

subprocess.call("sqlite3 database.db \"SELECT * FROM email\" > result.txt",shell=True)

f = open("result.txt","r")
emails = f.readlines()
for email in emails:
	subprocess.call(['bash','mailer.sh',email])