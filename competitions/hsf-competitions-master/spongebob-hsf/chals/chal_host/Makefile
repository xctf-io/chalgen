build:
	docker build . -t chal_host-119150926288

run: build
	docker run  chal_host-119150926288

clean:
	docker rm -f -v chal_host-119150926288

generate-img:
	docker run -d --name chal_host-119150926288 chal_host-119150926288:latest
	docker export chal_host-119150926288 -o vm.tar.gz
	docker stop chal_host-119150926288