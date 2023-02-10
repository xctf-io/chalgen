build:
	docker build . -t jekyll-blog-8781557909880

run: build
	docker run -p 8081:80 jekyll-blog-8781557909880

clean:
	docker rm -f -v jekyll-blog-8781557909880

generate-img:
	docker run -d --name jekyll-blog-8781557909880 jekyll-blog-8781557909880:latest
	docker export jekyll-blog-8781557909880 -o vm.tar.gz
	docker stop jekyll-blog-8781557909880