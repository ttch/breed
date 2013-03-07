# *.* coding=utf-8 *.*

def hello():
	print "hello"

def poptoaddbyleft(stat , dstat ):
	if len(stat) == 0 :
		return None
	else:
		token = stat.popleft()
		dstat.appendleft(token)
	 	return token


