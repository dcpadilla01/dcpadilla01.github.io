# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a marimo WebAssembly + GitHub Pages template repository that exports marimo notebooks to static HTML/WebAssembly and deploys them automatically to GitHub Pages. Marimo notebooks are interactive Python notebooks that can be exported as standalone web applications.

## Key Commands

### Building the Site

```bash
# Export all notebooks to _site/ directory (default template: tailwind.html.j2)
uv run .github/scripts/build.py

# Export with custom template
uv run .github/scripts/build.py --template templates/index.html.j2

# Export with custom output directory
uv run .github/scripts/build.py --output-dir dist
```

### Local Development

```bash
# Build the site
uv run .github/scripts/build.py

# Serve the built site locally at http://localhost:8000
python -m http.server -d _site
```

### Devbox (if installed)

```bash
# Build using devbox script
devbox run build

# Serve using devbox script
devbox run serve
```

## Architecture

### Directory Structure

- `notebooks/`: Contains marimo notebooks exported in **edit mode** (interactive editing interface)
- `apps/`: Contains marimo notebooks exported in **run mode** (read-only apps with hidden code)
- `articles/`: Static HTML articles (blog posts, traditional content) copied directly to output
- `public/`: Static assets (images, CSV files, etc.) accessible to notebooks via `mo.notebook_location() / "public" / "filename"`
- `templates/`: Jinja2 templates for the generated index.html page
- `.github/scripts/build.py`: Main build script that exports notebooks to HTML/WebAssembly
- `_site/`: Generated output directory (created by build script, not committed to git)

### Build Process Flow

1. **Build script** (`.github/scripts/build.py`) finds all `.py` files in `notebooks/` and `apps/`, plus all `.html` files in `articles/`
2. **Export process**:
   - Notebooks (`notebooks/*.py`) → exported with `--mode edit` (editable interface)
   - Apps (`apps/*.py`) → exported with `--mode run --no-show-code` (read-only, code hidden)
   - Articles (`articles/*.html`) → copied directly to output (static HTML pages)
   - Uses `uvx marimo export html-wasm --sandbox` for WebAssembly export
3. **Index generation**: Creates `_site/index.html` using Jinja2 templates, listing all exported notebooks/apps/articles
4. **Deployment**: GitHub Actions workflow deploys `_site/` to GitHub Pages on push to main

### Marimo Notebook Structure

Marimo notebooks are Python files with special structure:
- Use `marimo.App()` to define the application
- Cells are decorated with `@app.cell`
- Dependencies between cells defined by `app.setup` block
- Inline script dependencies declared using PEP 723 (script metadata block at top)
- Access notebook location with `mo.notebook_location()` for relative file paths

### Template System

Two templates available in `templates/`:
1. `index.html.j2` - Styled template with footer and more detailed layout
2. `tailwind.html.j2` - Lean template using Tailwind CSS (current default)

Templates receive `notebooks`, `apps`, and `articles` variables with structure:
```python
[{"display_name": "Title", "html_path": "notebooks/file.html"}, ...]
```

All templates now support displaying articles alongside notebooks and apps.

## Notebooks vs Apps: When to Use Each

### Key Difference

**Notebooks** (`notebooks/` folder):
- Exported in **edit mode** with visible, editable code
- Like Jupyter notebooks - visitors can see, modify, and run code
- Purpose: Educational, teaching, code walkthroughs

**Apps** (`apps/` folder):
- Exported in **run mode** with hidden code
- Like web applications - visitors only see the interface
- Purpose: Tools, dashboards, calculators, polished demos

### Decision Guide

**Use Notebooks when:**
- Teaching/tutorials: "Here's how to analyze data with Polars"
- Demonstrating techniques: "This is how gradient descent works"
- Reproducible research: "Here's my analysis with all the code"
- Code walkthroughs: Step-by-step explanations
- You want visitors to learn from and modify your code

**Use Apps when:**
- Calculators/tools: "Calculate your investment returns"
- Interactive dashboards: "Explore this dataset visually"
- Demos/visualizations: "Play with this interactive chart"
- Utilities: Convert units, generate data, etc.
- You want a clean UI without code clutter

**Use Articles when:**
- Blog posts, essays, written content
- Traditional static pages without interactive Python code

### Quick Question to Ask Yourself

"Do I want visitors to see and learn from the code?"
- ✅ **YES** → Use `notebooks/` (code visible and editable)
- ❌ **NO** → Use `apps/` (code hidden, clean interface)

### Example Organization

