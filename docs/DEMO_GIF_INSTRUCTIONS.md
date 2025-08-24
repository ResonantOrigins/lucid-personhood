# Demo GIF workflow

1. Screen record a 10–15s run showing console output from `python demo/run_demo_openai.py`.
2. Convert to GIF with ffmpeg:

```bash
ffmpeg -i demo.mp4 -vf "fps=12,scale=640:-1:flags=lanczos" -loop 0 -f gif docs/demo.gif
```

3. Commit and push the new `docs/demo.gif`.