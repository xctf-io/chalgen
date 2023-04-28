build:
	@docker build . -t alpine_vm-302287781 -q

run: build
	@docker run -p 8081:80 alpine_vm-302287781

clean:
	@docker rm -f -v alpine_vm-302287781

generate-img:
	@docker run -d --name alpine_vm-302287781 alpine_vm-302287781:latest
	@docker export alpine_vm-302287781 -o vm.tar.gz
	@docker rm alpine_vm-302287781
	@docker rmi alpine_vm-302287781