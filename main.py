'''
Steal all the passwds!
'''

if __name__ == "__main__":
  print open('/etc/passwd').read()
