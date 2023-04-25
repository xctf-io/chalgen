build:
	@docker build . -t chal_host-8748536445585 -q

run: build
	@docker run  chal_host-8748536445585

clean:
	@docker rm -f -v chal_host-8748536445585

generate-img:
	@docker run -d --name chal_host-8748536445585 chal_host-8748536445585:latest
	@docker export chal_host-8748536445585 -o vm.tar.gz
	@docker rm chal_host-8748536445585
	@docker rmi chal_host-8748536445585