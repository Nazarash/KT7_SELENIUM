.PHONY: test
test:
	pytest --alluredir=allure-results
allure:
	allure serve allure-results