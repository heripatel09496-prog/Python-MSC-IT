paragraph=input("Enter paragraph:")
words=paragraph.split()
print("total words",len(words))
print("unique words",len(set(words)))
longest=words[0]
sortest=words[0]
for w in words:
    if len(w)>len(longest):
        longest=w
        for w in words:
            if len(w)<len(sortest):
                sortest=w
                print("Longest Word is:",longest)
                print("sortest Word is:",sortest)
