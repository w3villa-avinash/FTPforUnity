To run local FTP server 
```
pip install python_ftp_server
python3 -m python_ftp_server -d "/path/to/your/dir"
```

once the Server is running you will get data in this format


OutPut if the Server is running successfully 
```
Local address: ftp://192.168.0.100:60000
User: user
Password: ***********************


INFO:pyftpdlib:concurrency model: async
INFO:pyftpdlib:masquerade (NAT) address: None
INFO:pyftpdlib:passive ports: 60001->60100
INFO:pyftpdlib:>>> starting FTP server on 192.168.0.100:60000, pid=1383
```


then you can run the wachter.py 

make sure to install aspose-3d lib for python
pip install aspose-python 
