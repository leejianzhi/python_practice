text = "X-DSPAM-Confidence:    0.8475";
whiteSpace = text.find(' ')
endNum = text.find('5', whiteSpace)
withSpace = text[whiteSpace + 1 : endNum + 1]
removeSpace = withSpace.strip()
floatStr = float(removeSpace)
print(floatStr)
