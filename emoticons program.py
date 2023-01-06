print("Digit happy or sad faces and it will say if have more happy or sad emoticons.\nIf have the same quantities or none of both, the text is neutral.(happy: :-); sad: :-( )")
M = str(input())
if M.count(":-)") > M.count(":-("):
    print("happy")
elif M.count(":-)") == M.count(":-("):
    print("neutral")
else:
    print("sad")