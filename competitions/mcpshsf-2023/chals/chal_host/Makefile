build:
	@docker build . -t chal_host-8781800195730 -q

run: build
	@docker run  chal_host-8781800195730

clean:
	@docker rm -f -v chal_host-8781800195730

generate-img:
	@docker run -d --name chal_host-8781800195730 chal_host-8781800195730:latest
	@docker export chal_host-8781800195730 -o vm.tar.gz
	@docker rm chal_host-8781800195730
	@docker rmi chal_host-8781800195730