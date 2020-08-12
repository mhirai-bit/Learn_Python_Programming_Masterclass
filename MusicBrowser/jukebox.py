import sqlite3
import tkinter





class Scrollbox(tkinter.Listbox):

    def __init__(self, window, **kwargs):
        super().__init__(window, **kwargs)
        self.scrollbar = tkinter.Scrollbar(window, orient=tkinter.VERTICAL, command=self.yview)

    def grid(self, row, column, sticky="nsw", rowspan=1, columnspan=1, **kwargs):
        super().grid(row=row, column=column, sticky=sticky, rowspan=rowspan, columnspan=columnspan, **kwargs)
        self.scrollbar.grid(row=row, column=column, sticky="nse", rowspan=rowspan)
        self['yscrollcomman'] = self.scrollbar.set


class DataListBox(Scrollbox):

    def __init__(self, window, connection, table, field, sort_order=(), **kwargs):
        super().__init__(window, **kwargs)

        self.linked_box = None
        self.link_field = None
        self.link_value = None

        self.cursor = connection.cursor()
        self.table = table
        self.field = field


        self.bind('<<ListboxSelect>>', self.on_select)

        self.sql_select = "select " + self.field + ", _id" + " from " + self.table
        if sort_order:
            self.sql_sort = " order by " + ','.join(sort_order)
        else:
            self.sql_sort = " order by " + self.field

    def clear(self):
        self.delete(0, tkinter.END)

    def link(self, widget, link_field):
        self.linked_box = widget
        widget.link_field = link_field

    def requery(self, link_value=None):
        self.link_value = link_value    # store the id so we know the master record we're populated from
        if link_value and self.link_field:
            sql = self.sql_select + " where " + self.link_field + "=?" + self.sql_sort
            print(sql)      # todo delete this line
            self.cursor.execute(sql, (link_value,))
        else:
            print(self.sql_select + self.sql_sort)
            self.cursor.execute(self.sql_select + self.sql_sort)

        self.clear()
        for value in self.cursor:
            self.insert(tkinter.END, value[0])

        if self.linked_box:
            self.linked_box.clear()

    def on_select(self, event):
        if self.linked_box:
            print(self is event.widget) # todo delete this line
            index = self.curselection()[0]
            value = self.get(index),

            if self.link_value:
                value = value[0], self.link_value
                sql_where = " where " + self.field + "=? and " + self.link_field + "=?"
            else:
                sql_where = " where " + self.field + "=?"

            link_id = self.cursor.execute(self.sql_select + sql_where, value).fetchone()[1]
            self.linked_box.requery(link_id)


def get_songs(event):
    lb = event.widget
    index = int(lb.curselection()[0])
    album_name = lb.get(index),

    album_id = conn.execute("select albums._id from albums where albums.name=?", album_name).fetchone()
    alist = []
    for x in conn.execute("select songs.title from songs where songs.album=? order by songs.track", album_id):
        alist.append(x[0])
    songLV.set(tuple(alist))



if __name__ == '__main__':
    conn = sqlite3.connect("music.sqlite")
    mainWindow = tkinter.Tk()
    mainWindow.title = ('Music DB Browser')
    mainWindow.geometry('1024x768')

    mainWindow.columnconfigure(0, weight=2)
    mainWindow.columnconfigure(1, weight=2)
    mainWindow.columnconfigure(2, weight=2)
    mainWindow.columnconfigure(3, weight=1)     # spacer column on right

    mainWindow.rowconfigure(0, weight=1)
    mainWindow.rowconfigure(1, weight=5)
    mainWindow.rowconfigure(2, weight=5)
    mainWindow.rowconfigure(3, weight=1)

    # ===== labels =====
    tkinter.Label(mainWindow, text="Artists").grid(row=0, column=0)
    tkinter.Label(mainWindow, text="Albums").grid(row=0, column=1)
    tkinter.Label(mainWindow, text="Songs").grid(row=0, column=2)

    # ===== Artist Listbox ======
    artistList = DataListBox(mainWindow, conn, "artists", "name")
    artistList.grid(row=1, column=0, sticky="nsew", rowspan=2, padx=(30, 0))
    artistList.config(border=2, relief="sunken")

    artistList.requery()


    # ===== Albums Listbox =====
    albumLV = tkinter.Variable(mainWindow)
    albumLV.set(("Choose an artist",))
    albumList = DataListBox(mainWindow, conn, "albums", "name", sort_order=("name",))
    # albumList.requery()
    albumList.grid(row=1, column=1, sticky="nsew", padx=(30, 0))
    albumList.config(border=2, relief="sunken")

    # albumList.bind('<<ListboxSelect>>', get_songs)
    artistList.link(albumList, "artist")

    # ====== Songs Listbox =====
    songLV = tkinter.Variable(mainWindow)
    songLV.set(("Choose an album",))
    songList = DataListBox(mainWindow, conn, "songs", "title", ("track", "title"))
    # songList.requery()
    songList.grid(row=1, column=2, sticky="nsew", padx=(30,0))
    songList.config(border=2, relief="sunken")

    albumList.link(songList, "album")

    # ===== Main loop =====
    # testList = range(0, 100)
    # albumLV.set(tuple(testList))
    mainWindow.mainloop()
    print("closing database connection")
    conn.close()