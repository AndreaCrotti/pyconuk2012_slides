# Makefile for Sphinx documentation
#

# You can set these variables from the command line.
SPHINXOPTS    =
SPHINXBUILD   = sphinx-build2
PAPER         =
BUILDDIR      = _build

# Internal variables.
PAPEROPT_a4     = -D latex_paper_size=a4
PAPEROPT_letter = -D latex_paper_size=letter
ALLSPHINXOPTS   =  $(PAPEROPT_$(PAPER)) $(SPHINXOPTS)
# the i18n builder cannot share the environment and doctrees with the others
I18NSPHINXOPTS  = $(PAPEROPT_$(PAPER)) $(SPHINXOPTS) .

.PHONY: deco zeromq_gen clean

all: zeromq_gen deco

clean:
	-rm -rf deco_slides/* zeromq_slides/*

deco:
	$(SPHINXBUILD) -b slides $(ALLSPHINXOPTS) deco_context deco_slides
	@echo "Build finished for decorator slides"

zeromq_gen:
	$(SPHINXBUILD) -b slides $(ALLSPHINXOPTS) zeromq zeromq_slides
	@echo "Build finished for zeromq slides"
