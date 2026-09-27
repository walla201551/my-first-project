ip = input("Enter an Ip address: ")
prits = ip.split(".")
if len(parts) ==4:
  valid = True
  for part in parts:
    if not part.isdigit() or not 0 <= int(part) <= 255:
      valid = False
      if valid:
        print("Valid IP address")
      else:
        print("Invalid IP address")
      else:
      print("Invalid IP address")
    
      
