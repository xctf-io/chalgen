build:
	@docker build . -t chal_host-304889389 -q

run: build
	@docker run  chal_host-304889389

clean:
	@docker rm -f -v chal_host-304889389

generate-img:
	@docker run -d --name chal_host-304889389 chal_host-304889389:latest
	@docker export chal_host-304889389 -o vm.tar.gz
	@docker rm chal_host-304889389
	@docker rmi chal_host-304889389