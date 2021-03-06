# Makefile for Little-Wire

CC=gcc
CXX=g++

# FIXME: Need to add OSX stuff
ifeq ($(shell uname), Linux)
	USBFLAGS = `libusb-config --cflags`
	USBLIBS = `libusb-config --libs`
	EXE_SUFFIX =
	OSFLAG = -D LINUX
else
	USBFLAGS = -I C:\MinGW\include
	USBLIBS = -L C:\MinGW\lib -lusb
	EXE_SUFFIX = .exe
	OSFLAG = -D WIN
endif

LIBS    = $(USBLIBS)
INCLUDE = library
CFLAGS = $(USBFLAGS) $(LIBS) -I$(INCLUDE) -O -Wall -pedantic -g $(OSFLAG)
CXXFLAGS = $(USBFLAGS) $(LIBS) -I$(INCLUDE) -O -Wall -pedantic -g $(OSFLAG)

LWLIBS = opendevice littleWire littleWire_util
EXAMPLES = adc blink button servo i2c_blinkM spi_LTC1448

.PHONY:	clean library docs

all: library $(EXAMPLES)

library: $(LWLIBS)

$(LWLIBS):
	@echo Building libraries...
	$(CXX) $(CXXFLAGS) -c library/littleWire.cpp
	$(CC) $(CFLAGS) -c library/opendevice.c
	$(CC) $(CFLAGS) -c library/littleWire_util.c

$(EXAMPLES): $(addsuffix .o, $(LWLIBS))
	@echo Building example: $@...
	$(CXX) $(CXXFLAGS) -o $@$(EXE_SUFFIX) examples/$@.cpp $^ $(LIBS)

docs:
	doxygen ./docs/doxygen.conf
	cd ./docs/latex/; make all

clean:
	rm -rf $(EXAMPLES)$(EXE_SUFFIX) *.o *.exe docs/html docs/latex
