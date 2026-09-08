from graphics_lib import *
BG="#FAF9F5"; INK="#3D3929"
class KernTest(Scene):
    def construct(self):
        self.camera.background_color = BG
        rows=[]
        for s in (24,26,28,30,32,34,36):
            rows.append(VGroup(
                label(str(s), size=24, color="#A9A491"),
                serif("their own recommendations grew", size=s, color=INK),
            ).arrange(RIGHT, buff=0.5))
        g = VGroup(*rows).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        g.scale_to_fit_height(6.8).move_to(ORIGIN)
        self.add(g)
