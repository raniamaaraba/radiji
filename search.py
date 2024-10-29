import tkinter as tk


def exampleFuncForAutoComplete(a, b):
    print(a)
    print(b)
    return ["a", "l", "4", "agasfasf", "afasfauy678", "858afas"]


def exampleFunctionToSearchBarValueChanged(value):
    print(value)


class SearchBar(tk.Frame):
    def __init__(self, parent, allItems, widthInText=30, autoCompleteFunction=None, valuesToDisplay=4):
        """
        :param parent: The Parent Object
        :param allItems: this specifies the Items From Which the search happens
        :param widthInText: The width of search bar in text units but not pixels.
        :param autoCompleteFunction: if you want to specify your own function for autocomplete. Default function will be
               used when set to None
        :param valuesToDisplay: The No Of Values to Display at a time
        """
        tk.Frame.__init__(self, parent)
        self.width = widthInText
        self.allItems = allItems
        self.autoCompleteFunction = autoCompleteFunction
        self.valuesToDisplay = valuesToDisplay
        if len(self.allItems) > self.valuesToDisplay:
            self.displayValues = self.allItems[:self.valuesToDisplay]
        else:
            self.displayValues = self.allItems
        self.searchBarOptionSelectedFunc = None
        self.searchVar = tk.StringVar()
        self.searchBar = tk.Entry(self, textvariable=self.searchVar, width=self.width, font=("Arial", 20),
                                  selectbackground="#d9d9d9", selectforeground="#000000")
        self.listBox = tk.Listbox(self, width=self.width, height=len(self.displayValues), font=("Arial", 20),
                                  activestyle='none', selectbackground="#e8e8e8", selectforeground="#000000",
                                  borderwidth=2)

        self.searchBar.pack(side=tk.TOP, fill=tk.Y)
        self.updateListBox(self.displayValues)

        self.searchBar.bind("<KeyRelease>", self.keyPressOnSearchBar)
        self.listBox.bind("<Return>", self.returnPressedOnListBox)
        self.searchBar.bind("<Tab>", self.tabPressedOnEntry)
        self.listBox.bind("<Tab>", self.tabPressedOnListBox)
        self.listBox.bind("<<ListboxSelect>>", self.optionSelectedInListBox)

    def updateListBox(self, items):
        self.listBox.delete(0, tk.END)
        for item in items:
            self.listBox.insert(tk.END, item)

    def matchString(self, text1):
        if self.autoCompleteFunction is None:
            # s = time.time()
            allStrings = self.allItems
            text1 = [i for i in text1.lower()]
            sameMatches = {}
            for j in allStrings:
                sameMatches[j] = 0
            for idx, word in enumerate(allStrings):

                letters = [i for i in word]
                for letter in text1:
                    for letter2 in letters:
                        if letter == letter2.lower():
                            sameMatches[allStrings[idx]] += 1

            marklist = sorted(sameMatches.items(), key=lambda x: x[1], reverse=True)
            allafgag = []
            for sortedS in marklist:
                allafgag.append(sortedS[0])
            # e = time.time()
            return allafgag
        else:
            functionSorted = self.autoCompleteFunction

            return functionSorted(text1, self.allItems)

    def returnPressedOnListBox(self, e=None):
        index = self.listBox.curselection()
        self.listBox.pack_forget()
        if len(index) > 0:
            index = index[0]
            self.searchVar.set(self.displayValues[index])
            if self.searchBarOptionSelectedFunc is not None:
                self.searchBarOptionSelectedFunc(self.displayValues[index])

    def tabPressedOnEntry(self, e=None):
        if self.listBox.winfo_ismapped():
            self.listBox.select_set(0)

    def optionSelectedInListBox(self, e=None):
        index = self.listBox.curselection()
        if len(index) > 0:
            index = index[0]
            self.searchVar.set(self.displayValues[index])
            if self.searchBarOptionSelectedFunc is not None:
                self.searchBarOptionSelectedFunc(self.displayValues[index])

    def tabPressedOnListBox(self, e=None):
        if self.listBox.winfo_ismapped():
            index = self.listBox.curselection()
            if len(index) > 0:
                index = index[0]
                self.searchVar.set(self.displayValues[index])
                if self.searchBarOptionSelectedFunc is not None:
                    self.searchBarOptionSelectedFunc(self.displayValues[index])
            else:
                self.searchVar.set(self.displayValues[0])
                if self.searchBarOptionSelectedFunc is not None:
                    self.searchBarOptionSelectedFunc(self.displayValues[0])
            self.listBox.pack_forget()

    def keyPressOnSearchBar(self, e=None):
        if e.keycode == 40: # Down Arrow presses on search Bar
            self.listBox.focus_set()
            self.listBox.select_set(0)
            self.searchVar.set(self.displayValues[0])
            if self.searchBarOptionSelectedFunc is not None:
                self.searchBarOptionSelectedFunc(self.displayValues[0])
        elif e.keycode == 13: # Enter Pressed on search Bar
            self.listBox.pack_forget()
            self.searchVar.set(self.displayValues[0])
            if self.searchBarOptionSelectedFunc is not None:
                self.searchBarOptionSelectedFunc(self.displayValues[0])
        else:
            searchBarText = self.searchVar.get()
            if searchBarText == "":
                self.listBox.pack_forget()
            else:
                dataInOrder = self.matchString(searchBarText)
                dataInOrder = dataInOrder[:self.valuesToDisplay]
                self.displayValues = dataInOrder
                self.updateListBox(dataInOrder)
                if not self.listBox.winfo_ismapped():
                    self.listBox.pack(side=tk.BOTTOM)

    def bind_Function_To_SearchBar_Option_Selected(self, func):
        self.searchBarOptionSelectedFunc = func

    def configureListBox(self, **options):
        self.listBox.configure(options)

    def configureSearchBar(self, **options):
        self.searchBar.configure(options)

    def getValue(self):
        return self.searchVar.get()


if __name__ == "__main__":
    root = tk.Tk()
    width, height = 1000, 800
    root.geometry(f"{width}x{height}")
    searchBar1 = SearchBar(root, ["Hello", "Morning", "Good", "Bye", "Camera", "Monitor", "Android"])
    searchBar1.pack()
    root.mainloop()