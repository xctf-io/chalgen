build:
	@docker build . -t alpine_vm-310405585 -q

run: build
	@docker run -p 8081:80 alpine_vm-310405585

clean:
	@docker rm -f -v alpine_vm-310405585

generate-img:
	@docker run -d --name alpine_vm-310405585 alpine_vm-310405585:latest
	@docker export alpine_vm-310405585 -o vm.tar.gz
	@docker rm alpine_vm-310405585
	@docker rmi alpine_vm-310405585