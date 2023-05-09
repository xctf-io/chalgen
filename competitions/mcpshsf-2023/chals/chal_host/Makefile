build:
	@docker build . -t chal_host-8755269800552 -q

run: build
	@docker run  chal_host-8755269800552

clean:
	@docker rm -f -v chal_host-8755269800552

generate-img:
	@docker run -d --name chal_host-8755269800552 chal_host-8755269800552:latest
	@docker export chal_host-8755269800552 -o vm.tar.gz
	@docker rm chal_host-8755269800552
	@docker rmi chal_host-8755269800552