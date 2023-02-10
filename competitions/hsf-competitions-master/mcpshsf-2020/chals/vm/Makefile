build:
	docker build . -t alpine_vm-8781558027231

run: build
	docker run -p 8081:80 alpine_vm-8781558027231

clean:
	docker rm -f -v alpine_vm-8781558027231

generate-img:
	docker run -d --name alpine_vm-8781558027231 alpine_vm-8781558027231:latest
	docker export alpine_vm-8781558027231 -o vm.tar.gz
	docker stop alpine_vm-8781558027231