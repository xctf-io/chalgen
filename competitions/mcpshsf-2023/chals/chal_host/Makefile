build:
	@docker build . -t chal_host-304924085 -q

run: build
	@docker run  chal_host-304924085

clean:
	@docker rm -f -v chal_host-304924085

generate-img:
	@docker run -d --name chal_host-304924085 chal_host-304924085:latest
	@docker export chal_host-304924085 -o vm.tar.gz
	@docker rm chal_host-304924085
	@docker rmi chal_host-304924085