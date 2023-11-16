build:
	@docker build  --platform linux/amd64 . -t alpine_vm-343633301

run: build
	@docker run -p 8081:80 alpine_vm-343633301

clean:
	@docker rm -f -v alpine_vm-343633301

generate-img:
	@docker run -d --name alpine_vm-343633301 alpine_vm-343633301:latest
	@docker export alpine_vm-343633301 -o vm.tar.gz
	@docker rm alpine_vm-343633301
	@docker rmi alpine_vm-343633301