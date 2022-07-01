build:
	docker build . -t chal_host-8787542345765

run: build
	docker run  chal_host-8787542345765

clean:
	docker rm -f -v chal_host-8787542345765

generate-img:
	docker run -d --name chal_host-8787542345765 chal_host-8787542345765:latest
	docker export chal_host-8787542345765 -o vm.tar.gz
	docker stop chal_host-8787542345765