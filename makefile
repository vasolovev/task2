make streamlit:
	pip install jupytext
	jupytext --to py task2.ipynb
	streamlit run task2.py
	
