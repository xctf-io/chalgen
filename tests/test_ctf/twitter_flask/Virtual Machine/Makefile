build:
	docker build . -t alpine_vm-8786335639682

run: build
	docker run  alpine_vm-8786335639682

clean:
	docker rm -f -v alpine_vm-8786335639682

generate-img:
	docker run -d --name alpine_vm-8786335639682 alpine_vm-8786335639682:latest
	docker export alpine_vm-8786335639682 -o vm.tar.gz
	docker stop alpine_vm-8786335639682