build:
	@docker build . -t chal_host-302191029 -q

run: build
	@docker run  chal_host-302191029

clean:
	@docker rm -f -v chal_host-302191029

generate-img:
	@docker run -d --name chal_host-302191029 chal_host-302191029:latest
	@docker export chal_host-302191029 -o vm.tar.gz
	@docker rm chal_host-302191029
	@docker rmi chal_host-302191029