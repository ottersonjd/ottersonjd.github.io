# Justin Otterson — Business Analytics & Strategy Portfolio

A standalone portfolio for GitHub Pages. Visitors need no account or browser extension. The site uses HTML, CSS and JavaScript; its build script uses Python's standard library. All assets are relative, so it works at either `USERNAME.github.io` or `USERNAME.github.io/portfolio/`.

## Publish on GitHub Pages

1. Create a public repository named `USERNAME.github.io` for a root portfolio address, or `portfolio` for a project address. GitHub Free supports Pages for public repositories.
2. Upload the contents of this folder to the repository's `main` branch, including `.github/workflows/pages.yml` and `scripts/`.
3. In the repository's **Settings → Pages → Build and deployment**, select **GitHub Actions**.
4. In **Actions → Publish portfolio**, run the workflow if it has not already started. The successful deployment reports the live URL.

No credentials, ChatGPT hosting configuration, login code or private data are required. The original ChatGPT-hosted portfolio is separate and remains available until its owner decides to retire it.

## Add or update a project

Edit `projects.json` in GitHub's web editor and commit to `main`. Copy an existing project object and give it a unique `id`. Keep academic consulting and independent externship labels accurate, and distinguish modeled outcomes from realized results. The workflow builds and republishes the site after a commit.

### Add a Google Colab notebook

- For a link: set a project's `colab` field to its HTTPS Colab URL, and configure viewer access in Google Drive.
- For a download: in Colab choose **File → Download → Download .ipynb**. In the repository, open `notebooks/`, then choose **Add file → Upload files** and commit the notebook. Set that project's `notebookPath` to `./notebooks/Your_Notebook.ipynb` in `projects.json`.
- You can supply both. Notebook filenames should use letters, digits, periods, underscores and hyphens.

Uploads now happen through your GitHub account. Public visitors cannot change the portfolio. There is no server-backed upload editor on this static site.

The two included notebooks are cleaned methodology artifacts. Their source datasets are not included, and original-data results have not been reproduced. Existing limitations and AI-assisted refactoring disclosures inside the notebooks are preserved.

## Preview locally

```sh
python3 scripts/build.py
python3 -m http.server 8000 --directory _site
```

Open `http://localhost:8000`. Stop the server with Ctrl+C. The site itself also renders directly from `index.html`; case studies remain accessible without JavaScript.
