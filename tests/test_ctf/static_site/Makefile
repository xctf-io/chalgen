build:
	docker build . -t static_site-8728970303067

run: build
	docker run -p 8080:80 static_site-8728970303067

clean:
	docker rm -f -v static_site-8728970303067

generate-img:
	docker run -d --name static_site-8728970303067 static_site-8728970303067:latest
	docker export static_site-8728970303067 -o vm.tar.gz
	docker stop static_site-8728970303067