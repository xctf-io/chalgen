build:
	docker build  --platform linux/amd64 . -t chal_host-8787440261717

run: build
	docker run  chal_host-8787440261717

clean:
	docker rm -f -v chal_host-8787440261717

generate-img:
	docker run -d --name chal_host-8787440261717 chal_host-8787440261717:latest
	docker export chal_host-8787440261717 -o vm.tar.gz
	docker stop chal_host-8787440261717