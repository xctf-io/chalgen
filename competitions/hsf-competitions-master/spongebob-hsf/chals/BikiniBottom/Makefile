build:
	docker build . -t static_site-119150911570

run: build
	docker run -p 8080:80 static_site-119150911570

clean:
	docker rm -f -v static_site-119150911570

generate-img:
	docker run -d --name static_site-119150911570 static_site-119150911570:latest
	docker export static_site-119150911570 -o vm.tar.gz
	docker stop static_site-119150911570