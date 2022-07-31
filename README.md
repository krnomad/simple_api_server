# simple_api_server

Based on `fastapi`, this is the source of building a simple API server using `sqlalchemy` and `DI`.

Creating CI/CD using github action and distributing it based on container is also a goal to guide.

Aims to build an API sample test environment with ultra-simple commands

# pre requirements
* Install docker
* Install docker-compose

# Get started
```
docker-compose up -d
```

# How to access
ex) When running docker-compose command on server with IP address 192.168.0.7
```
> curl http://192.168.1.5:8081/data


StatusCode        : 200
StatusDescription : OK
Content           : {"hello":1235}
RawContent        : HTTP/1.1 200 OK
                    Content-Length: 14
                    Content-Type: application/json
                    Date: Sun, 31 Jul 2022 02:20:11 GMT
                    Server: uvic
```

