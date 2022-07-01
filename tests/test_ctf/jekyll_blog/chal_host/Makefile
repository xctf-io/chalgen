build:
	docker build . -t chal_host-8761992966928

run: build
	docker run  chal_host-8761992966928

clean:
	docker rm -f -v chal_host-8761992966928

generate-img:
	docker run -d --name chal_host-8761992966928 chal_host-8761992966928:latest
	docker export chal_host-8761992966928 -o vm.tar.gz
	docker stop chal_host-8761992966928