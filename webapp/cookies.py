from http import cookies
C = cookies.SimpleCookie()
C["fig"] = "newton"
print(C)
print(C.output(header="Cookie:"))