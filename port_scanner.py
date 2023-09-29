import socket
import re

import common_ports


def probePort(host, port):
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  s.settimeout(0.1)
  #print(host, port)
  if s.connect_ex((host, port)):
    #print(port, ": The port is closed")
    s.close()
    return None
  else:
    s.close()
    return port


def get_open_ports(*args):

  host = args[0]

  ipMatch = re.search(
      "^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$",
      host)

  wrongIpMatch = re.search("^[\.0-9]*$", host)

  urlMatch = re.search(
      "(https:\/\/www\.|http:\/\/www\.|https:\/\/|http:\/\/)?[a-zA-Z0-9]{2,}\.[a-zA-Z0-9]{2,}\.[a-zA-Z0-9]{2,}(\.[a-zA-Z0-9]{2,})?",
      host)

  if (ipMatch is not None or urlMatch is not None):
    pass
  elif (wrongIpMatch is not None):
    #print("Wrong IP detected")
    return "Error: Invalid IP address"
  else:
    #print("Wrong URL detected")
    return "Error: Invalid hostname"


#  print host

###################################
#print(host)

  output = []

  i = args[1][0]
  while i < args[1][1]:
    i += 1
    j = probePort(host, i)
    if j is not None:
      output.append(j)

  #print(output)

  verboseOutput = []
  verboseOutput.append("Open ports for " + host)
  verboseOutput.append("PORT    SERVICE")
  for element in output:
    verboseOutput.append(
        str(element) + "    " + common_ports.Теports_and_services[element])

  #print(verboseOutput)

  outputString = "\n".join([str(o) for o in verboseOutput])

  if (len(args) > 2):
    if (args[2] is True):
      #verbose mode enabled
      return outputString
    else:
      return output
  else:
    return output
