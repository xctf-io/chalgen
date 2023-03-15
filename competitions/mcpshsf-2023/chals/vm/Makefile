build:
	@docker build . -t alpine_vm-8791523345737 -q

run: build
	@docker run -p 8081:80 alpine_vm-8791523345737

clean:
	@docker rm -f -v alpine_vm-8791523345737

generate-img:
	@docker run -d --name alpine_vm-8791523345737 alpine_vm-8791523345737:latest
	@docker export alpine_vm-8791523345737 -o vm.tar.gz
	@docker rm alpine_vm-8791523345737
	@docker rmi alpine_vm-8791523345737