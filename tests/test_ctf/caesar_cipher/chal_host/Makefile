build:
	docker build . -t chal_host-283127309

run: build
	docker run  chal_host-283127309

clean:
	docker rm -f -v chal_host-283127309

generate-img:
	docker run -d --name chal_host-283127309 chal_host-283127309:latest
	docker export chal_host-283127309 -o vm.tar.gz
	docker stop chal_host-283127309