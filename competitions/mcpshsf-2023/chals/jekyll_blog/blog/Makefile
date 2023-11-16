build:
	@docker build  --platform linux/amd64 . -t jekyll-blog-343637601

run: build
	@docker run -p 8081:80 jekyll-blog-343637601

clean:
	@docker rm -f -v jekyll-blog-343637601

generate-img:
	@docker run -d --name jekyll-blog-343637601 jekyll-blog-343637601:latest
	@docker export jekyll-blog-343637601 -o vm.tar.gz
	@docker rm jekyll-blog-343637601
	@docker rmi jekyll-blog-343637601