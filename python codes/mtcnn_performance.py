from __future__ import print_function

def run():
    p = 0
    with open("rect_py.txt", "r") as f1, open("rect.txt", "r") as f2, open("outfile.txt", "w") as outfile:
        for line1, line2 in zip(f1, f2):
            x11 = float(line1.split()[0])
            y11 = float(line1.split()[1])
            x12 = float(line1.split()[2])
            y12 = float(line1.split()[3])
            x21 = float(line2.split()[0])
            y21 = float(line2.split()[1])
            x22 = float(line2.split()[2])
            y22 = float(line2.split()[3])
            overlap = max(0, min(x12, x22)-max(x11, x21)) * max(0, min(y12, y22)-max(y11, y21))     
            s1 = abs((x11-x12)*(y11-y12))
            s2 = abs((x21-x22)*(y21-y22))
            percent = overlap/(s1+s2-overlap)
            p += percent
            outfile.write(str(percent)+"\n")
    print(p/100)

run()
