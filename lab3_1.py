from​ google.cloud ​ import​ storage
client = storage.Client()
bucket = client.get_bucket(​ 'mm16b009'​ )
blob = bucket.get_blob(​ 'addresses.csv'​ )
x = blob.download_as_string()
x = x.decode(​ 'utf-8'​ )
t = x.split('\n')
t = x.remove('')
count = 0
for line in t:
	count+=1
print('number of lines :', count)
# count the lines in x
