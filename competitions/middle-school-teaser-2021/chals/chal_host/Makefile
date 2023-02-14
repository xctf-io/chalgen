build:
	@docker build . -t chal_host-8769283743153 -q

run: build
	@docker run  chal_host-8769283743153

clean:
	@docker rm -f -v chal_host-8769283743153

generate-img:
	docker run -d --name chal_host-8769283743153 chal_host-8769283743153:latest
	docker export chal_host-8769283743153 -o vm.tar.gz
	docker stop chal_host-8769283743153