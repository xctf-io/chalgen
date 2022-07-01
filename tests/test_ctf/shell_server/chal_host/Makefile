build:
	docker build . -t chal_host-8729873248525

run: build
	docker run  chal_host-8729873248525

clean:
	docker rm -f -v chal_host-8729873248525

generate-img:
	docker run -d --name chal_host-8729873248525 chal_host-8729873248525:latest
	docker export chal_host-8729873248525 -o vm.tar.gz
	docker stop chal_host-8729873248525