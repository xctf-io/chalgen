build:
	docker build . -t chal_host-274935801

run: build
	docker run  chal_host-274935801

clean:
	docker rm -f -v chal_host-274935801

generate-img:
	docker run -d --name chal_host-274935801 chal_host-274935801:latest
	docker export chal_host-274935801 -o vm.tar.gz
	docker stop chal_host-274935801