# Compiler
CC = gcc

# Compiler flags
CFLAGS = -Wall -Wextra -std=c11 -lm

# Default rule (if you just type 'make')
all:
	@echo "Usage: make filename.c"
	@echo "Or use: make run filename.c to compile and run"

# Pattern rule to compile any .c file
%.c:
	$(CC) $(CFLAGS) -o $* $@

# Alternative syntax if the above doesn't work in some environments
.PHONY: %.c
%.c:
	$(CC) $(CFLAGS) -o $* $@

# Clean rule
clean:
	rm -f *.o a.out

# Rule to compile and run any program
run: 
	@if [ -z "$(filter-out run,$(MAKECMDGOALS))" ]; then \
		echo "Usage: make run filename.c"; \
	else \
		file=$(filter-out run,$(MAKECMDGOALS)) && \
		base=$${file%.c} && \
		$(CC) $(CFLAGS) -o $$base $$file && \
		./$$base; \
	fi

# Prevent errors when using the run rule with a filename
%:
	@:
