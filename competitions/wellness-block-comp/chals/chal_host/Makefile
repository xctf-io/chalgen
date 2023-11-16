build:
	@docker build  --platform linux/amd64 . -t chal_host

run: build
	@docker run  chal_host

clean:
	@docker rm -f -v chal_host

generate-img:
	@docker run -d --name chal_host chal_host:latest
	@docker export chal_host -o vm.tar.gz
	@docker rm chal_host
	@docker rmi chal_host