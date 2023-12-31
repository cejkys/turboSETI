### Usage of the turbo_seti tutorials ###

The turbo_seti package is a Python tool, used and developed by SETI researchers at the Berkeley SETI Research Center. The turbo_seti search algorithm looks for narrow band signals that have a doppler drift, a feature expected from an alien source with a non-zero acceleration relative to our receivers on Earth. 

We'll search some HDF5 files that have been condensed into a single coarse channel and are routinely used for testing the code. They are located here: http://blpd14.ssl.berkeley.edu/voyager_2020/single_coarse_channel/ (total download size of 288 MB).

Typical SETI searches, such as described by https://arxiv.org/pdf/1906.07750.pdf, have used drift rates of up to ±4 Hz/s and a minimum signal-to-noise ratio of 10. We'll adapt those parameters for these tutorials.

There are 2 methods of executing a turbo_seti search processing after package installation:
1) Run the ```turboSETI``` executable at the bash (or Windows equivalent) command line in a terminal window.
2) Develop and run your own Python program which leverages the ```FindDoppler``` class and its functions.

Contained herein are two tutorials that display both methods:
* ```tutorial_1.ipynb``` - The simplest approach for searching and analyzing candidate events.  This is the recommended approach for most scientific work.
* ```tutorial_2.ipynb``` - Functionally equivalent to the first tutorial and exposes details of the event pipeline functions after the search completes.  This is a bit more complex model for use on a daily basis.

Both tutorials require the execution of an initialization notebook before using them: ```initialise.ipynb```.  This will download a set of 6 Voyager 2020 HDF5 files into a directory called "turbo_seti_data" under the user's home directory.

After the files are downloaded, we'll need to set up a conda environment by running the following commands in the bash terminal (or Windows equivalent):
```
$ conda deactivate
$ conda create -n turboseti # The string "turboseti" after -n is arbitrary.  The name of your environment can be any of your choosing.
$ conda activate turboseti
$ conda install pip
```

Now let's install the required packages:
```
$ python3 -m pip install -U blimpy      # <--- used by turbo_seti for Filterbank file access
$ python3 -m pip install -U turbo_seti  # <--- the latest stable turbo_seti
```

If you are trying out a new experimental version of turbo_seti, then the turbo_seti install step is a little different.  For example,
```
$ python3 -m pip install -U git+https://github.com/texadactyl/turbo_seti
```

Now we need to install into the turboseti environment as an IPython kernel, so we can use it in Jupyter:
```
$ conda install -c anaconda ipykernel
$ python -m ipykernel install --user --name=turboseti
```
A ready-to-use version of turboseti is now installed. You will have to restart Jupyter to see this kernel and be able to switch over (a quick refresh of the webpage should work).
