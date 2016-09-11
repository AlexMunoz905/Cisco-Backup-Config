# Starter script to log in to IOS devices and pull basic info.
# File is saved with hostname of the device.

# Requires netmiko library to be installed

# import the modules you want to call        
import netmiko, getpass

# grab some info from the user
ip = raw_input('Device IP: ')
un = raw_input('Username: ')
pw = getpass.getpass()

# define your device
cisco_nxos = {
    'device_type': 'cisco_nxos',
    'ip': ip,
    'username': un,
    'password': pw,
}

# connect to the device w/ netmiko
net_connect = netmiko.ConnectHandler(**cisco_nxos)

# get the prompt as a string
prompt = net_connect.find_prompt()

hostname = net_connect.send_command('show run | i host')
hostname.split(" ")
col1,col2 = hostname.split(" ")
print "Working on " + col2
filename = col2 + '.txt'

showrun = net_connect.send_command('show run')
showver = net_connect.send_command('show ver')
log_file = open(filename, "a")   # in append mode
log_file.write(showrun)
log_file.write("\n")
log_file.write(showver)
log_file.write("\n")