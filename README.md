# Zhejiang Lab LaTeX Paper Template

This repository contains a LaTeX template for academic papers, designed for researchers at Zhejiang Lab.

## Features

- Professional academic paper styling
- Single and two-column layout options
- Support for mathematical expressions, tables, and figures
- Properly structured sections for academic papers
- Consistent styling for headings, captions, and citations

## Prerequisites

To use this template, you need:

- A LaTeX distribution (TeXLive, MiKTeX, or MacTeX)
- A LaTeX editor or IDE (Overleaf, TeXStudio, VS Code with LaTeX Workshop, etc.)

## Usage

### Basic Setup

1. Clone this repository or download it as a ZIP file
2. Open `paper.tex` in your LaTeX editor
3. Modify the paper's title, authors, and affiliation in the preamble
4. Edit the content in the section files located in the `sections/` directory

### Layout Options

- For single-column layout (default): `\documentclass[]{bytedance_seed}`
- For two-column layout: `\documentclass[twocolumn]{bytedance_seed}`

### Section Files

The paper content is organized in separate files within the `sections/` directory:

- `000abstract.tex` - Paper abstract
- `010intro.tex` - Introduction
- `030data.tex` - Data description and methodology
- `040rm.tex` - Research methods
- `050rl.tex` - Results
- `060Experiments.tex` - Experiments
- `070Infra.tex` - Infrastructure details
- `100conclusion.tex` - Conclusion
- `appendix.tex` - Appendix materials

### Citations

The template uses the `unsrt` bibliography style. Add your references to `main.bib` and cite them in your paper using the `\cite{}` command.

## Compilation

To generate the PDF:

```bash
pdflatex paper.tex
bibtex paper
pdflatex paper.tex
pdflatex paper.tex
```

Or use your LaTeX editor's build function.

## Troubleshooting

- **Font Warnings**: The template includes the `fix-cm` package to handle small font sizes in mathematical expressions.
- **Header Height Warning**: The template sets `\headheight` to 64pt to accommodate the header content.

## Version History

- v1.0.0 (April 26, 2025) - Initial release

## License

This template is provided for use by researchers at Zhejiang Lab. Please consult your institution's policies regarding the use and distribution of this template.
