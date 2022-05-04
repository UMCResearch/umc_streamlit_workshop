# Step 0

Let's start by creating the python environment where all our dependencies will be installed.

This assumes you have conda installed. However this is an optional step.

```bash
conda env create -f environment.yml
conda activate mie2022_workshop_streamlit
```

Now let's install all the requirements which installs streamlit and other dependencies of this project.

```bash
pip install -r requirements.txt
```

> ##### :rocket: Fast forwrad
> Alternatively, if you don't have a working python or conda installation, you can fork a repl at: https://replit.com/@ShachiBista/Streamlit (requires registration, no affiliation).

You will also need a dataset, for this tutorial we will use the VAERS 2020 dataset available for download here: https://vaers.hhs.gov/data/datasets.html

Download the "CSV File (VAERS DATA)" column for the year 2020 and place it in the working directory.

# Step 1 - basic UI

Since we are aiming to build a search interface, the most basic interface we need is a search field. This is quite easily done with streamlit using the `text_input` method.

```python
{% include "tutorial_000.py" %}
```

Unlike most python scripts, streamlit has its own runtime which launches a local web server. In order to run this script, we need to invoke the `streamlit run` command:

```bash
$ streamlit run tutorial_000.py

  You can now view your Streamlit app in your browser.

  Local URL: http://localhost:8501
  Network URL: http://192.168.4.109:8501
```

The app can now be launched by opening `http://localhost:8501` in the browser as the instructions state.

# Step 2 - basic interactivity

So far our interface does not do anything useful, it just presents the user with a search input. It would be useful to be able to do something with the query provided by the user, let us look at the value of the `query` variable using the `write` method.

```python
{% include "tutorial_001.py" %}
```

As we see here the `query` variable is just a normal python string. We can also see that when the user has not input anything, it contains the empty string. We would like to handle this edge case.

```python
{% include "tutorial_002.py" %}
```

The way we handle the edge-case is very pythonic, we check if the query is present and perform some operation only when it is present, for e.g. print the query.

However, just printing the query is not very useful, let's use it to actually perform a search.

# Step 3 - simple search

For the purposes of this demo, we perform a simple case-insensitive exact-match search. However, you can use any advanced search. 

```python
{% include "tutorial_003.py" %}
```

First we load the dataset using `read_csv` from the pandas package, we import the columns `VAERS_ID` used for identifying a report for further assessment, `SEX` to get the sex distribution, `SYMPTOM_TEXT` which is the free-text field we will search for, `RECVDATE` representing the date that the report was received and `NUMDAYS` which denotes the number of days since the vaccine administration that the reaction occured.

For this step, we only use the `SYMPTOM_TEXT` column and search using the `str.contains` pandas method.

> ##### :warning: NOTE
> Do not forget to add the `encoding="cp1252"` parameter to `read_csv`. 

We use `st.table` to display the results.

# Step 4 - pagination

Our search seems to work! However there are too many results, our users want some way of limiting them!

Let us first add a slider to select the number of results to display. This can be done using the `st.slider` input type.

```python
{% include "tutorial_005.py" %}
```

That seems to work, however we can only see the first page of results. Let's add some basic pagination by calculating the number of pages as:

$ N_\text{pages} = \lceil \frac{N_\text{results}}{N_\text{results per page}} \rceil $

```python
{% include "tutorial_0051.py" %}
```

# Step 5 - sidebar

So far, we've worked on functionality. However streamlit can also perform some layout operations to a minimum degree. In our search engine for example, the presence of the pagination functions next to the search makes the UI look unncessarily complex. After all, we should focus on the results. 

With a simple application of `st.sidebar` we can move the paginations to the sidebar.

```python
{% include "tutorial_006.py" %}
```

---

# Bonus: Step 6 - charts!!

We get a request from our users that they want some form of overview of the results such as gender distribution and the histogram of date when the report was received. They feel that they don't have a good view of covid reporting patterns. 

Here we use the altair library to quickly add some basic charts and additionally lay them out using streamlit's column functionality.

```python
{% include "tutorial_007.py" %}
```