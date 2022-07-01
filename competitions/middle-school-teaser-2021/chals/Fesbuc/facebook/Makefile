build:
	docker build . -t facebook-django-8787537151898

run: build
	docker run -p 8081:8000 facebook-django-8787537151898

clean:
	docker rm -f -v facebook-django-8787537151898

generate-img:
	docker run -d --name facebook-django-8787537151898 facebook-django-8787537151898:latest
	docker export facebook-django-8787537151898 -o vm.tar.gz
	docker stop facebook-django-8787537151898