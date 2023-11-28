build:
	@docker build  --platform linux/amd64 . -t chal_host-8792530824673 -q

run: build
	@docker run  chal_host-8792530824673

clean:
	@docker rm -f -v chal_host-8792530824673

generate-img:
	docker run -d --name chal_host-8792530824673 chal_host-8792530824673:latest
	docker export chal_host-8792530824673 -o vm.tar.gz
	docker stop chal_host-8792530824673