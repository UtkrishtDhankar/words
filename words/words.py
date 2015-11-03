#!/usr/bin/python
import os

_ROOT = os.path.abspath(os.path.dirname(__file__))
def get_data(path):
    return os.path.join(_ROOT, 'data', path)

def main():
  data_file = open(get_data('english.txt'), 'r')
  print data_file
  for line in data_file:
    print line,

if __name__ == '__main__':
  main()
