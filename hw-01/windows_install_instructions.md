# Installing Cygwin 

Please do this before the first class.

* Go to https://cywgin.com/install.html
* Download the 64-bit version (setup-x86_53.exe) and open it.
* Click through the first setup window (Cygwin Setup).
* "Choose Installation Type" → "Install from Internet."
* "Choose Installation Directory" → whatever you'd like, but the default (C:\cygwin64) is good.
* "Select Local Package Directory" → again, whatever you'd like, but the Downloads default  is good.
* "Select Connection Type" → "Direct Connection"
* "Choose Download Sites" → any are fine.
* "Select packages."  Pay attention here: what you're doing is selecting the "additional prorams that you'll want!
   * search "git".  Expand "Devel" (developpper).  Click on "git: Distributed version control system", so that it says 2.8.2-1 (or so), instead of "Skip".
   * search "vim".  Expand "Editors" (text editors).  Click on "vim: Vi IMproved - enhanced vi editor\", so that it says 7.3.2181-1, instead of "Skip"
   * search "python3".  Expand "Python.  Click on "python3: Py3K language interpreter" to see version 3.2.5-4 instead of "Skip".
   * search "curl".  Expand "net".  Click on curl so that it doesn't Skip.
   * Next.
* "Resolving Dependencies" → Next.  (i.e., leave "Select required packages (RECOMMENDED)" checked.)
* The setup will now start "spinning."  Give it some time.
* "Installation Status and Create Icons" → Up to you ("Finish").  I do have the icons.

Bonus: if you need to install additional packages, you can just run the exact same cygwin installer, over and over again, adding the extra packages you want (e.g., curl).

# Install Anaconda
* Go to https://www.continuum.io/downloads.  Download and open the 64-bit installer.  (Don't give them your email!)
* Setup: Next.
* "License Agreement" → Agree to the terms and conditions.
* "Select Installation Type" → Just Me (recommended).
* "Choose Install Location" → Default is probably fine.  *Make a note of where it goes.*  In my case:
   * C:\cygwin64\home\\\<YOUR_USER_ID\>\Continuum\Anaconda3  (<YOUR_USER_ID> is actually your user id, not that string.)
* "Advanced Installation Options" → just accept. "Install."  (Let it go.)
* Learn about Anaconda cloud only if you feel like it (no).
* Now, open up cygwin.  You will be at /home/<YOUR_USER_ID>/.  Type `which python`.  It will probably _not_ be the one you just installed.  Type (with an appropriate substitution for the path) `echo 'export PATH=/the/path/to/your/Continuum/Anaconda3:$PATH' >> ~/.bashrc`.
   * What is this doing?  `echo` just 'parrots' the rest of the line.  `export PATH` is telling the system where to look for programs.  In this case, you're adding `.../Anaconda3` to the existing `$PATH`.  You are then placing these (`>>`) at the end of your preferences file, `~/.bashrc`.  
* Now, when you open cygwin, you should be able to get a python prompt via `python -i` (return) (it should say "Python 3.5.2 |Anaconda 4.1.1 ..."), and a Jupyter notebook with `./Continuum/Anaconda3/Scripts/jupyter-notebook.exe` (return).

# Atom Install.
* Go to atom.io and download the Windows installer.  Launch it.  It is that simple.
