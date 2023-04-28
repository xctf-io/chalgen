build:
	@docker build . -t chal_host-306763021 -q

run: build
	@docker run  chal_host-306763021

clean:
	@docker rm -f -v chal_host-306763021

generate-img:
	@docker run -d --name chal_host-306763021 chal_host-306763021:latest
	@docker export chal_host-306763021 -o vm.tar.gz
	@docker rm chal_host-306763021
	@docker rmi chal_host-306763021