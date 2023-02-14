build:
	@docker build . -t chal_host-8785501710141 -q

run: build
	@docker run  chal_host-8785501710141

clean:
	@docker rm -f -v chal_host-8785501710141

generate-img:
	docker run -d --name chal_host-8785501710141 chal_host-8785501710141:latest
	docker export chal_host-8785501710141 -o vm.tar.gz
	docker stop chal_host-8785501710141