build:
	docker build . -t facebook-django-8781578493730

run: build
	docker run -p 8081:8000 facebook-django-8781578493730

clean:
	docker rm -f -v facebook-django-8781578493730

generate-img:
	docker run -d --name facebook-django-8781578493730 facebook-django-8781578493730:latest
	docker export facebook-django-8781578493730 -o vm.tar.gz
	docker stop facebook-django-8781578493730