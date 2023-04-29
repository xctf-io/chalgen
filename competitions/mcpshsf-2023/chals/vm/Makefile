build:
	@docker build . -t alpine_vm-302457845 -q

run: build
	@docker run -p 8081:80 alpine_vm-302457845

clean:
	@docker rm -f -v alpine_vm-302457845

generate-img:
	@docker run -d --name alpine_vm-302457845 alpine_vm-302457845:latest
	@docker export alpine_vm-302457845 -o vm.tar.gz
	@docker rm alpine_vm-302457845
	@docker rmi alpine_vm-302457845