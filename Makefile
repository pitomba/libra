
clean:
	find . -name '*.pyc' | xargs rm -f
	rm -rf build

deploy-prod:
	fab -i ~/Documents/victorpantoja.pem prod deploy

setup:
	@echo "Installing dependencies..."
	@pip install -r requirements-dev.txt --no-deps

start:
	PYTHONPATH=`pwd`:`pwd`/libra python libra/server.py ${PORT}
