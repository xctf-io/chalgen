build:
	@docker build  --platform linux/amd64 . -t static_site-8737150909203

run: build
	@docker run -p 8080:80 static_site-8737150909203

clean:
	@docker rm -f -v static_site-8737150909203

generate-img:
	@docker run -d --name static_site-8737150909203 static_site-8737150909203:latest
	@docker export static_site-8737150909203 -o vm.tar.gz
	@docker rm static_site-8737150909203
	@docker rmi static_site-8737150909203