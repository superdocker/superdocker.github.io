# superdocker.github.io

Personal academic homepage of Janghwan Lee — <https://superdocker.github.io>

Built with [Astro](https://astro.build) and [Tailwind CSS](https://tailwindcss.com).

## Development

```bash
npm install
npm run dev      # local dev server
npm run build    # static build into dist/
npm run preview  # preview the production build
```

## Structure

- `src/pages/` — pages (`index`, `publications`, `cv`)
- `src/components/`, `src/layouts/` — shared UI
- `src/data/publications.json` — publication list
- `public/` — static files served from the site root
  - `public/pdf/cv_janghwan.pdf` → `/pdf/cv_janghwan.pdf` (replace this file to update the CV)
  - `public/img/profile.jpeg` → `/img/profile.jpeg`

## Deployment

Pushing to `master` triggers `.github/workflows/deploy.yml`, which builds the site and publishes `dist/` to the `gh-pages` branch.
