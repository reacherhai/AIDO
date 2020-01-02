
import re

def deal_control_char(s):
	s = re.sub(r"\x1b\[33m","",s)
	s = re.sub(r"\x1b\[0m","",s)
	s = re.sub(r"\x1b\[36m","",s)
	s = re.sub(r'[\x00-\x09|\x0b-\x0c|\x0e-\x1f]','',s)
	return s
