build:
	docker build . -t chal_host-8786335643935

run: build
	docker run  chal_host-8786335643935

clean:
	docker rm -f -v chal_host-8786335643935

generate-img:
	docker run -d --name chal_host-8786335643935 chal_host-8786335643935:latest
	docker export chal_host-8786335643935 -o vm.tar.gz
	docker stop chal_host-8786335643935