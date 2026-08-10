import React from "react";
import {
  AbsoluteFill,
  Audio,
  Easing,
  Sequence,
  interpolate,
  spring,
  staticFile,
  useCurrentFrame,
  useVideoConfig,
} from "remotion";

export type VideoStory = {
  id: string;
  index: number;
  title: string;
  captions: string[];
  action: string;
  actionLabel: string;
  source: string;
  url: string;
  bucket: string;
  videoScore: number;
  relevanceScore: number;
  audioSrc: string | null;
  startFrame: number;
  durationFrames: number;
};

export type VideoManifest = {
  title: string;
  date: string;
  language: string;
  width: number;
  height: number;
  fps: number;
  introFrames: number;
  outroFrames: number;
  totalFrames: number;
  stories: VideoStory[];
};

const C = {
  ink: "#071018",
  panel: "#0D1A25",
  panelRaised: "#132432",
  paper: "#F4F7FB",
  muted: "#8FA3B5",
  line: "#294052",
  cobalt: "#5B8CFF",
  cyan: "#56D6C9",
  amber: "#FFBE5C",
};

const clamp = {
  extrapolateLeft: "clamp" as const,
  extrapolateRight: "clamp" as const,
};

const Grid: React.FC = () => {
  const frame = useCurrentFrame();
  const x = (frame * 0.45) % 80;
  return (
    <AbsoluteFill
      style={{
        backgroundColor: C.ink,
        backgroundImage:
          "linear-gradient(rgba(143,163,181,.055) 1px, transparent 1px), linear-gradient(90deg, rgba(143,163,181,.055) 1px, transparent 1px)",
        backgroundSize: "80px 80px",
        backgroundPosition: x + "px 0",
      }}
    />
  );
};

const UtilityHeader: React.FC<{date: string}> = ({date}) => (
  <div
    style={{
      position: "absolute",
      left: 86,
      right: 86,
      top: 58,
      height: 56,
      display: "flex",
      alignItems: "center",
      justifyContent: "space-between",
      borderBottom: "1px solid " + C.line,
      fontFamily: "SFMono-Regular, Menlo, monospace",
      fontSize: 19,
      letterSpacing: "0.14em",
      color: C.muted,
    }}
  >
    <div>
      <span style={{color: C.paper, fontWeight: 700}}>HORIZON</span>
      <span style={{marginLeft: 20}}>DAILY SIGNAL</span>
    </div>
    <div>{date} · 16:9 EDITION</div>
  </div>
);

const SignalLine: React.FC<{
  count: number;
  active: number;
  progress: number;
}> = ({count, active, progress}) => {
  const safeCount = Math.max(count, 1);
  return (
    <div
      style={{
        position: "absolute",
        left: 86,
        right: 86,
        bottom: 58,
        height: 72,
      }}
    >
      <div
        style={{
          position: "absolute",
          left: 0,
          right: 0,
          top: 26,
          height: 2,
          background: C.line,
        }}
      />
      <div
        style={{
          position: "absolute",
          left: 0,
          top: 25,
          height: 4,
          width: Math.round(progress * 100) + "%",
          background: C.cyan,
        }}
      />
      {Array.from({length: safeCount}).map((_, index) => {
        const selected = index === active;
        return (
          <div
            key={index}
            style={{
              position: "absolute",
              left: safeCount === 1 ? "50%" : index * (100 / (safeCount - 1)) + "%",
              top: selected ? 16 : 21,
              width: selected ? 22 : 12,
              height: selected ? 22 : 12,
              transform: "translateX(-50%) rotate(45deg)",
              background: selected ? C.amber : C.panelRaised,
              border: "2px solid " + (selected ? C.amber : C.muted),
            }}
          />
        );
      })}
    </div>
  );
};

const Intro: React.FC<VideoManifest> = ({stories, date, introFrames}) => {
  const frame = useCurrentFrame();
  const {fps} = useVideoConfig();
  const enter = spring({frame, fps, config: {damping: 18, stiffness: 120}});
  const line = interpolate(frame, [5, introFrames - 5], [0, 1], {
    ...clamp,
    easing: Easing.out(Easing.cubic),
  });
  return (
    <AbsoluteFill>
      <Grid />
      <UtilityHeader date={date} />
      <div
        style={{
          position: "absolute",
          left: 170,
          top: 258,
          color: C.paper,
          transform: "translateY(" + (1 - enter) * 34 + "px)",
          opacity: enter,
        }}
      >
        <div
          style={{
            fontFamily: "SFMono-Regular, Menlo, monospace",
            fontSize: 24,
            letterSpacing: "0.18em",
            color: C.cyan,
            marginBottom: 34,
          }}
        >
          {stories.length} SIGNALS / ONE DECISION WINDOW
        </div>
        <div
          style={{
            maxWidth: 1340,
            fontFamily:
              '"Hiragino Sans GB", "PingFang SC", "Noto Sans CJK SC", sans-serif',
            fontSize: 88,
            fontWeight: 800,
            lineHeight: 1.12,
            letterSpacing: "-0.045em",
          }}
        >
          今天值得你动手的
          <br />
          AI 与开发信号
        </div>
      </div>
      <SignalLine count={stories.length} active={-1} progress={line} />
    </AbsoluteFill>
  );
};

