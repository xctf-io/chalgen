build:
	@docker build . -t chal_host-304576913 -q

run: build
	@docker run  chal_host-304576913

clean:
	@docker rm -f -v chal_host-304576913

generate-img:
	@docker run -d --name chal_host-304576913 chal_host-304576913:latest
	@docker export chal_host-304576913 -o vm.tar.gz
	@docker rm chal_host-304576913
	@docker rmi chal_host-304576913