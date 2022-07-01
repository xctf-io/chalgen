build:
	docker build . -t chal_host-8793010507563

run: build
	docker run  chal_host-8793010507563

clean:
	docker rm -f -v chal_host-8793010507563

generate-img:
	docker run -d --name chal_host-8793010507563 chal_host-8793010507563:latest
	docker export chal_host-8793010507563 -o vm.tar.gz
	docker stop chal_host-8793010507563