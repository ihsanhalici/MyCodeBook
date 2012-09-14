#!/usr/bin/env python
import os
import serial

sensetive = "10" ## Mouse Hassasiyet Degeri - Mouse Sensetive ##

SERIAL_PORT     = '/dev/ttyACM0'
SERI_BAUDRATE   = 9600
SERI_BYTESIZE   = 8
SERI_PARITY     = 'N'
SERI_STOPBITS   = 1
SERI_TIMEOUT    = 0.2
SERI_BUFFER_SIZE= 1024

def seriBaglan():
    bag             = serial.Serial()
    bag.port        = SERIAL_PORT
    bag.baudrate    = SERI_BAUDRATE
    bag.bytesize    = SERI_BYTESIZE
    bag.parity      = SERI_PARITY
    bag.stopbits    = SERI_STOPBITS
    bag.timeout     = SERI_TIMEOUT
    bag.open()
    return bag
bag = seriBaglan()
while 1:

	gelen  = bag.readline()
	for gl in gelen:
		gl = str(gl)
	
	asagi        = gelen.find("F38")		
	yukari       = gelen.find("B38")
	sag  	     = gelen.find("738")
	sol 	     = gelen.find("338")
	sagclick     = gelen.find("5E25")
	solclick     = gelen.find("70")
	asagitik     = gelen.find("C90")
	yukgitik     = gelen.find("490")



	if asagi == 0:
		print "asagi"
		os.system("xdotool mousemove_relative 0 %s" %sensetive)
	if yukari == 0:
		print "yukari"
		os.system("xdotool mousemove_relative -- 0 -%s" %sensetive)
	if sag == 0:
		os.system("xdotool mousemove_relative %s 0" %sensetive)
	if sol == 0:
		os.system("xdotool mousemove_relative -- -%s 0" %sensetive)
	if solclick == 0:
		os.system("xdotool click 3")
	if sagclick == 0:
		os.system("xdotool click 1")
	if asagitik == 0:
		os.system("xdotool click 5")
	if yukgitik == 0:
		os.system("xdotool click 4")				
