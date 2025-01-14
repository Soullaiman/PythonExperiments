### ENABLE LOGGING MONITOR
from netmiko import ConnectHandler
IP_ADDRESS = "192.168.56.101" #"Get IP Address"
sshCli = ConnectHandler(
    device_type="cisco_ios",
    host="devnetsandboxiosxe.cisco.com",
    port="22",
    username="admin",
    password="C1sco12345"
    )
config_commands = (
    'no interface loopback 10' ,
    )
output=sshCli.send_command("show ip interface brief")
print(output)
output=sshCli.send_config_set(config_commands)
print(output)
output=sshCli.send_command("show ip interface brief")
print(output)
