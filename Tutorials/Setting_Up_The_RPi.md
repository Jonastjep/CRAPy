# How to setup the Raspberry Pi (headless connection, remote access, wifi hotspot)

This project relies on the Raspberry Pi to be self relient and disconnected from the grid. This means that we need to set it up to be controlled remotely through ssh or VNC (secreenless or headless in techy terms) and make it host it's own local network for us to connect to. The end goal is to have the RPi host a Flask that we can access by connecting to it's hotspot.

## Flashing the RPi and connecting to it through WLAN/LAN

The fist step consists in actually flashing the RPi SD card with the OS (we used Raspbian as it is really handy). For this you can use any imager software like [Rufus](https://rufus.ie/) or even more practical nowadays, the official RPi Imager that you can find on their [site](https://www.raspberrypi.org/software/). With the latter you don't even need to download the [image of the OS](https://www.raspberrypi.org/software/operating-systems/) on your computer, but both imagers support the old way of actually downloading the Raspbian package onto your computer and flashing it to the SD card (my prefered way, as it also teaches you how to do these things for older or different software, as the concept is the same if you want to install Ubuntu or Debian on our actual machine, which I highly recommend!). The flashing process can take some time, but once it's finished, don't directly put it into the RPi, it need a little more configuration so that you don't require any screens/keyboards for the setting up.

The first step if to open the boot partition of the SD card (you should see two accessible hardrives connected to your computer, go into `boot`). There you simply need to create a new file titled `ssh`, with **NO EXTENTION** (which can be surprisingly complex on Windows; on GNU/Linux and MacOS, simply type `touch ssh` to create it). This simple step will tell the RPi to activate it's ssh connection when booting, which will allow you to take control later on. 

Activating ssh is nice, but it is totally useless if your RPi is not connected to your local network, as you won't be able to access it if it's the case. The configuration for the network is a little more involved but still very basic. In the same `boot` folder, you need to create a file called `wpa_supplicant.conf`. This file will give details to the network manager of the RPi and make it connect to the supplied network information automatically. The file should contain:

```bash
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1
country=<Insert 2 letter Icountry code - e.g. NL for Netherlands>

network={
 ssid="<Name of your wireless LAN>"
 psk="<Password for your wireless LAN>"
}
```

The fist two lines should not be changed, the third you can simply go on [wikipedia](https://en.wikipedia.org/wiki/ISO_3166-1) to check your country code and the last two entries are simply your wifi name and password. These will not be stored in plain text in case you are wondering.

Now with these two changes done, you can insert the SD card into your Raspberry Pi and turn it on. There are different ways to connect to a RPi for the first time when not yet knowing it's ip address, and probably the easiest is to try `ssh pi@raspberrypi.local`. This might fail if you have more than one RPi with the same name on the network. Once you are in through this method, you can simply type `hostname -I` to find your full ip address, or type `ifconfig` which just gives you more information. The second method consists in using the nmap command `nmap -sn ipAddressOfRouter/24` and find out which of the returned ip's is the RPi. The `ipAddressOfRouter` can be found by finding your own ip and changing the last number to a 1 (so if your local ip is 192.168.0.134, your router ip will be 192.168.0.1). This is a bit more involved because generally computers don't come directly with nmap, and it requires a few extra steps.

Congratulations! Now you should finally be connected to you clead install of Raspbian! the first two steps you should be doing is `sudo apt update` and `sudo apt upgrade` to upgrade all components to latest version available. This might take some time and would benefit from a reboot afterwards (this provides a good test that all your work has worked and you can reconnect even after a reboot). You can also start downloading all the programs/packages that you need for your projects.

## Finalizing the setting up of the RPi (static ip, VNC, I2C, SPI, RPiCam)

Now that you have your RPi up and running there are a few extra things that you might want to do depending on the use you have for your RPi. The first thing you might regret is not having a static ip address, as with time your router assigns a new one to your system and you have to go through figuring out what the ip is once more... It is actually possible to tell the router/modem to allocate you a fixed ip address.

First step to set this up is to check if DHCPCD is active by running `sudo service dhcpcd status` (it should be). If it is not, then you need to run 

```bash
sudo service dhcpcd start
sudo systemctl enable dhcpcd
```

With DHCPCD active, we can now go and make our configuration changes to `sudo nano /etc/dhcpcd.conf`. This means adding these lines:

```bash
interface wlan0
static ip_address=192.168.0.4/24 
static routers=192.168.0.1
static domain_name_servers=192.168.0.1
```

to the opened file. The first line explicitely says what type of interface this connection is (can be`wlan0` for wifi or `eth0` for ethernet conn.). The second is where you set which ip you want to set as static. You only need to change the last number and should be careful to choose a number that your modem will not assign to another device (you can check your DHCP range on your modem settings if you have access). Line 3-4 only explicitely show towards your router, and you have to choose the same ip as yours, but with a 1 a the last place. After this change, just `sudo reboot` and you should be able to reconnect using your new static ip address! This static ip is also very important in case you want to open your server to the rest of the internet and that other people can access it outside of your local network. This is called port-forwarding and can be set up in your modem settings, but will not be covered here.

Lastly, there are many more ways to control or take control of the raspberry pi. These are mostly kept in the same settings area. You can enter it by typing `sudo raspi-config`. This opens a GUI with many choices. To change the authorizations for remote interfaces etc, go into the subcategory "Interface Options" and there you can activate the RPi camera, the SPI and I2C connections and the VNC tunnelling (I don;t use much else from there, but keep in mind for the other interfaces you might one day use!

For the moment this is all, I hope you enjoyed and learned something! :)
