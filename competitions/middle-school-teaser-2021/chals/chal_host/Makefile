build:
	@docker build . -t chal_host-8776764456157 -q

run: build
	@docker run  chal_host-8776764456157

clean:
	@docker rm -f -v chal_host-8776764456157

generate-img:
	@docker run -d --name chal_host-8776764456157 chal_host-8776764456157:latest
	@docker export chal_host-8776764456157 -o vm.tar.gz
	@docker rm chal_host-8776764456157
	@docker rmi chal_host-8776764456157