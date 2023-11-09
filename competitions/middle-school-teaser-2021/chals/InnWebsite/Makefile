build:
	@docker build . -t static_site-377556161

run: build
	@docker run -p 8080:80 static_site-377556161

clean:
	@docker rm -f -v static_site-377556161

generate-img:
	@docker run -d --name static_site-377556161 static_site-377556161:latest
	@docker export static_site-377556161 -o vm.tar.gz
	@docker rm static_site-377556161
	@docker rmi static_site-377556161