"""testing wexpect"""

import wexpect

child = wexpect.spawn("cmd")
child.expect(">")
child.sendline("ls")
child.expect(">")
print(child.before)
child.sendline("exit")
child.close()

# https://stackoverflow.com/questions/13891571/how-to-match-a-regular-expression-like-i1-in-python-pexpect

child = wexpect.spawn("C:/maxima-5.45.1/bin/maxima.bat")
child.expect("(%i1)")
child.sendline("print(1+1);")
child.expect("(%o1)")
print(child.before)
child.close()

child = wexpect.spawn("C:/maxima-5.45.1/bin/maxima.bat")
child.expect("(%i1)")
child.sendline("print(matrix([1,2,3],[4,5,6]));")
child.expect("(%o1)")
print(child.before)
child.close()

"""
print("takowosz")
child = wexpect.spawn('C:/maxima-5.45.1/bin/maxima.bat')
child.expect('')
print(child)
child.close()

print("takowosz")
child = wexpect.spawn('D:/moje/studia/semestr_2/testy/beznazwy.wxmx')
file_contents = child.read()

# Print the file contents
print(file_contents)

child.close()
"""
