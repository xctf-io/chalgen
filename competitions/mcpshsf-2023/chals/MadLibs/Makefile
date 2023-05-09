build:
	@docker build . -t temp_inj-8793342911519 -q

run: build
	@docker run -p 8080:8080 --cap-drop all --cap-add chown --cap-add setuid --cap-add setgid         --cap-add sys_admin --security-opt apparmor=unconfined --security-opt seccomp=unconfined temp_inj-8793342911519

clean:
	@docker rm -f -v temp_inj-8793342911519

generate-img:
	@docker run -d --name temp_inj-8793342911519 temp_inj-8793342911519:latest
	@docker export temp_inj-8793342911519 -o vm.tar.gz
	@docker rm temp_inj-8793342911519
	@docker rmi temp_inj-8793342911519