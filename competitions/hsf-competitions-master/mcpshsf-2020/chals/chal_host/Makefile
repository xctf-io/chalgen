build:
	docker build . -t chal_host-8781578356881

run: build
	docker run  chal_host-8781578356881

clean:
	docker rm -f -v chal_host-8781578356881

generate-img:
	docker run -d --name chal_host-8781578356881 chal_host-8781578356881:latest
	docker export chal_host-8781578356881 -o vm.tar.gz
	docker stop chal_host-8781578356881