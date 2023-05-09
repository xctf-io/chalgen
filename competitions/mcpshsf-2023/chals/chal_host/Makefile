build:
	@docker build . -t chal_host-346942677 -q

run: build
	@docker run  chal_host-346942677

clean:
	@docker rm -f -v chal_host-346942677

generate-img:
	@docker run -d --name chal_host-346942677 chal_host-346942677:latest
	@docker export chal_host-346942677 -o vm.tar.gz
	@docker rm chal_host-346942677
	@docker rmi chal_host-346942677