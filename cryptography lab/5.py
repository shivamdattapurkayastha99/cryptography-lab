# algo of reverse cipher
message="my name is shivam"
translated=""
l=len(message)
i=l-1
while i>=0:
    translated+=message[i]
    i-=1
print(translated)
