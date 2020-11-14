def count_lines(data, context):
	from​ google.cloud ​ import​ storage
	client = storage.Client()
	bucket = client.get_bucket(​ 'mm16b009'​ )
	blob = bucket.get_blob(​ 'addresses.csv'​ )
	x = blob.download_as_string()
	x = x.decode(​ 'utf-8'​ )
	t = x.split('\n')
	t = x.remove('')
	length = len(t)
	print('number of lines: ' +str(length))
# count the lines in x
