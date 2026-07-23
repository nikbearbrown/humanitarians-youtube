import { Composition } from "remotion";
import { Lecture, totalFrames } from "./Lecture";
import beats from "./data/beats.json";

const fps: number = beats.metadata.fps ?? 30;

export const RemotionRoot: React.FC = () => {
  return (
    <Composition
      id="Lecture"
      component={Lecture}
      durationInFrames={Math.max(1, totalFrames())}
      fps={fps}
      width={1920}
      height={1080}
    />
  );
};
