narx=100_000
yosh=int(input("Yosh kiriting:"))
if 1 <= yosh < 7:
    print("Yakuniy narx:", narx*0.5)
if 7<= yosh < 17:
    print("Yakuniy narx:", narx*0.8)
if yosh > 60:
    print("Yakuniy narx:", narx*0.7)