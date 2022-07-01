build:
	docker build . -t temp_inj-8754429288512
	#echo temp_inj-8754429288512

run: build
	docker run -p 8080:8080 --cap-drop all --cap-add chown --cap-add setuid --cap-add setgid         --cap-add sys_admin --security-opt apparmor=unconfined --security-opt seccomp=unconfined temp_inj-8754429288512

clean:
	docker rm -f -v temp_inj-8754429288512

generate-img:
	docker run -d --name temp_inj-8754429288512 temp_inj-8754429288512:latest
	docker export temp_inj-8754429288512 -o vm.tar.gz
	docker stop temp_inj-8754429288512