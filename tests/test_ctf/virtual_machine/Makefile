build:
	docker build  --platform linux/amd64 . -t alpine_vm-8761580582373

run: build
	docker run  alpine_vm-8761580582373

clean:
	docker rm -f -v alpine_vm-8761580582373

generate-img:
	docker run -d --name alpine_vm-8761580582373 alpine_vm-8761580582373:latest
	docker export alpine_vm-8761580582373 -o vm.tar.gz
	docker stop alpine_vm-8761580582373