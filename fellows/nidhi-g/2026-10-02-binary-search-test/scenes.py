from manim import *

INK = "#3D3929"
ACCENT = "#D97757"
BG = "#F2F0E9"


class B01_BinarySearch(Scene):
    def construct(self):
        self.camera.background_color = BG
        nums = [2, 5, 8, 12, 16, 23, 38, 45, 56, 72, 91]
        target = 72

        boxes = VGroup(*[Square(0.9, color=INK, stroke_width=3) for _ in nums])
        boxes.arrange(RIGHT, buff=0.12)
        labels = VGroup(*[Text(str(n), color=INK, font_size=28).move_to(b)
                          for n, b in zip(nums, boxes)])
        title = Text(f"Find {target}", color=INK, font_size=40).to_edge(UP, buff=1.0)
        counter = Text("looks: 0", color=INK, font_size=30).to_edge(DOWN, buff=1.0)

        self.play(FadeIn(title), Create(boxes), FadeIn(labels), FadeIn(counter))

        lo, hi, looks = 0, len(nums) - 1, 0
        while lo <= hi:
            mid = (lo + hi) // 2
            looks += 1
            new_counter = Text(f"looks: {looks}", color=INK, font_size=30).move_to(counter)
            self.play(boxes[mid].animate.set_fill(ACCENT, opacity=0.7),
                      Transform(counter, new_counter), run_time=0.8)
            self.wait(0.6)
            if nums[mid] == target:
                break
            gone = range(lo, mid + 1) if nums[mid] < target else range(mid, hi + 1)
            self.play(*[VGroup(boxes[i], labels[i]).animate.set_opacity(0.4) for i in gone],
                      run_time=0.8)
            if nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid - 1

        self.play(Indicate(VGroup(boxes[mid], labels[mid]), color=ACCENT), run_time=1.0)
        self.wait(1.5)