build:
	@docker build . -t chal_host-8773376674699 -q

run: build
	@docker run  chal_host-8773376674699

clean:
	@docker rm -f -v chal_host-8773376674699

generate-img:
	@docker run -d --name chal_host-8773376674699 chal_host-8773376674699:latest
	@docker export chal_host-8773376674699 -o vm.tar.gz
	@docker rm chal_host-8773376674699
	@docker rmi chal_host-8773376674699