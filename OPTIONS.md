
```
        location / {
            if ($request_method = OPTIONS ) {
                add_header Content-Length 0;
                add_header Content-Type text/plain;
                return 200;
            }
            add_header Access-Control-Allow-Origin *;
            add_header Access-Control-Max-Age 3600;
            add_header Access-Control-Expose-Headers Content-Length;
            add_header Access-Control-Allow-Headers Range;
        }

```


```
$ curl -Ivs -X OPTIONS http://138.2.44.237:80
HTTP/1.1 200 OK
Date: Thu, 14 Jul 2022 07:24:11 GMT
Content-Type: text/plain
Content-Length: 0
Connection: keep-alive

*   Trying 138.2.44.237:80...
* Connected to 138.2.44.237 (138.2.44.237) port 80 (#0)
> OPTIONS / HTTP/1.1
> Host: 138.2.44.237
> User-Agent: curl/7.78.0
> Accept: */*
>
* Mark bundle as not supporting multiuse
< HTTP/1.1 200 OK
< Date: Thu, 14 Jul 2022 07:24:11 GMT
< Content-Type: text/plain
< Content-Length: 0
< Connection: keep-alive
<
* Connection #0 to host 138.2.44.237 left intact
```


```
$ time curl -Ivs -X OPTIONS http://140.83.63.223:80
HTTP/1.1 200 OK
Date: Thu, 14 Jul 2022 07:36:45 GMT
Content-Type: text/plain
Content-Length: 0
Connection: keep-alive

*   Trying 140.83.63.223:80...
* Connected to 140.83.63.223 (140.83.63.223) port 80 (#0)
> OPTIONS / HTTP/1.1
> Host: 140.83.63.223
> User-Agent: curl/7.78.0
> Accept: */*
>
* Mark bundle as not supporting multiuse
< HTTP/1.1 200 OK
< Date: Thu, 14 Jul 2022 07:36:45 GMT
< Content-Type: text/plain
< Content-Length: 0
< Connection: keep-alive
<
* Connection #0 to host 140.83.63.223 left intact

real    0m0.878s
user    0m0.000s
sys     0m0.015s


```


