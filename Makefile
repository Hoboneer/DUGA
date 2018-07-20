.PHONY: clean
clean:
	@echo Cleaning...
	@for /d %%d in (*.build) do @rmdir /s /q %%d
	@for /d %%d in (*.dist) do @rmdir /s /q %%d
	@if exist *.pyd @erase *.pyd
	@if exist *.pyi @erase *.pyi
	@if exist *.exe @erase *.exe
	@if exist *.dll @erase *.dll
	@if exist *.a @erase *.a

# Data files not copied over-- needs to be done manually
.PHONY: standalone
standalone:
	@make clean
	pipenv run nuitka MAIN.py --standalone --show-progress
	@rem If the above fails, then the echo should go through, meaning
	@rem there is no need for any &s
	@echo compilation complete 

.PHONY: module
module:
ifndef mod
	$(error `mod` not set)
endif
	@make clean

	pipenv run nuitka $(mod) --module --show-progress
	@echo compilation complete 
