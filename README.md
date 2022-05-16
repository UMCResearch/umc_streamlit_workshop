# Streamlit workshop for MIE 2022

This repository is created for the MIE2022 workshop on [streamlit](https://streamlit.io).

This workshop requires the `conda` environment, which can be installed from [here](https://docs.conda.io/en/latest/miniconda.html).

Once installed, follow the instructions in [tutorial.md](tutorial.md) for a step-by-step walkthrough. 

## Preparation

Start by creating the python environment where all our dependencies will be installed.

We recommend that you install the dependencies in a conda environment, which can create and activate using the following commands:

```
conda env create -f environment.yml
conda activate mie2022_workshop_streamlit
```

Now let's install all the requirements which installs streamlit and other dependencies of this project.

```
pip install -r requirements.txt
```

> ##### :rocket: Fast forward
> Alternatively, if you don't have a working python or conda installation, you can fork a repl at: https://replit.com/@UMCResearch/mie2022workshopstreamlit (requires registration).
>
> Repl.it is a browser-based environment for running python scripts without installing it locally. UMC has no affiliation to repl.it.
> 
> Once the page opens, click on "Fork repl" to create your own local copy.

You will also need a dataset, for this tutorial we will use the VAERS 2020 dataset available for download here: https://vaers.hhs.gov/data/datasets.html

Download the "CSV File (VAERS DATA)" column for the year 2020 and place it in the working directory.

> #### :lying_face: Fake data
> 
> If you do not wish to download the VAERS data (or are unable to due to network issues), you can also use the `2020VAERSLike.csv` file included in this repo. This some fake data generated from sci.med newsgroup with similar distribution to the VAERS 2020 dataset.


## Running the tutorial (offline)

If you just want to see the tutorial and associated code without writing it, run the `tutorial.py` script like so:

```
streamlit run tutorial.py
```

## Feedback

If you have any feedback on the workshop and the presentation feel free to leave your comments here: https://forms.office.com/r/PcYbSuxeZ4