```
notebooks/
  ├── monte-carlo-simulation.py        # Show the simulation logic
  ├── neural-network-from-scratch.py   # Teach how NNs work
  └── risk-metrics-explained.py        # Demonstrate calculations

apps/
  ├── risk-calculator.py               # Hidden code, just input/output
  ├── ml-model-playground.py           # Interactive parameter tuning
  └── portfolio-simulator.py           # Run simulations with sliders

articles/
  ├── my-blog-post.html               # Written article
  └── tutorial-introduction.html       # Static content
```

## Adding Content

### Adding a New Notebook

1. Create a `.py` file in `notebooks/` (for editable) or `apps/` (for read-only)
2. Use marimo format with `@app.cell` decorators
3. Declare dependencies in PEP 723 script metadata block
4. Push to main - GitHub Actions will auto-build and deploy

### Adding an Article (Static HTML Page)

1. Create an `.html` file in `articles/` directory
2. Use the example article template (`articles/example-article.html`) as a starting point
3. Include `<a href="../index.html">` links to navigate back to home
4. Push to main - build script will copy it to `_site/articles/` and add to index

### Adding Static Assets

1. Create `public/` directory if it doesn't exist
2. Add files (images, CSVs, etc.) to `public/`
3. Reference in notebooks:
   - Images: `<img src="public/logo.png" />`
   - Data: `pl.read_csv(mo.notebook_location() / "public" / "file.csv")`
4. Reference in articles: `<img src="../public/image.png" />`

## Customization Guide (For Non-Developers)

### What You Can Safely Customize

**Good news:** You can completely personalize the site WITHOUT breaking marimo functionality!

Here's why: The marimo notebooks/apps are standalone files generated by marimo. Your customization only affects the **index/landing page** and **article pages**. The interactive Python notebooks will always work.

### Understanding the Template Files

The template files use **Jinja2**, a template language that mixes HTML with special placeholder syntax:

#### Safe to Change (Regular HTML/CSS):
```html
<h1>My Website Title</h1>                    ← Regular HTML - change freely!
<p class="subtitle">My description</p>       ← Regular HTML - change freely!
<title>My Page Title</title>                 ← Regular HTML - change freely!
```

#### DO NOT CHANGE (Jinja2 Syntax):
```jinja2
{% if articles %}                            ← Keep this! Shows articles section if articles exist
{% for article in articles %}                ← Keep this! Loops through all articles
{{ article.display_name }}                   ← Keep this! Shows the article name
{{ article.html_path }}                      ← Keep this! Links to the article
{% endfor %}                                 ← Keep this! Ends the loop
{% endif %}                                  ← Keep this! Ends the if statement
```

**Rule of thumb:**
- Anything with `{% %}` or `{{ }}` = **DON'T TOUCH** (it's template logic)
- Everything else = **Safe to customize**

### Step-by-Step: Customize the Index Page

**File to edit:** `templates/tailwind.html.j2` (the default template)

#### Step 1: Change the Title and Subtitle

Find lines 6, 15, and 16:
```html
<title>marimo WebAssembly + GitHub Pages Template</title>           ← Line 6
...
<h1 class="text-2xl font-bold mb-2">marimo WebAssembly...</h1>     ← Line 15
<p class="text-sm">Interactive Python notebooks...</p>              ← Line 16
```

Replace with your text:
```html
<title>My Awesome Site</title>
...
<h1 class="text-2xl font-bold mb-2">My Awesome Site</h1>
<p class="text-sm">My personal website description</p>
```

#### Step 2: Remove or Replace the Logo

Find line 14:
```html
<img src="https://raw.githubusercontent.com/marimo-team/marimo/main/docs/_static/marimo-logotype-thick.svg" alt="marimo Logo" class="w-20 h-auto mx-auto mb-3">
```

**Option A - Remove it:** Delete the entire line

**Option B - Replace with your logo:**
1. Add your logo image to `public/` folder (e.g., `public/my-logo.png`)
2. Change the line to:
```html
<img src="public/my-logo.png" alt="My Logo" class="w-20 h-auto mx-auto mb-3">
```

#### Step 3: Customize Section Descriptions

Find these lines (around 21-22, 37-38, 53-54):
```html
<p class="text-center mb-4">Blog posts and static content</p>                    ← Articles description
<p class="text-center mb-4">Interactive notebooks in edit mode...</p>            ← Notebooks description
<p class="text-center mb-4">Interactive applications in run mode...</p>          ← Apps description
```

