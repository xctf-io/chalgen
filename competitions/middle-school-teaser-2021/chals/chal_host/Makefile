build:
	@docker build . -t chal_host-8750599668813 -q

run: build
	@docker run  chal_host-8750599668813

clean:
	@docker rm -f -v chal_host-8750599668813

generate-img:
	docker run -d --name chal_host-8750599668813 chal_host-8750599668813:latest
	docker export chal_host-8750599668813 -o vm.tar.gz
	docker stop chal_host-8750599668813