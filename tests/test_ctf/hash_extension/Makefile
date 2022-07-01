build:
	docker build . -t hash_ext-89788385615

run: build
	docker run -p 8080:80 hash_ext-89788385615

clean:
	docker rm -f -v hash_ext-89788385615

generate-img:
	docker run -d --name hash_ext-89788385615 hash_ext-89788385615:latest
	docker export hash_ext-89788385615 -o vm.tar.gz
	docker stop hash_ext-89788385615