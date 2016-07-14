# pycoap
CoAP Python Client

# Dependencies
* [Python3](https://www.python.org/)
* [pip](https://pip.pypa.io/en/stable/)
* [AioCoAP](https://github.com/chrysn/aiocoap)
* [VirtualENV](https://virtualenv.pypa.io/en/stable/)

# Installation
### Client Side
Install :
```
git clone https://github.com/gzsierra/pycoap/
```
#### Configuration
In the file `coapSender.py`, you have to edit one line:
```
request.opt.uri_host = '[INSERT_YOUR_SERVER_IP]'
```
If you want to send data to another specific endpoint, you can edit this line (DON'T FORGET TO ADD THE RESSOURCE IN SERVER SIDE) :
```
request.opt.uri_path = ("[INSERT_ORGANISATIONAL_FOLDER]", "[FINAL_ENDPOINT_NAME]")
```
#### Usage
```
python3 pycoap.py [FILENAME]
```
### Server Side
Install :
```
git clone https://github.com/gzsierra/pycoap/
```
#### Configuration
In the file `pyServer.py`, if you want to add more ressource, you have to add another line like this :
```
root.add_resource(('[INSERT_ORGANISATIONAL_FOLDER]', '[FINAL_ENDPOINT_NAME]'), BlockResource())
```
#### Usage
```
python3 pyServer.py
```
### OpenHAB
For installation of OpenHAB, please refer to the [doc](https://github.com/openhab/openhab)

Script needed `pyGet.py` :
```
git clone https://github.com/gzsierra/pycoap/
```
Additional addon needed :
```
apt install openhab-addon-binding-exec
```
#### Configuration
  * File to edit 1 `items/demo.items`, for more details, please refer to the [doc](https://github.com/openhab/openhab/wiki/Exec-Binding) :

```
Number coapsw1                  "temp [%.1f °C]" (Temperature) {exec="<[/usr/bin/python3 /home/openhab/Documents/pycoap/pyGet.py:60000:REGEX((.*?))]"}
```
  * File to edit 2 `sitemap/demo.sitemap`:

```
sitemap demo label="Main Menu"
{
      Frame label="CoAP" {
              Text item=coapsw1
      }
}
```

# LICENCE
MIT
