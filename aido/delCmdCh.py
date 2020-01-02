
import re

def deal_control_char(s):
	temp=re.sub('[\x00-\x09|\x0b-\x0c|\x0e-\x1f]','',s)
	return temp
