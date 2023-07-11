build:
	docker build -t ball_pass --target base .

build-test:
	docker build -t ball_pass_test --target test .

test:
	docker run -it \
	-v $(PWD):/ball-pass \
	ball_pass_test

run:
	docker run -it \
	-v $(PWD)/input_files:/ball-pass/input_files/ \
	ball_pass input_files/$(FILE)