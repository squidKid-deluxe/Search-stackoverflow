"""
Script takes information from radiobuttons, checkbuttons,
and entries and creates a URL that it opens in your default web browser.
"""

import tkinter as tk
from webbrowser import open_new_tab

# Create tkinter window and set the title of it.
ROOT = tk.Tk()
ROOT.title("Search Stackoverflow Questions")

# I like to define my definitions before tkinter widgets
def search():
    """
    Do the actual searching
    """

    def tags():
        """
        Parse the tag information
        """
        # initalise varibles
        tagged = ""
        tag = ""

        # As long as tags are provided, get the tags and strip any commas
        if E1.get() != "":
            tagged = E1.get().replace(",", "")

        # if there are more than one tags...
        if len(tagged.split()) > 1:
            # go through each one and format tham URL-style
            for item in tagged.split():
                tag += item + "%20"
        # otherwise, continue
        else:
            tag = tagged

        # as long as tags are provided, add their url piece to the url
        if tag != "":
            tag = "/tagged/" + tag

        # Strip trailing '%20's
        tag = tag.strip("%20")

        # return the tags
        return tag

    def filters():
        """
        Parse the filters information
        """
        # initalize the varible
        ret_val = ""

        # get the values of the checkbuttons to aviod repeatedly getting them
        check1 = CHECKVAR1.get()
        check2 = CHECKVAR2.get()
        check3 = CHECKVAR3.get()

        # as long as at least one checkbutton is selected, add the beginning URL piece
        if check1 + check2 + check3 != "000":
            ret_val += "&filters="

        # Check if each checkbutton is selected, and if the current button is, 
        #    add its URL piece
        if check1 != "0":
            ret_val += "NoAnswers,"

        if check2 != "0":
            ret_val += "NoAcceptedAnswer,"

        if check3 != "0":
            ret_val += "Bounty,"

        # return the filters with trailing commas striped
        return ret_val.strip(",")

    # Make the URL with returned values
    url = f"https://stackoverflow.com/questions{tags()}?sort={VAR2.get()}{filters()}&edited=true"

    # open the url
    open_new_tab(url)

# create the frame used for all the inputs (radiobuttons, checkbuttons, and entry)
FRAME = tk.Frame(ROOT)
FRAME.grid(row=1, column=1)

# ==================================================================================================
# ========================================Check Buttons=============================================
# ==================================================================================================

# Create the 'Filtered by' label
L1 = tk.Label(FRAME, text="Filtered by")
L1.grid(row=1, column=1)

# Create the varibles for the checkbuttons
CHECKVAR1 = tk.StringVar()
CHECKVAR2 = tk.StringVar()
CHECKVAR3 = tk.StringVar()

# Create all the Checkbuttons
C1 = tk.Checkbutton(
    FRAME,
    text="No Answers",
    anchor="w",
    variable=CHECKVAR1,
    onvalue="NoAnswers",
    offvalue=0,
    width=18,
)
C2 = tk.Checkbutton(
    FRAME,
    text="No Accepted Answer",
    anchor="w",
    variable=CHECKVAR2,
    onvalue="NoAcceptedAnswer",
    offvalue=0,
    width=18,
)
C3 = tk.Checkbutton(
    FRAME,
    text="Has Bounty",
    anchor="w",
    variable=CHECKVAR3,
    onvalue="HasBounty",
    offvalue=0,
    width=18,
)

# Pack all the checkbuttons
C1.grid(row=2, column=1)
C2.grid(row=3, column=1)
C3.grid(row=4, column=1)

# deselect all the checkbuttons
C1.deselect()
C2.deselect()
C3.deselect()

# ==================================================================================================
# ========================================Radio Buttons=============================================
# ==================================================================================================

# create the varible for the radiobuttons
VAR2 = tk.StringVar()

# create the 'Sorted by' label
tk.Label(FRAME, text="Sorted by").grid(row=1, column=2)

# Create all the radio buttons
R1 = tk.Radiobutton(
    FRAME, text="Newest", anchor="w", width=18, variable=VAR2, value="Newest"
)
R1.grid(row=2, column=2)

tk.Radiobutton(
    FRAME,
    text="Recent Activity",
    anchor="w",
    width=18,
    variable=VAR2,
    value="RecentActivity",
).grid(row=3, column=2)

tk.Radiobutton(
    FRAME, text="Most Votes", anchor="w", width=18, variable=VAR2, value="MostVotes"
).grid(row=4, column=2)

tk.Radiobutton(
    FRAME,
    text="Most Frequent",
    anchor="w",
    width=18,
    variable=VAR2,
    value="MostFrequent",
).grid(row=5, column=2)

tk.Radiobutton(
    FRAME,
    text="Bounty Ending Soon",
    anchor="w",
    width=18,
    variable=VAR2,
    value="BountyEndingSoon",
).grid(row=6, column=2)

# select the 'Newest' radiobutton by default
R1.select()

# ==================================================================================================
# ========================================'Tagged With'=============================================
# ==================================================================================================

# Create the 'Tagged with' label
tk.Label(FRAME, text="Tagged with").grid(row=1, column=3)


# Create the entry widget for the tags
E1 = tk.Entry(FRAME, width=18)
E1.grid(row=2, column=3)

# ==================================================================================================
# =============================================Send=================================================
# ==================================================================================================

# create the search button
tk.Button(
    ROOT,
    text="Search",
    bg="blue",
    fg="white",
    activebackground="blue",
    activeforeground="white",
    command=search,
).grid(row=2, column=1)

# mainloop
ROOT.mainloop()
