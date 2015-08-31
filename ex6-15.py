str = 'X-DSPAM-Confidence: 0.8475'
start = str.find(":")
number = float(str[start+1:].strip())
print(number)