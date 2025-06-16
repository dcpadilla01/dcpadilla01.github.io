# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This repository is a Jekyll-based personal website/blog using the Reverie theme. It's designed to be deployed on GitHub Pages.

## Development Commands

### Setup and Installation
```bash
# Install dependencies
bundle install
```

### Local Development
```bash
# Start local development server
bundle exec jekyll serve

# Start with drafts enabled
bundle exec jekyll serve --drafts

# Build the site
bundle exec jekyll build
```

## Site Structure

- `_config.yml`: Main configuration file for the Jekyll site
- `_posts/`: Directory containing blog posts as Markdown files
- `_pages/`: Directory containing static pages
- `_layouts/`: HTML templates for different page types
- `_includes/`: Reusable HTML components
- `_sass/`: SCSS style partials
- `assets/`: Contains compiled CSS and JavaScript files
- `images/`: Site images and resources

## Content Creation

### Adding New Posts
1. Create a new Markdown file in `_posts/` directory
2. Name the file using the format: `YYYY-MM-DD-title.md`
3. Include front matter at the top of the file:
   ```
   ---
   layout: post
   title: Your Post Title
   categories: [Category1, Category2]
   ---
   ```
4. Write post content in Markdown below the front matter

### Adding New Pages
1. Create a new Markdown file in `_pages/` directory
2. Include front matter with layout and permalink:
   ```
   ---
   layout: page
   title: Page Title
   permalink: /page-url/
   ---
   ```

## Site Configuration

Major site settings can be changed in `_config.yml`, including:
- Site title and description
- Author information
- Social media links
- Google Analytics integration
- Disqus commenting system
- Pagination settings