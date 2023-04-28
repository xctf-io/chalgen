build:
	@docker build . -t chal_host-306763989 -q

run: build
	@docker run  chal_host-306763989

clean:
	@docker rm -f -v chal_host-306763989

generate-img:
	@docker run -d --name chal_host-306763989 chal_host-306763989:latest
	@docker export chal_host-306763989 -o vm.tar.gz
	@docker rm chal_host-306763989
	@docker rmi chal_host-306763989