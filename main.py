import sys

def main_add():
  print('main_add')

def main_change():
  print('main_change')

def main_done():
  print('main_done')

def main_next():
  print('main_next')

n_args = len(sys.argv)

if n_args > 1:
  # $TODO handle error
  arg = sys.argv[1]
  if arg == 'add':
    main_add()
  elif arg == 'change':
    main_change()
  elif arg == 'done':
    main_done()
  elif arg == 'next':
    main_next()
  else:
    print('unknown argument')
else:
  print('usage')
