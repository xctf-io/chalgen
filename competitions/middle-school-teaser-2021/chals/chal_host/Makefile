build:
	@docker build . -t chal_host-307419841 -q

run: build
	@docker run  chal_host-307419841

clean:
	@docker rm -f -v chal_host-307419841

generate-img:
	@docker run -d --name chal_host-307419841 chal_host-307419841:latest
	@docker export chal_host-307419841 -o vm.tar.gz
	@docker rm chal_host-307419841
	@docker rmi chal_host-307419841