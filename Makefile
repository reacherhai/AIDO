PORT = 8056

todocli:
	-rm -rf ~/.toduh

runserver:
	python manage.py runserver 0.0.0.0:$(PORT)
