# Articles

This directory contains static HTML articles that will be copied to the built site and listed on the index page.

## Creating a New Article

1. **Create a new HTML file** in this directory (e.g., `my-article.html`)
2. **Use the example template** (`example-article.html`) as a starting point
3. **Edit the content** - you can use HTML directly or write in Markdown and convert to HTML
4. **Link back to home** - include `<a href="../index.html">← Back to Home</a>` for navigation
5. **Build and test** - run `uv run .github/scripts/build.py` and serve locally with `python -m http.server -d _site`

## File Naming

- Use lowercase letters and hyphens (e.g., `my-article-title.html`)
- The filename (without extension) will be used to generate the display name on the index page
- Underscores and hyphens are converted to spaces, and each word is capitalized
  - Example: `example-article.html` → "Example Article"

## Adding Images

To include images in your articles:
1. Create a `public/` directory in the root if it doesn't exist
2. Place your images in `public/`
3. Reference them in your article: `<img src="../public/your-image.png" />`

## Styling

The example template uses Tailwind CSS via CDN for easy styling. You can:
- Use the same approach for consistency
- Create your own custom CSS
- Use a different CSS framework

## Build Process

When you run the build script:
1. All `.html` files in this directory are found
2. Each file is copied to `_site/articles/` maintaining the directory structure
3. Articles are automatically added to the index page in the "Articles" section

## Local Development

To preview your articles locally:
```bash
# Build the site
uv run .github/scripts/build.py

# Serve locally at http://localhost:8000
python -m http.server -d _site

# Open http://localhost:8000 in your browser
# Click on your article from the "Articles" section
```
