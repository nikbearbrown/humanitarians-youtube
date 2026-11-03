# B13: 1000x500, paddle 50, no speed-up at the serve: quarter-speed paddle defends, a fifth does not (full aim).
src=open('angle_check2.py').read().split('for vp in [1.0')[0].replace("W,H,h=858.0,525.0,60.0","W,H,h=1000.0,500.0,50.0").replace("vx0,g=6.0,0.05","vx0,g=6.0,0.0")
ns={};exec(src,ns)
for ratio in (0.25,0.2):
    vp=ratio*6.0
    print(f"paddle = {ratio} x ball speed: first break {ns['first_break'](vp,1.0)}")
