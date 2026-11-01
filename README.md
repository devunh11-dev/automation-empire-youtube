# Automation Empire — YouTube Production Engine

A practical, approval-gated content system for Devun H / Automation Empire. It is designed around the creator's own on-camera footage and authentic recorded voice, with fast 27-second Shorts as the repeatable format.

## Brand direction
- Topic: practical AI automation, creator independence, and building a digital business in public.
- Presenter: the creator's own face and real recorded voice. No synthetic presenter or voice cloning.
- Visuals: premium blue-and-gold technology look; bold, readable captions; clean mobile-first framing.
- Format: hook → show the problem → demonstrate one useful action → clear CTA.
- Originality: learn from public creator formats without copying scripts, branding, footage, or protected assets.

## Current status
- YouTube and GitHub integrations were reported active by Composio.
- The connected YouTube API read test currently fails: channel statistics returned `quotaExceeded`; listing uploads returned 403. No upload or channel modification was attempted.
- No source video file was available to this repository workflow. The system prepares scripts and production assets; it cannot honestly claim to render or publish a video until the creator's actual footage is supplied and the YouTube API works.
- Publishing is intentionally manual/approval-gated. No public upload is performed by this project.

## Quick start
1. Record the script in `content/episode-001.md` on camera, using your own voice.
2. Follow `docs/recording-and-editing.md` for framing, audio, captions and pacing.
3. Use `tools/validate_content.py` to check the script and metadata.
4. Export a vertical 1080×1920 MP4 and keep the original recording.
5. Review the final video, title, description and thumbnail before upload.
6. Publish only after explicit approval and a successful account/API check.

## Project map
- `docs/strategy.md` — channel pillars and repeatable production loop.
- `docs/recording-and-editing.md` — authentic face-and-voice production guide.
- `content/episode-001.md` — first 27-second script and metadata pack.
- `content/shorts-template.md` — reusable script template.
- `prompts/production-prompts.md` — reusable ChatGPT prompts.
- `workflow/content-pipeline.yml` — pipeline stages and approval gates.
- `tools/validate_content.py` — local script/metadata validation.

## Safety and publishing
Do not commit raw footage, private analytics exports, account tokens, OAuth credentials, or personal contact details. Store secrets in a secure provider secret store, never in Git. Never upload automatically from a draft pipeline. See `docs/strategy.md` for the approval gate.