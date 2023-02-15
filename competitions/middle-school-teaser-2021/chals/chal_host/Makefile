build:
	@docker build . -t chal_host-8756733825729 -q

run: build
	@docker run  chal_host-8756733825729

clean:
	@docker rm -f -v chal_host-8756733825729

generate-img:
	docker run -d --name chal_host-8756733825729 chal_host-8756733825729:latest
	docker export chal_host-8756733825729 -o vm.tar.gz
	docker stop chal_host-8756733825729