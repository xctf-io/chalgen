build:
	@docker build . -t chal_host-8791128482883 -q

run: build
	@docker run  chal_host-8791128482883

clean:
	@docker rm -f -v chal_host-8791128482883

generate-img:
	@docker run -d --name chal_host-8791128482883 chal_host-8791128482883:latest
	@docker export chal_host-8791128482883 -o vm.tar.gz
	@docker rm chal_host-8791128482883
	@docker rmi chal_host-8791128482883