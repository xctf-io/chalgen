build:
	docker build  --platform linux/amd64 . -t chal_host-8729619655940

run: build
	docker run  chal_host-8729619655940

clean:
	docker rm -f -v chal_host-8729619655940

generate-img:
	docker run -d --name chal_host-8729619655940 chal_host-8729619655940:latest
	docker export chal_host-8729619655940 -o vm.tar.gz
	docker stop chal_host-8729619655940