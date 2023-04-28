build:
	@docker build . -t chal_host-319385013 -q

run: build
	@docker run  chal_host-319385013

clean:
	@docker rm -f -v chal_host-319385013

generate-img:
	@docker run -d --name chal_host-319385013 chal_host-319385013:latest
	@docker export chal_host-319385013 -o vm.tar.gz
	@docker rm chal_host-319385013
	@docker rmi chal_host-319385013