Change to whatever you want:
```html
<p class="text-center mb-4">My blog articles and tutorials</p>
<p class="text-center mb-4">Jupyter-style notebooks you can edit live</p>
<p class="text-center mb-4">Interactive data visualizations and demos</p>
```

#### Step 4: Customize the Footer

Find the footer section (around lines 70-77):
```html
<footer class="mt-10 pt-6 border-t border-gray-200 text-center text-sm text-gray-600">
  <p class="mb-2">Built with <a href="https://marimo.io" target="_blank" class="text-blue-500 hover:underline">marimo</a> - Interactive Python notebooks</p>
</footer>
```

Replace with your own footer:
```html
<footer class="mt-10 pt-6 border-t border-gray-200 text-center text-sm text-gray-600">
  <p class="mb-2">© 2025 Your Name | Built with marimo</p>
  <p>Follow me on <a href="https://twitter.com/yourhandle" class="text-blue-500">Twitter</a></p>
</footer>
```

#### Step 5: Change Colors

The template uses Tailwind CSS classes for colors. Here are common ones you can change:

**Background colors:**
- `bg-gray-100` → `bg-blue-100`, `bg-green-100`, `bg-purple-100`, etc.
- `bg-white` → `bg-gray-50`, `bg-blue-50`, etc.

**Text colors:**
- `text-gray-800` → `text-blue-800`, `text-green-800`, etc.
- `text-blue-500` → `text-purple-500`, `text-red-500`, etc.

**Button colors (for article/notebook/app buttons):**
- Articles: `bg-green-500 hover:bg-green-600` → change `green` to any color
- Notebooks: `bg-blue-500 hover:bg-blue-600` → change `blue` to any color
- Apps: `bg-amber-500 hover:bg-amber-600` → change `amber` to any color

Example: Change article button to purple:
```html
<a href="{{ article.html_path }}" class="inline-block bg-purple-500 hover:bg-purple-600 text-white py-1 px-3 rounded transition-colors">Read Article</a>
```

### Step-by-Step: Customize Article Pages

**File to edit:** `articles/example-article.html` (or your own article files)

Article pages are pure HTML - you can change EVERYTHING:

1. **Change the title:** Edit line 6 inside `<title>` tags
2. **Change the heading:** Edit the `<h1>` tag content
3. **Add your content:** Replace the example text with your own
4. **Add images:** Use `<img src="../public/your-image.png" />`
5. **Change colors:** Modify the Tailwind classes (same as above)

**Important:** Keep this line to link back to home:
```html
<a href="../index.html" class="text-blue-600 hover:text-blue-800">← Back to Home</a>
```

### Testing Your Changes

After making changes, always test locally before pushing:

```bash
# 1. Build the site
uv run .github/scripts/build.py

# 2. Serve locally
python -m http.server -d _site

# 3. Open http://localhost:8000 in your browser

# 4. Check:
#    - Does the index page look right?
#    - Do articles open correctly?
#    - Do marimo notebooks/apps still work?
```

### What NOT to Touch

**Never modify these:**
- Files in `_site/` (auto-generated, will be overwritten)
- `.github/scripts/build.py` (unless you know Python)
- The Jinja2 template logic: `{% %}` and `{{ }}`
- Files in `notebooks/` or `apps/` (unless you're editing the Python code)

### Getting Help

If you break something:
1. Check the build output for errors: `uv run .github/scripts/build.py`
2. Compare your changes to the original template
3. Look for mismatched `{% if %}` and `{% endif %}` tags
4. Make sure you didn't delete any `{{ variable }}` placeholders

## Deployment

Automatic deployment via GitHub Actions (`.github/workflows/deploy.yml`):
- Triggers on push to `main` branch
- Runs build script to export notebooks
- Uploads `_site/` artifact
- Deploys to GitHub Pages

**First-time setup**: Go to Settings > Pages and set Source to "GitHub Actions"

## Technology Stack

- **marimo**: Interactive Python notebooks
- **uv/uvx**: Fast Python package installer and runner
- **Jinja2**: Template engine for index page generation
- **GitHub Actions**: CI/CD for automated deployment
- **GitHub Pages**: Static site hosting

## Important Notes

- The `build.py` symlink at root points to `.github/scripts/build.py` for convenience
- All marimo notebooks must be valid Python files with marimo app structure
- WebAssembly export runs notebooks client-side (no server needed)
- Dependencies are bundled into the exported HTML files via WebAssembly
- Default template is `tailwind.html.j2` (can be changed in build command)
