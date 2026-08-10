"""Render a previously prepared Horizon video manifest."""

import argparse
import asyncio
from pathlib import Path

from rich.console import Console

from ..models import VideoConfig
from .pipeline import HorizonVideoPipeline


console = Console(stderr=True)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Render a Horizon landscape-video manifest"
    )
    parser.add_argument("manifest", type=Path)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--renderer-dir", default="video")
    parser.add_argument("--output-dir", default="data/videos")
    args = parser.parse_args()

    pipeline = HorizonVideoPipeline(
        VideoConfig(
            enabled=True,
            auto_render=True,
            renderer_dir=args.renderer_dir,
            output_dir=args.output_dir,
        )
    )
    output = asyncio.run(
        pipeline.render_manifest(args.manifest, output_path=args.output)
    )
    console.print(f"[green]Rendered video:[/green] {output}")


if __name__ == "__main__":
    main()
