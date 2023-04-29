build:
	@docker build . -t temp_inj-304924157 -q

run: build
	@docker run -p 8080:8080 --cap-drop all --cap-add chown --cap-add setuid --cap-add setgid         --cap-add sys_admin --security-opt apparmor=unconfined --security-opt seccomp=unconfined temp_inj-304924157

clean:
	@docker rm -f -v temp_inj-304924157

generate-img:
	@docker run -d --name temp_inj-304924157 temp_inj-304924157:latest
	@docker export temp_inj-304924157 -o vm.tar.gz
	@docker rm temp_inj-304924157
	@docker rmi temp_inj-304924157