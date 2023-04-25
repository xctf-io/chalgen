build:
	@docker build . -t chal_host-8743123899645 -q

run: build
	@docker run  chal_host-8743123899645

clean:
	@docker rm -f -v chal_host-8743123899645

generate-img:
	@docker run -d --name chal_host-8743123899645 chal_host-8743123899645:latest
	@docker export chal_host-8743123899645 -o vm.tar.gz
	@docker rm chal_host-8743123899645
	@docker rmi chal_host-8743123899645