build:
	docker build . -t chal_host-8728972503071

run: build
	docker run  chal_host-8728972503071

clean:
	docker rm -f -v chal_host-8728972503071

generate-img:
	docker run -d --name chal_host-8728972503071 chal_host-8728972503071:latest
	docker export chal_host-8728972503071 -o vm.tar.gz
	docker stop chal_host-8728972503071