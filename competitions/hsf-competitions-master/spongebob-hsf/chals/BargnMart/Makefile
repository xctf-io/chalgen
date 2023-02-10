build:
	docker build . -t static_site-119150921491

run: build
	docker run -p 8080:80 static_site-119150921491

clean:
	docker rm -f -v static_site-119150921491

generate-img:
	docker run -d --name static_site-119150921491 static_site-119150921491:latest
	docker export static_site-119150921491 -o vm.tar.gz
	docker stop static_site-119150921491