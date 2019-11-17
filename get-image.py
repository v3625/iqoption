#!/usr/bin/env python3

from minio import Minio
minioClient = Minio('localhost:8001', access_key='user1', secret_key='testtest', secure=False)

try:
	data = minioClient.get_partial_object('test', 'testimage.jpg', 1000)
	with open('testimage-fixed.jpg', 'wb') as file_data:
		for d in data:
			file_data.write(d)
except ResponseError as err:
	print(err)
