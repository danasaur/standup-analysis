FROM jupyter/minimal-notebook
RUN conda install -c anaconda beautifulsoup4
RUN conda install -c anaconda pandas
