# try:
#     pass
# except:
#     pass
# finally:
#     pass

data={'A':1,'B':2}
try:
    print(data['A'])
except KeyError:
    print('Key Error')
except ZeroDivisionError:
    print('Zero Division Error')
finally:
    print('Finally called')

