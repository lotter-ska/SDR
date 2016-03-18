# SDR
Gnu radio and python scripts for RTL-SDR


GNU Radio:

The easiest way to get gnuradio is to download the live environement:
https://gnuradio.org/redmine/projects/gnuradio/wiki/GNURadioLiveDVD

Create the boobable SD/USB:
http://www.ubuntu.com/download/desktop/create-a-usb-stick-on-windows

For booting from device enter Bios and select the device with the OS on.


Python scripts:
Most drivers/software required is installed on the live environment.  A superior rtl_power is used in the scripts, rtl_power_fftw.  This
can be installed(Linux machine) by following these instructions:
https://github.com/AD-Vega/rtl-power-fftw

The following libraries might be required to be compiled and added:
tclap-1.2.1
librtlsdr
rtl-power-fftw

If you want to install all rtl-sdr software from scratch the following link might be useful:
http://sdr.osmocom.org/trac/wiki/rtl-sdr
http://www.rtl-sdr.com/rtl-sdr-quick-start-guide/
