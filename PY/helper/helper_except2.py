try:
    print ('Press Ctrl+C or Interrupt the Kernel:')
    inp = input()
except KeyboardInterrupt:
    print ('Caught KeyboardInterrupt')
else:
    print ('No exception occurred')
    print ('You entered ', inp, ' key')
finally:
    print('Finally free')