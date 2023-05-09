build:
	@docker build . -t jekyll-blog-378028045 -q

run: build
	@docker run -p 8081:80 jekyll-blog-378028045

clean:
	@docker rm -f -v jekyll-blog-378028045

generate-img:
	@docker run -d --name jekyll-blog-378028045 jekyll-blog-378028045:latest
	@docker export jekyll-blog-378028045 -o vm.tar.gz
	@docker rm jekyll-blog-378028045
	@docker rmi jekyll-blog-378028045