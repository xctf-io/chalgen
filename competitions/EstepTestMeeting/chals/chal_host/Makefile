build:
	@docker build . -t chal_host-8763061278421 -q

run: build
	@docker run  chal_host-8763061278421

clean:
	@docker rm -f -v chal_host-8763061278421

generate-img:
	@docker run -d --name chal_host-8763061278421 chal_host-8763061278421:latest
	@docker export chal_host-8763061278421 -o vm.tar.gz
	@docker rm chal_host-8763061278421
	@docker rmi chal_host-8763061278421