const StoryScene: React.FC<{
  manifest: VideoManifest;
  story: VideoStory;
  localFrame: number;
}> = ({manifest, story, localFrame}) => {
  const {fps} = useVideoConfig();
  const enter = spring({
    frame: localFrame,
    fps,
    config: {damping: 20, stiffness: 145, mass: 0.9},
  });
  const exit = interpolate(
    localFrame,
    [story.durationFrames - 16, story.durationFrames],
    [1, 0],
    clamp,
  );
  const progress = interpolate(
    localFrame,
    [0, story.durationFrames],
    [story.index - 1, story.index],
    clamp,
  ) / Math.max(manifest.stories.length, 1);
  const captionIndex = Math.min(
    story.captions.length - 1,
    Math.floor(
      (localFrame / Math.max(story.durationFrames - 1, 1)) *
        story.captions.length,
    ),
  );
  const scoreWidth = Math.round((story.relevanceScore / 10) * 100);
  const titleSize = story.title.length > 34 ? 54 : story.title.length > 22 ? 64 : 74;

  return (
    <AbsoluteFill style={{opacity: exit}}>
      <Grid />
      <UtilityHeader date={manifest.date} />
      <div
        style={{
          position: "absolute",
          left: 86,
          top: 150,
          width: 290,
          bottom: 160,
          padding: "32px 34px",
          background: C.panel,
          borderTop: "6px solid " + C.cobalt,
          display: "flex",
          flexDirection: "column",
          justifyContent: "space-between",
          transform: "translateX(" + (1 - enter) * -36 + "px)",
          opacity: enter,
        }}
      >
        <div>
          <div
            style={{
              fontFamily: "SFMono-Regular, Menlo, monospace",
              fontSize: 82,
              fontWeight: 700,
              letterSpacing: "-0.08em",
              color: C.paper,
            }}
          >
            {String(story.index).padStart(2, "0")}
          </div>
          <div
            style={{
              marginTop: 18,
              color: C.cyan,
              fontFamily: "SFMono-Regular, Menlo, monospace",
              fontSize: 17,
              lineHeight: 1.5,
              letterSpacing: "0.12em",
            }}
          >
            {story.bucket.toUpperCase()}
          </div>
        </div>
        <div>
          <div
            style={{
              color: C.muted,
              fontFamily: "SFMono-Regular, Menlo, monospace",
              fontSize: 15,
              letterSpacing: "0.1em",
              marginBottom: 12,
            }}
          >
            PERSONAL FIT {story.relevanceScore.toFixed(1)}
          </div>
          <div style={{height: 8, background: C.line}}>
            <div
              style={{
                height: "100%",
                width: scoreWidth + "%",
                background: C.cyan,
              }}
            />
          </div>
          <div
            style={{
              marginTop: 26,
              color: C.muted,
              fontFamily: "SFMono-Regular, Menlo, monospace",
              fontSize: 17,
              overflow: "hidden",
              textOverflow: "ellipsis",
              whiteSpace: "nowrap",
            }}
          >
            {story.source}
          </div>
        </div>
      </div>

      <div
        style={{
          position: "absolute",
          left: 430,
          right: 120,
          top: 180,
          bottom: 180,
          display: "flex",
          flexDirection: "column",
          justifyContent: "center",
          transform: "translateY(" + (1 - enter) * 26 + "px)",
          opacity: enter,
        }}
      >
        <div
          style={{
            color: C.amber,
            fontFamily: "SFMono-Regular, Menlo, monospace",
            fontSize: 18,
            letterSpacing: "0.16em",
            marginBottom: 22,
          }}
        >
          VIDEO VALUE {story.videoScore.toFixed(1)} / 10
        </div>
        <div
          style={{
            maxWidth: 1240,
            color: C.paper,
            fontFamily:
              '"Hiragino Sans GB", "PingFang SC", "Noto Sans CJK SC", sans-serif',
            fontWeight: 800,
            fontSize: titleSize,
            lineHeight: 1.18,
            letterSpacing: "-0.035em",
          }}
        >
          {story.title}
        </div>
        <div
          style={{
            marginTop: 40,
            maxWidth: 1160,
            minHeight: 126,
            color: C.paper,
            fontFamily:
              '"Hiragino Sans GB", "PingFang SC", "Noto Sans CJK SC", sans-serif',
            fontSize: 32,
            fontWeight: 500,
            lineHeight: 1.55,
            borderLeft: "5px solid " + C.cyan,
            paddingLeft: 30,
          }}
        >
          {story.captions[captionIndex]}
        </div>
        {story.action ? (
          <div
            style={{
              marginTop: 34,
              maxWidth: 1120,
              display: "flex",
              alignItems: "flex-start",
              gap: 18,
              padding: "18px 22px",
              color: C.paper,
              background: C.panelRaised,
              border: "1px solid " + C.line,
              fontFamily:
                '"Hiragino Sans GB", "PingFang SC", "Noto Sans CJK SC", sans-serif',
              fontSize: 22,
              lineHeight: 1.45,
            }}
          >
            <span
              style={{
                color: C.amber,
                fontFamily: "SFMono-Regular, Menlo, monospace",
                fontSize: 15,
                letterSpacing: "0.12em",
                whiteSpace: "nowrap",
                marginTop: 6,
              }}
            >
              {story.actionLabel}
            </span>
            <span>{story.action}</span>
          </div>
        ) : null}
      </div>
      <SignalLine
        count={manifest.stories.length}
        active={story.index - 1}
        progress={progress}
      />
    </AbsoluteFill>
  );
};

