# Compiler
CC = gcc

# Compiler flags
CFLAGS = -Wall -Wextra -std=c11 -lm

# Target executable
TARGET = closesIntR

# Source files
SRC = closesIntR.c

# Default rule to build and run the program
all: $(TARGET)
    ./$(TARGET)

# Rule to compile the program
$(TARGET): $(SRC)
    $(CC) $(CFLAGS) -o $(TARGET) $(SRC)

# Clean rule to remove the compiled files
clean:
    rm -f $(TARGET)