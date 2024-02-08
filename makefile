make streamlit:
	pip install jupytext
	pip install streamlit
	pip install streamlit_jupyter
	jupytext --to py jupyter.ipynb
	streamlit run jupyter.py
	