const Outro: React.FC<VideoManifest> = ({stories, date}) => {
  const frame = useCurrentFrame();
  const {fps} = useVideoConfig();
  const enter = spring({frame, fps, config: {damping: 18, stiffness: 120}});
  return (
    <AbsoluteFill>
      <Grid />
      <UtilityHeader date={date} />
      <div
        style={{
          position: "absolute",
          left: 170,
          right: 170,
          top: 280,
          color: C.paper,
          opacity: enter,
          transform: "translateY(" + (1 - enter) * 25 + "px)",
        }}
      >
        <div
          style={{
            fontFamily: "SFMono-Regular, Menlo, monospace",
            fontSize: 22,
            letterSpacing: "0.16em",
            color: C.cyan,
            marginBottom: 30,
          }}
        >
          SIGNALS COMPLETE
        </div>
        <div
          style={{
            fontFamily:
              '"Hiragino Sans GB", "PingFang SC", "Noto Sans CJK SC", sans-serif',
            fontSize: 76,
            lineHeight: 1.18,
            fontWeight: 800,
            letterSpacing: "-0.04em",
          }}
        >
          不收藏一堆新闻。
          <br />
          只留下一个下一步。
        </div>
        <div
          style={{
            marginTop: 34,
            color: C.muted,
            fontFamily:
              '"Hiragino Sans GB", "PingFang SC", "Noto Sans CJK SC", sans-serif',
            fontSize: 25,
          }}
        >
          完整日报包含 {stories.length} 条视频精选及更多文字信号
        </div>
      </div>
      <SignalLine count={stories.length} active={stories.length - 1} progress={1} />
    </AbsoluteFill>
  );
};

export const HorizonDaily: React.FC<VideoManifest> = (manifest) => {
  const frame = useCurrentFrame();
  const outroStart = manifest.totalFrames - manifest.outroFrames;
  const activeStory = manifest.stories.find(
    (story) =>
      frame >= story.startFrame &&
      frame < story.startFrame + story.durationFrames,
  );

  return (
    <AbsoluteFill style={{backgroundColor: C.ink}}>
      {frame < manifest.introFrames ? <Intro {...manifest} /> : null}
      {activeStory ? (
        <StoryScene
          manifest={manifest}
          story={activeStory}
          localFrame={frame - activeStory.startFrame}
        />
      ) : null}
      {frame >= outroStart ? (
        <Sequence from={outroStart} layout="none">
          <Outro {...manifest} />
        </Sequence>
      ) : null}
      {manifest.stories.map((story) =>
        story.audioSrc ? (
          <Sequence
            key={story.id}
            from={story.startFrame}
            durationInFrames={story.durationFrames}
          >
            <Audio src={staticFile(story.audioSrc)} />
          </Sequence>
        ) : null,
      )}
    </AbsoluteFill>
  );
};
