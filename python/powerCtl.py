#!/usr/bin/python3
import sys
import telnetlib
import time

pdu=dict()
pdu["host"]="192.168.0.50"
pdu["uPrompt"]=b'User Name : '
pdu["user"]=b'laser'
pdu["pPrompt"]=b'Password  : '
pdu["pw"]=b'laser -c'
pdu["prompt"]=b'APC> '
pdu["fan"]=1
pdu["pi"]=23
pdu["cutter"]=24
pdu["expects"]=[pdu["uPrompt"], pdu["pPrompt"], b'APC>']
validUnits = ["fan", "pi", "cutter"]
onOff = ["on", "off"]
action = "on"
units = []
args=sys.argv
def usage():
    print("powercontrol [on off] [fan pi cutter]")
    exit()
if (len(args) <1) :
    usage()
for arg in args[1:]:
    if arg in onOff :
        action = arg
    elif arg in validUnits :
        units.append(pdu[arg])
    else :
        print("Unknown argument %s" %arg)
        usage()
print("action = %s" % action)
unitStr = ' '.join(str(u) for u in units)
print("units %s" % unitStr)
cmdStr = (action + " " + unitStr).encode('ASCII')
print("command %s" % cmdStr)

tn=telnetlib.Telnet(pdu["host"])
#tn.set_debuglevel(3)
#print(tn.read_all().decode('ascii'))
#print(tn.read_until(pdu["uPrompt"],1))
#time.sleep(2);
(ndx,exp,bts) = tn.expect(pdu["expects"],2)
print("got %s, %s, %s" %(ndx,exp,bts))
tn.write(pdu["user"] + b'\r')
#print(tn.read_until(pdu["pPrompt"],1))
#time.sleep(2);
(ndx,exp,bts) = tn.expect(pdu["expects"],2)
print("got %s, %s, %s" %(ndx,exp,bts))
tn.write(pdu["pw"] + b'\r')
#print(tn.read_until(pdu["prompt"],1))
#time.sleep(2);
(ndx,exp,bts) = tn.expect(pdu["expects"],2)
print("got %s, %s, %s" %(ndx,exp,bts))
tn.write(cmdStr + b'\r')
#print(tn.read_until(pdu["pPrompt"],1))
#time.sleep(2);
(ndx,exp,bts) = tn.expect(pdu["expects"],2)
print("got %s, %s, %s" %(ndx,exp,bts))
tn.write(b'exit\r')
print(tn.read_all().decode('ascii'))
tn.close()


