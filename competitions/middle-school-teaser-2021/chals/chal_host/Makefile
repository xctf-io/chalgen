build:
	@docker build . -t chal_host-8732723900213 -q

run: build
	@docker run  chal_host-8732723900213

clean:
	@docker rm -f -v chal_host-8732723900213

generate-img:
	docker run -d --name chal_host-8732723900213 chal_host-8732723900213:latest
	docker export chal_host-8732723900213 -o vm.tar.gz
	docker stop chal_host-8732723900213