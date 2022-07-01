build:
	docker build . -t chal_host-281350177

run: build
	docker run  chal_host-281350177

clean:
	docker rm -f -v chal_host-281350177

generate-img:
	docker run -d --name chal_host-281350177 chal_host-281350177:latest
	docker export chal_host-281350177 -o vm.tar.gz
	docker stop chal_host-281350177