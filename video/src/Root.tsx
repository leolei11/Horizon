import React from "react";
import {Composition} from "remotion";
import {HorizonDaily, VideoManifest} from "./HorizonDaily";

const defaultProps: VideoManifest = {
  title: "HORIZON / DAILY SIGNAL",
  date: "2026-08-10",
  language: "zh",
  width: 1920,
  height: 1080,
  fps: 30,
  introFrames: 45,
  outroFrames: 36,
  totalFrames: 300,
  stories: [],
};

export const Root: React.FC = () => (
  <Composition
    id="HorizonDaily"
    component={HorizonDaily}
    durationInFrames={defaultProps.totalFrames}
    fps={defaultProps.fps}
    width={defaultProps.width}
    height={defaultProps.height}
    defaultProps={defaultProps}
  />
);
