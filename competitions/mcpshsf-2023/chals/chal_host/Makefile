build:
	@docker build . -t chal_host-306800201 -q

run: build
	@docker run  chal_host-306800201

clean:
	@docker rm -f -v chal_host-306800201

generate-img:
	@docker run -d --name chal_host-306800201 chal_host-306800201:latest
	@docker export chal_host-306800201 -o vm.tar.gz
	@docker rm chal_host-306800201
	@docker rmi chal_host-306800201