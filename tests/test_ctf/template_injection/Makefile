build:
	docker build . -t temp_inj-120902214753

run: build
	docker run -p 8080:8080 --cap-drop all --cap-add chown --cap-add setuid --cap-add setgid         --cap-add sys_admin --security-opt apparmor=unconfined --security-opt seccomp=unconfined temp_inj-120902214753

clean:
	docker rm -f -v temp_inj-120902214753

generate-img:
	docker run -d --name temp_inj-120902214753 temp_inj-120902214753:latest
	docker export temp_inj-120902214753 -o vm.tar.gz
	docker stop temp_inj-120902214753