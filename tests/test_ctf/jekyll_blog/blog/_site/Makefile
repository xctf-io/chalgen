build:
	docker build . -t jekyll-blog-8761992963027

run: build
	docker run -p 8081:80 jekyll-blog-8761992963027

clean:
	docker rm -f -v jekyll-blog-8761992963027

generate-img:
	docker run -d --name jekyll-blog-8761992963027 jekyll-blog-8761992963027:latest
	docker export jekyll-blog-8761992963027 -o vm.tar.gz
	docker stop jekyll-blog-8761992963027