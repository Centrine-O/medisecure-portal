# MediSecure Frontend

This frontend now has two UI modes:

## 1) Public landing page
Default route:
- `/`

## 2) Internal roadmap page (for interviews/demo storytelling)
Hidden from public navigation, accessible only by direct URL:
- `/?view=roadmap`
- `/roadmap`

This roadmap page contains:
- Product purpose (end-to-end)
- Kenya market disconnects to solve
- Universal architecture approach
- Roadmap (MVP -> county rollout -> national scale)
- Success metrics

## Run locally

```bash
cd frontend
npm install
npm run dev
```

## Build

```bash
npm run build
npm run preview
```
