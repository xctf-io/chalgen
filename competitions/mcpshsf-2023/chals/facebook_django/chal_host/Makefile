build:
	docker build  --platform linux/amd64 . -t chal_host-8756468667781

run: build
	docker run  chal_host-8756468667781

clean:
	docker rm -f -v chal_host-8756468667781

generate-img:
	docker run -d --name chal_host-8756468667781 chal_host-8756468667781:latest
	docker export chal_host-8756468667781 -o vm.tar.gz
	docker stop chal_host-8756468667781