data=open('file.txt')
text=data.read()
text=text.replace(',',' ').replace('!',' ').replace('?',' ').replace('.',' ')
tweets=list(text.split())
stri=str()
for i in tweets:
	stri+=str(i)
	stri+=" "
print(f"Number of words={len(tweets)}")
st=stri.lower()
tweet=st.split()
uniq=set(tweet)
print(f"Number of unique elements={len(uniq)}")
uni=list(uniq)
uni.sort()
for word in uni:
	print(f'{word} :=>{tweet.count(word)} times \t Percentage: {tweet.count(word)/len(tweet)*100:.2f}')
